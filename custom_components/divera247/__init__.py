"""Divera 24/7 Component."""

import asyncio
from pathlib import Path

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_API_KEY, CONF_NAME, Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import (
    CONF_FLOW_MINOR_VERSION,
    CONF_FLOW_VERSION,
    CONF_SCAN_INTERVAL,
    DATA_ACCESSKEY,
    DATA_BASE_URL,
    DATA_UCRS,
    DEFAULT_SCAN_INTERVAL,
    DIVERA_BASE_URL,
    DOMAIN,
    LOGGER,
)
from .coordinator import DiveraCoordinator
from .data import DiveraRuntimeData
from .divera247 import DiveraClient, DiveraError

__version__ = "0.0.0"  # Lazy-loaded inside async_setup_entry

PLATFORMS = [
    Platform.SELECT,
    Platform.SENSOR,
    Platform.CALENDAR,
    Platform.BINARY_SENSOR,
    Platform.BUTTON,
    Platform.DEVICE_TRACKER,
]

type DiveraConfigEntry = ConfigEntry[DiveraRuntimeData]


async def async_setup_entry(hass: HomeAssistant, entry: DiveraConfigEntry):
    """
    Set up Divera as config entry.

    :param hass: Home Assistant instance
    :param entry: Config entry for Divera
    :return: True if setup was successful
    """
    # Lazy-load version now (avoids file I/O at import time)
    try:
        manifest_path = Path(__file__).parent / "manifest.json"
        import json
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        globals()["__version__"] = manifest.get("version", "0.0.0")
    except Exception:  # pragma: no cover - non-critical
        globals()["__version__"] = "0.0.0"

    LOGGER.info(
        "Starting Divera 24/7 setup (version=%s, entry_id=%s)", __version__, entry.entry_id
    )

    accesskey: str | None = entry.data.get(DATA_ACCESSKEY)
    ucr_ids: list[int] | None = entry.data.get(DATA_UCRS)
    base_url: str = entry.data.get(DATA_BASE_URL, DIVERA_BASE_URL)

    if not accesskey or not ucr_ids:
        LOGGER.error(
            "Setup aborted: missing accesskey (%s) or ucr_ids (%s) in config entry data.",
            bool(accesskey),
            bool(ucr_ids),
        )
        return False

    divera_hass_data = hass.data.setdefault(DOMAIN, {})
    divera_hass_data[entry.entry_id] = {}

    websession = async_get_clientsession(hass)
    tasks = []
    coordinators = {}

    # Create a DiveraClient instance and store it for the service
    divera_client = DiveraClient(websession, accesskey, base_url=base_url)
    hass.data[DOMAIN]["divera_client"] = divera_client

    # Determine update interval from options (fallback to default)
    try:
        scan_interval = int(entry.options.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL))
    except Exception:
        scan_interval = DEFAULT_SCAN_INTERVAL

    for ucr_id in ucr_ids:
        divera_coordinator = DiveraCoordinator(
            hass, websession, accesskey, base_url=base_url, ucr_id=ucr_id, update_interval=scan_interval
        )
        coordinators[ucr_id] = divera_coordinator
        tasks.append(divera_coordinator.async_config_entry_first_refresh())

    # Run initial refreshes with error collection
    results = await asyncio.gather(*tasks, return_exceptions=True)
    errors: list[Exception] = [r for r in results if isinstance(r, Exception)]
    if errors:
        for err in errors:
            LOGGER.error("Initial data refresh failed for Divera: %s", err)
        # If any coordinator failed we abort setup to prevent partial broken state
        return False

    entry.runtime_data = DiveraRuntimeData(coordinators)

    LOGGER.debug(
        "Divera setup completed for %d coordinator(s) (entry_id=%s)",
        len(coordinators),
        entry.entry_id,
    )
    entry.async_on_unload(entry.add_update_listener(async_update_listener))

    # Register the service to trigger a test probe alarm
    async def trigger_probe_alarm_service(call):
        """
        Service to trigger a test probe alarm.

        :param call: Service call
        """
        LOGGER.info("🔔 trigger_probe_alarm_service is being called")
        divera_client = hass.data[DOMAIN].get("divera_client")
        if divera_client is None:
            LOGGER.error(
                "❌ No DiveraClient instance available for triggering probe alarm."
            )
            return
        await divera_client.trigger_probe_alarm()

    LOGGER.info("🔔 Registering service divera247.trigger_probe_alarm")
    hass.services.async_register(
        DOMAIN, "trigger_probe_alarm", trigger_probe_alarm_service
    )

    # Service: set user state by name
    async def set_user_state_service(call):
        state_name: str | None = call.data.get("state_name")
        divera_client = hass.data[DOMAIN].get("divera_client")
        if divera_client is None or state_name is None:
            LOGGER.error("❌ set_user_state: client or state_name missing")
            return
        # Validate available states (case-insensitive)
        try:
            valid = divera_client.get_all_state_name()
        except Exception:
            LOGGER.error("❌ set_user_state: cannot fetch state list")
            return
        match_name = next((s for s in valid if s.lower() == state_name.lower()), None)
        if match_name is None:
            LOGGER.error("❌ set_user_state: unknown state '%s' (valid: %s)", state_name, valid)
            return
        try:
            await divera_client.set_user_state_by_name(match_name)
            LOGGER.info("✅ User state changed to '%s'", match_name)
        except Exception as exc:  # DiveraError handled inside client
            LOGGER.error("❌ Failed changing user state to '%s': %s", match_name, exc)

    LOGGER.info("🔔 Registering service divera247.set_user_state")
    hass.services.async_register(
        DOMAIN, "set_user_state", set_user_state_service
    )

    # Forward platform setups (must be awaited to avoid frame warning in HA >=2025.1)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    LOGGER.debug("Forwarded setups for platforms: %s", PLATFORMS)
    return True


async def async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """
    Asynchronous update listener.

    :param hass: Home Assistant instance
    :param entry: Config entry for Divera
    """
    await hass.config_entries.async_reload(entry_id=entry.entry_id)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """
    Unload Divera config entry.

    :param hass: Home Assistant instance
    :param entry: Config entry for Divera
    :return: True if unload was successful
    """
    results = await asyncio.gather(
        *[
            hass.config_entries.async_forward_entry_unload(entry, component)
            for component in PLATFORMS
        ]
    )
    unload_ok = all(results)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
        if not hass.data[DOMAIN]:
            hass.data.pop(DOMAIN)
    return unload_ok


async def async_migrate_entry(hass, config_entry: ConfigEntry):
    """
    Migrate old entry.

    :param hass: Home Assistant instance
    :param config_entry: Config entry for Divera
    :return: True if migration was successful
    """
    LOGGER.debug("🔄 Migrating from version %s", config_entry.version)
    if (
        config_entry.version > CONF_FLOW_VERSION
        or config_entry.minor_version > CONF_FLOW_MINOR_VERSION
    ):
        LOGGER.debug(
            "❌ Migration to version %s.%s failed. Downgraded ",
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
                "❌ Migration to version %s.%s failed.",
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
        "✅ Migration to version %s.%s successful",
        config_entry.version,
        config_entry.minor_version,
    )
    return True
