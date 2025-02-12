"""Divera 24/7 Component."""

import asyncio
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_API_KEY, CONF_NAME, Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession


from .const import (
    CONF_FLOW_MINOR_VERSION,
    CONF_FLOW_VERSION,
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

    # Create a DiveraClient instance and store it for the service
    divera_client = DiveraClient(websession, accesskey, base_url=base_url)
    hass.data[DOMAIN]["divera_client"] = divera_client

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

    # Register the service to trigger a test probe alarm
    async def trigger_probe_alarm_service(call):
        # Service to trigger a test probe alarm
        LOGGER.info("🔔 trigger_probe_alarm_service is being called")
        divera_client = hass.data[DOMAIN].get("divera_client")
        if divera_client is None:
            LOGGER.error("❌ No DiveraClient instance available for triggering probe alarm.")
            return
        await divera_client.trigger_probe_alarm()

    LOGGER.info("🔔 Registering service divera247.trigger_probe_alarm")
    hass.services.async_register(
        DOMAIN,
        "trigger_probe_alarm",
        trigger_probe_alarm_service
    )

    # Forward the config entry setups for all platforms (select, sensor, calendar, binary_sensor)
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