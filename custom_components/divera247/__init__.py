"""Divera 24/7 Component."""

import asyncio
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_API_KEY, CONF_NAME, Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.components.select import SelectEntity

from .const import (
    CONF_FLOW_MINOR_VERSION,
    CONF_FLOW_VERSION,
    DATA_ACCESSKEY,
    DATA_ACCESSKEY,
    DATA_BASE_URL,
    DATA_UCRS,
    DIVERA_BASE_URL,
    DOMAIN,
    LOGGER,
)
from .coordinator import DiveraCoordinator
from .data import DiveraRuntimeData
from .divera247 import DiveraClient, DiveraError

PLATFORMS = [
    Platform.SELECT,
    Platform.SENSOR,
    Platform.CALENDAR,
    Platform.BINARY_SENSOR,
]


# Diese Klasse stellt die Organisations-Auswahl als Select-Entität dar
class OrganizationSelectEntity(SelectEntity):
    """Repräsentiert die Organisations-Auswahl als Select-Entität."""

    def __init__(self, name, options, initial):
        self._name = name
        self._options = options
        self._current_value = initial

    @property
    def name(self):
        """Gibt den Namen der Entität zurück."""
        return self._name

    @property
    def current_option(self):
        """Gibt die aktuell gewählte Option zurück."""
        return self._current_value

    @property
    def options(self):
        """Gibt die möglichen Optionen zurück."""
        return self._options

    async def async_select_option(self, option: str) -> None:
        """Ändert die aktuell gewählte Option."""
        self._current_value = option
        self.async_write_ha_state()


type DiveraConfigEntry = ConfigEntry[DiveraRuntimeData]


async def async_setup_entry(hass: HomeAssistant, entry: DiveraConfigEntry):
    """Set up Divera as config entry."""

    accesskey: str = entry.data.get(DATA_ACCESSKEY)
    ucr_ids = entry.data.get(DATA_UCRS)
    base_url = entry.data.get(DATA_BASE_URL, DIVERA_BASE_URL)

    divera_hass_data = hass.data.setdefault(DOMAIN, {})
    divera_hass_data[entry.entry_id] = {}

    websession = async_get_clientsession(hass)
    tasks = []
    coordinators = {}

    # Erstelle die Select-Entität für die Auswahl der Organisation
    organization_select = OrganizationSelectEntity(
        name="Organisation wählen", 
        options=["THW", "Feuerwehr", "DRK", "DLRG"],  # Optionen
        initial="THW",  # Standard-Auswahl
    )

    # Füge die Entität zu den Hass-Daten hinzu
    hass.data[DOMAIN]["organization_select"] = organization_select

    for ucr_id in ucr_ids:
        divera_coordinator = DiveraCoordinator(
            hass, websession, accesskey, base_url=base_url, ucr_id=ucr_id
        )
        coordinators[ucr_id] = divera_coordinator
        tasks.append(
            asyncio.create_task(divera_coordinator.async_config_entry_first_refresh())
        )

    entry.runtime_data = DiveraRuntimeData(coordinators)

    await asyncio.wait(tasks)

    entry.async_on_unload(entry.add_update_listener(async_update_listener))

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Asynchronous update listener."""

    await hass.config_entries.async_reload(entry_id=entry.entry_id)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload Divera config entry."""

    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, component)
                for component in PLATFORMS
            ]
        )
    )
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
        if not hass.data[DOMAIN]:
            hass.data.pop(DOMAIN)
    return unload_ok


async def async_migrate_entry(hass, config_entry: ConfigEntry):
    """Migrate old entry."""

    LOGGER.debug("Migrating from version %s", config_entry.version)

    if (
        config_entry.version > CONF_FLOW_VERSION
        or config_entry.minor_version > CONF_FLOW_MINOR_VERSION
    ):
        LOGGER.debug(
            "Migration to version %s.%s failed. Downgraded ",
            config_entry.version,
            config_entry.minor_version,
        )
        return False

    new = {**config_entry.data}
    if config_entry.version < 3:
        accesskey: str = new.get(CONF_API_KEY)
        new.pop(CONF_API_KEY)
        new[DATA_ACCESSKEY] = accesskey
        new.pop(CONF_NAME)

        websession = async_get_clientsession(hass)
        divera_client: DiveraClient = DiveraClient(websession, accesskey=accesskey)
        try:
            await divera_client.pull_data()
        except DiveraError:
            LOGGER.debug(
                "Migration to version %s.%s failed.",
                config_entry.version,
                config_entry.minor_version,
            )
            return False
        ucr_id = divera_client.get_active_ucr()
        new[DATA_UCRS] = [ucr_id]

    hass.config_entries.async_update_entry(
        config_entry,
        data=new,
        minor_version=CONF_FLOW_MINOR_VERSION,
        version=CONF_FLOW_VERSION,
    )
    LOGGER.debug(
        "Migration to version %s.%s successful",
        config_entry.version,
        config_entry.minor_version,
    )
    return True