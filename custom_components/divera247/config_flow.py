"""Config flow for Divera 24/7 integration."""

from typing import Any

from voluptuous import Optional, Required, Schema

from homeassistant.config_entries import HANDLERS, ConfigEntry, ConfigFlow, OptionsFlow
from homeassistant.data_entry_flow import FlowHandler
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.selector import (
    SelectSelector,
    SelectSelectorConfig,
    TextSelector,
    TextSelectorConfig,
    TextSelectorType,
)

from .const import (
    CONF_ACCESSKEY,
    CONF_BASE_URL,
    CONF_CLUSTERS,
    CONF_FLOW_MINOR_VERSION,
    CONF_FLOW_NAME_API,
    CONF_FLOW_NAME_RECONFIGURE,
    CONF_FLOW_NAME_UCR,
    CONF_FLOW_VERSION,
    CONF_SCAN_INTERVAL,
    CONF_VEHICLE_NAME_MODE,
    DATA_ACCESSKEY,
    DATA_BASE_URL,
    DATA_UCRS,
    DIVERA_BASE_URL,
    DOMAIN,
    ERROR_AUTH,
    ERROR_CONNECTION,
    VEHICLE_NAME_MODES,
)
from .divera247 import DiveraAuthError, DiveraClient, DiveraConnectionError


class DiveraFlow(FlowHandler):
    """
    Flow handler for Divera integration.

    This class manages the configuration flow for setting up the Divera integration.
    """

    def __init__(self, config_entry: ConfigEntry = None):
        """
        Initialize DiveraFlow.

        Args:
            config_entry (ConfigEntry, optional): Configuration entry for Divera integration. Defaults to None.
        """
        self._config_entry: ConfigEntry | None = config_entry
        self._divera_client: DiveraClient | None = None
        self._data: dict[str, Any] = {}
        self._scan_interval: int = 10

    async def _show_clusters_form(self, active_cluster_names, cluster_names, errors):
        """
        Show the form to select clusters.

        Args:
            active_cluster_names (list): List of active cluster names.
            cluster_names (list): List of all cluster names.
            errors (dict): Dictionary of errors.

        Returns:
            dict: The form to present to the user.
        """
        cluster_schema = Schema(
            {
                Required(CONF_CLUSTERS, default=active_cluster_names): SelectSelector(
                    SelectSelectorConfig(options=cluster_names, multiple=True)
                ),
            }
        )
        return self.async_show_form(
            step_id=CONF_FLOW_NAME_UCR, data_schema=cluster_schema, errors=errors
        )

    async def _show_api_form(self, errors):
        """
        Show the form to enter API details.

        Args:
            errors (dict): Dictionary of errors.

        Returns:
            dict: The form to present to the user.
        """
        api_schema = Schema(
            {
                Required(CONF_ACCESSKEY, default=""): str,
                Optional(
                    CONF_BASE_URL, description={"suggested_value": DIVERA_BASE_URL}
                ): TextSelector(TextSelectorConfig(type=TextSelectorType.URL)),
                Required(CONF_SCAN_INTERVAL, default="60"): str,
            },
        )
        return self.async_show_form(
            step_id=CONF_FLOW_NAME_API, data_schema=api_schema, errors=errors
        )


@HANDLERS.register(DOMAIN)
class DiveraConfigFlow(DiveraFlow, ConfigFlow):
    """
    Handle a config flow for Divera integration.

    This class manages the configuration flow for setting up the Divera integration.
    """

    VERSION = CONF_FLOW_VERSION
    MINOR_VERSION = CONF_FLOW_MINOR_VERSION

    def __init__(self):
        """Initialize DiveraConfigFlow."""
        super().__init__()

    async def async_step_user(self, user_input: dict[str, Any] | None = None):
        """
        Handle the initial step.

        Args:
            user_input (dict): User input.

        Returns:
            dict: The next step or form to present to the user.
        """
        return await self.async_step_api(user_input)

    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None):
        """
        Handle the reconfigure step to allow to reconfigure a config entry.

        Args:
            user_input (dict): User input.

        Returns:
            dict: The next step or form to present to the user.
        """
        self._config_entry = self._get_reconfigure_entry()

        websession = async_get_clientsession(self.hass)
        accesskey = self._config_entry.data.get(DATA_ACCESSKEY)
        base_url = self._config_entry.data.get(DATA_BASE_URL)

        self._divera_client = DiveraClient(websession, accesskey, base_url)

        return await self.async_step_reconfigure_confirm()

    async def async_step_reconfigure_confirm(
        self, user_input: dict[str, Any] | None = None
    ):
        """
        Handle the reconfigure confirm step to reconfigure active clusters of a config entry.

        Args:
            user_input (dict): User input.

        Returns:
            ConfigFlowResult: The next step or form to present to the user.
        """
        errors: dict[str, str] = {}
        if not self._config_entry:
            errors["base"] = "config_entry_missing"
            return self.async_abort(reason="config_entry_missing")

        try:
            await self._divera_client.pull_data()
            if self._divera_client.get_ucr_count() == 1:
                return self.async_abort(reason="only_one_unit")
        except DiveraAuthError:
            errors["base"] = ERROR_AUTH
        except DiveraConnectionError:
            errors["base"] = ERROR_CONNECTION

        if user_input is not None and not errors:
            selected_cluster_names = user_input[CONF_CLUSTERS]
            ucr_ids = self._divera_client.get_ucr_ids(selected_cluster_names)
            # Keep for next step; update both data and options after name selection
            self._data[DATA_UCRS] = ucr_ids
            return await self.async_step_reconfigure_vehicle_name_selection()

        cluster_names = self._divera_client.get_all_cluster_names()
        ucr_ids = self._config_entry.data.get(DATA_UCRS)
        active_cluster_names = self._divera_client.get_cluster_names_from_ucrs(ucr_ids)

        cluster_schema = Schema(
            {
                Required(CONF_CLUSTERS, default=active_cluster_names): SelectSelector(
                    SelectSelectorConfig(options=cluster_names, multiple=True)
                ),
            }
        )
        return self.async_show_form(
            step_id=CONF_FLOW_NAME_RECONFIGURE,
            data_schema=cluster_schema,
            errors=errors,
        )

    async def async_step_reconfigure_vehicle_name_selection(
        self, user_input: dict[str, Any] | None = None
    ):
        """Additional reconfigure step to select vehicle name mode.

        Allows adjusting the vehicle name selection via "Reconfigure".
        """
        errors: dict[str, str] = {}

        current_mode = self._config_entry.options.get(
            CONF_VEHICLE_NAME_MODE, VEHICLE_NAME_MODES[0]
        )

        if user_input is not None and not errors:
            vehicle_name_mode = user_input.get(
                CONF_VEHICLE_NAME_MODE, current_mode
            )
            # Apply both data and options updates, then reload and abort
            await self.hass.config_entries.async_update_entry(
                self._config_entry,
                data={
                    **self._config_entry.data,
                    DATA_UCRS: self._data.get(DATA_UCRS, self._config_entry.data.get(DATA_UCRS)),
                },
                options={
                    **self._config_entry.options,
                    CONF_VEHICLE_NAME_MODE: vehicle_name_mode,
                },
            )
            self.hass.async_create_task(
                self.hass.config_entries.async_reload(self._config_entry.entry_id)
            )
            return self.async_abort(reason="reconfigure_successful")

        vehicle_schema = Schema(
            {
                Required(CONF_VEHICLE_NAME_MODE, default=current_mode): SelectSelector(
                    SelectSelectorConfig(
                        options=VEHICLE_NAME_MODES,
                        multiple=False,
                        translation_key="vehicle_name_mode",
                    )
                ),
            }
        )
        return self.async_show_form(
            step_id="reconfigure_vehicle_name_selection",
            data_schema=vehicle_schema,
            errors=errors,
        )

    async def async_step_api(self, user_input: dict[str, Any] | None = None):
        """
        Handle the API step of the config flow.

        Args:
            user_input (dict[str, Any], optional): User input. Defaults to None.

        Returns:
            Dict[str, Any]: Dictionary of step results.
        """
        errors: dict[str, str] = {}

        if user_input is not None:
            accesskey = user_input.get(CONF_ACCESSKEY)
            base_url = user_input.get(CONF_BASE_URL)
            # Validate scan interval
            scan_val = user_input.get(CONF_SCAN_INTERVAL, "60")
            try:
                scan_int = int(scan_val)
                if scan_int < 10 or scan_int > 300:
                    errors[CONF_SCAN_INTERVAL] = "range_error"
                else:
                    self._scan_interval = scan_int
            except (TypeError, ValueError):
                errors[CONF_SCAN_INTERVAL] = "invalid_int"

            websession = async_get_clientsession(self.hass)
            self._divera_client = DiveraClient(websession, accesskey, base_url)
            try:
                await self._divera_client.pull_data()
            except DiveraAuthError:
                errors["base"] = ERROR_AUTH
            except DiveraConnectionError:
                errors["base"] = ERROR_CONNECTION

            if not errors:
                await self.check_unique_id()

                if not self._divera_client.check_usergroup_id():
                    return self.async_abort(reason="not_supported")

                if self._divera_client.get_ucr_count() > 1:
                    return await self.async_step_user_cluster_relation()
                
                # Single cluster - proceed to vehicle name selection
                return await self.async_step_vehicle_name_selection()

        return await self._show_api_form(errors)

    async def async_step_user_cluster_relation(
        self, user_input: dict[str, Any] | None = None
    ):
        """Second step in config flow to select the cluster of the user.

        When the account is part of multiple clusters we let the user pick which to activate.
        """
        errors: dict[str, str] = {}

        if user_input is not None and not errors:
            selected_cluster_names = user_input[CONF_CLUSTERS]
            ucr_ids = self._divera_client.get_ucr_ids(selected_cluster_names)
            self._data[DATA_UCRS] = ucr_ids
            return await self.async_step_vehicle_name_selection()

        cluster_names = self._divera_client.get_all_cluster_names()
        # Preselect first cluster
        active_cluster_names = [cluster_names[0]] if cluster_names else []

        return await self._show_clusters_form(
            active_cluster_names, cluster_names, errors
        )
    
    async def async_step_vehicle_name_selection(
        self, user_input: dict[str, Any] | None = None
    ):
        """Third step in config flow to select vehicle name mode.

        Let the user choose which vehicle name field to use for sensor names.
        """
        errors: dict[str, str] = {}

        if user_input is not None and not errors:
            vehicle_name_mode = user_input.get(CONF_VEHICLE_NAME_MODE, VEHICLE_NAME_MODES[0])
            
            # If DATA_UCRS not yet set (single cluster case), set it now
            if DATA_UCRS not in self._data:
                ucr_id: int = self._divera_client.get_default_ucr()
                self._data[DATA_UCRS] = [ucr_id]
            
            self._data[DATA_BASE_URL] = self._divera_client.get_base_url()
            self._data[DATA_ACCESSKEY] = self._divera_client.get_accesskey()
            
            # Store initial vehicle name mode in options
            title = self._divera_client.get_full_name()
            return self.async_create_entry(
                title=title, 
                data=self._data,
                options={
                    CONF_VEHICLE_NAME_MODE: vehicle_name_mode,
                    CONF_SCAN_INTERVAL: self._scan_interval,
                }
            )

        vehicle_schema = Schema(
            {
                Required(CONF_VEHICLE_NAME_MODE, default=VEHICLE_NAME_MODES[0]): SelectSelector(
                    SelectSelectorConfig(
                        options=VEHICLE_NAME_MODES,
                        multiple=False,
                        translation_key="vehicle_name_mode",
                    )
                ),
            }
        )
        return self.async_show_form(
            step_id="vehicle_name_selection",
            data_schema=vehicle_schema,
            errors=errors,
        )

    async def check_unique_id(self):
        """Check uniqueness of user email to avoid duplicate entries."""
        uid = self._divera_client.get_email()
        await self.async_set_unique_id(uid)
        self._abort_if_unique_id_configured()

    # NOTE: Options flow handled by separate handler below


class DiveraOptionsFlowHandler(OptionsFlow):
    """Options flow for Divera integration (scan interval, vehicle name mode)."""

    def __init__(self, config_entry: ConfigEntry) -> None:
        self._entry = config_entry

    async def async_step_init(self, user_input: dict[str, Any] | None = None):  # type: ignore[override]
        errors: dict[str, str] = {}
        current_scan = self._entry.options.get(CONF_SCAN_INTERVAL, 60)
        current_mode = self._entry.options.get(
            CONF_VEHICLE_NAME_MODE, VEHICLE_NAME_MODES[0]
        )

        if user_input is not None:
            scan = user_input.get(CONF_SCAN_INTERVAL, current_scan)
            try:
                scan_int = int(scan)
                if scan_int < 10 or scan_int > 300:
                    errors[CONF_SCAN_INTERVAL] = "range_error"
                else:
                    new_options = {
                        **self._entry.options,
                        CONF_SCAN_INTERVAL: scan_int,
                        CONF_VEHICLE_NAME_MODE: user_input.get(
                            CONF_VEHICLE_NAME_MODE, current_mode
                        ),
                    }
                    # Create entry and trigger reload so sensors get recreated with new naming mode
                    result = self.async_create_entry(
                        title="Divera Options", data=new_options
                    )
                    # Reload integration to apply option changes (add task so flow can finish)
                    self.hass.async_create_task(
                        self.hass.config_entries.async_reload(self._entry.entry_id)
                    )
                    return result
            except (TypeError, ValueError):
                errors[CONF_SCAN_INTERVAL] = "invalid_int"

        schema = Schema(
            {
                Required(CONF_SCAN_INTERVAL, default=current_scan): str,
                Required(CONF_VEHICLE_NAME_MODE, default=current_mode): SelectSelector(
                    SelectSelectorConfig(
                        options=VEHICLE_NAME_MODES,
                        multiple=False,
                        translation_key="vehicle_name_mode",
                    )
                ),
            }
        )
        return self.async_show_form(step_id="init", data_schema=schema, errors=errors)


async def async_get_options_flow(config_entry: ConfigEntry):  # type: ignore[override]
    return DiveraOptionsFlowHandler(config_entry)
