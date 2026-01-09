"""Sensor Module for Divera 24/7 Integration."""

from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
import html

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import EntityCategory

from . import DiveraConfigEntry
from .coordinator import DiveraCoordinator
from .divera247 import DiveraClient
from .const import (
    CONF_VEHICLE_NAME_MODE,
    VEHICLE_NAME_MODE_AUTO,
    VEHICLE_NAME_MODE_SHORT,
    VEHICLE_NAME_MODE_NAME,
    VEHICLE_NAME_MODE_FULL,
    DOMAIN,
    DIVERA_BASE_URL,
    DIVERA_GMBH,
)
from .entity import DiveraEntity, DiveraEntityDescription


def _safe_string(value: Any) -> str:
    """Safely sanitize string values to prevent XSS.
    
    Args:
        value: Value to sanitize
        
    Returns:
        Sanitized string with HTML entities escaped
    """
    if not isinstance(value, str):
        value = str(value) if value else ""
    # HTML escape to prevent XSS attacks
    value = html.escape(value)
    # Max 500 chars to prevent overflow
    return value.strip()[:500]


@dataclass(frozen=True, kw_only=True)
class DiveraHelperEntityDescription(DiveraEntityDescription, SensorEntityDescription):
    """
    Description of a Divera helper sensor entity.

    Attributes:
        value_fn (Callable[[DiveraClient, dict], Any]):
            Function that returns the value of the sensor based on a helper dict.
    """

    value_fn: Callable[[DiveraClient, dict], Any]


HELPER_SENSORS: tuple[DiveraHelperEntityDescription, ...] = (
    DiveraHelperEntityDescription(
        key="helper_name",
        translation_key="helper_name",
        icon="mdi:account",
        attribute_fn=lambda divera: {},
        value_fn=lambda divera, helper: f"{_safe_string(helper.get('firstname', ''))} {_safe_string(helper.get('lastname', ''))}".strip(),
    ),
    DiveraHelperEntityDescription(
        key="helper_status",
        translation_key="helper_status",
        icon="mdi:account-check",
        attribute_fn=lambda divera: {},
        value_fn=lambda divera, helper: _safe_string(helper.get("status", "unknown")),
    ),
)

@dataclass(frozen=True, kw_only=True)
class DiveraVehicleEntityDescription(DiveraEntityDescription, SensorEntityDescription):
    """Description of a Divera vehicle sensor entity.

    Attributes:
        value_fn (Callable[[DiveraClient, str], Any]):
            Function returning the sensor value for a vehicle id.
    """

    value_fn: Callable[[DiveraClient, str], Any]
    name_mode: str | None = None


class DiveraVehicleSensorEntity(DiveraEntity, SensorEntity):
    """Sensor representing a single vehicle state."""

    entity_description: DiveraVehicleEntityDescription

    def __init__(
        self,
        coordinator: DiveraCoordinator,
        vehicle_id: str,
        description: DiveraVehicleEntityDescription,
    ) -> None:
        # Set vehicle id before calling base __init__ (base triggers _divera_update)
        self._vehicle_id = vehicle_id
        self._name_mode = description.name_mode or VEHICLE_NAME_MODE_AUTO
        # Store a separate display name for the device, not the entity name
        self._vehicle_display_name: str | None = None
        # Pre-compute display name if data is already available to avoid 'Vehicle <id>' fallback
        try:
            self._vehicle_display_name = self._compute_display_name(coordinator.data)
        except Exception:
            self._vehicle_display_name = None
        super().__init__(coordinator, description)
        # Show entity as "<Device Name>: <Translated Label>" in UI
        self._attr_has_entity_name = True
        self._update_vehicle_display_name()
        # Mark location sensor as diagnostic and disabled by default to avoid duplication
        if description.translation_key == "vehicle_location":
            self._attr_entity_category = EntityCategory.DIAGNOSTIC
            self._attr_entity_registry_enabled_default = False

    def _compute_display_name(self, client: DiveraClient | None) -> str | None:
        mode = self._name_mode
        name: str | None = None
        if client is not None:
            try:
                attrs = client.get_vehicle_attributes(self._vehicle_id)
                if mode == VEHICLE_NAME_MODE_SHORT:
                    name = attrs.get("shortname")
                elif mode == VEHICLE_NAME_MODE_NAME:
                    name = attrs.get("name")
                elif mode == VEHICLE_NAME_MODE_FULL:
                    name = attrs.get("fullname")
                else:  # auto
                    name = attrs.get("shortname") or attrs.get("name") or attrs.get("fullname")
            except Exception:
                name = None
        return name

    def _update_vehicle_display_name(self):
        client = self.coordinator.data
        name = self._compute_display_name(client)
        # Save for device_info usage; fall back to id string if computation failed
        self._vehicle_display_name = name or self._vehicle_id

    def _divera_update(self) -> None:  # noqa: D401
        client = self.coordinator.data
        if client is None:
            self._attr_native_value = None
            self._attr_extra_state_attributes = {}
            return
        # Update the cached device display name (entity name remains translated label)
        self._update_vehicle_display_name()
        self._attr_native_value = self.entity_description.value_fn(
            client, self._vehicle_id
        )
        try:
            # For location entities, keep attributes minimal (latitude/longitude) to
            # ensure map compatibility; otherwise expose full vehicle attributes.
            if self.entity_description.translation_key == "vehicle_location":
                self._attr_extra_state_attributes = self.entity_description.attribute_fn(  # type: ignore[attr-defined]
                    client
                )
            else:
                self._attr_extra_state_attributes = client.get_vehicle_attributes(
                    self._vehicle_id
                )
        except Exception:
            self._attr_extra_state_attributes = {}

    @property
    def device_info(self) -> DeviceInfo:  # type: ignore[override]
        # Ensure we have a display name; compute from current data if missing
        if not self._vehicle_display_name or self._vehicle_display_name == self._vehicle_id:
            try:
                self._vehicle_display_name = self._compute_display_name(self.coordinator.data) or self._vehicle_id
            except Exception:
                self._vehicle_display_name = self._vehicle_id
        from . import __version__
        client = self.coordinator.data
        cluster_version = client.get_cluster_version() if client else "unknown"
        return DeviceInfo(
            identifiers={(DOMAIN, f"{self._ucr_id}_vehicle_{self._vehicle_id}")},
            manufacturer=DIVERA_GMBH,
            name=self._vehicle_display_name,
            model=f"Divera Vehicle {cluster_version}",
            sw_version=__version__,
            configuration_url=DIVERA_BASE_URL,
            via_device=(DOMAIN, str(self._ucr_id)),
        )


class DiveraHelperSensorEntity(DiveraEntity, SensorEntity):
    """
    Sensor representing an individual helper with personal info.

    Attributes:
        entity_description (DiveraHelperEntityDescription): Description of the sensor.
        _helper (dict): A dictionary with the helper's data.
    """

    entity_description: DiveraHelperEntityDescription

    def __init__(
        self,
        coordinator: DiveraCoordinator,
        helper: dict,
        description: DiveraHelperEntityDescription,
    ) -> None:
        """
        Initialize a helper sensor entity.

        Args:
            coordinator (DiveraCoordinator): The coordinator for the integration.
            helper (dict): A dictionary with the helper's data.
            description (DiveraHelperEntityDescription): Description of the sensor.
        """
        super().__init__(coordinator, description)
        self._helper = helper

    def _divera_update(self) -> None:
        """
        Update the state of the entity.

        This method is called to update the state of the entity based on the latest data from the coordinator.
        """
        self._attr_native_value = self.entity_description.value_fn(
            self.coordinator.data, self._helper
        )
        # Include unit/cluster information for easier UI filtering
        self._attr_extra_state_attributes = {
            **self._helper,
            "cluster_name": self._cluster_name,
            "ucr_id": self._ucr_id,
        }


@dataclass(frozen=True, kw_only=True)
class DiveraStatusCountEntityDescription(
    DiveraEntityDescription, SensorEntityDescription
):
    """
    Description of a status count sensor.

    Attributes:
        status (str): The status to count.
    """

    status: str


STATUS_SENSORS: tuple[DiveraStatusCountEntityDescription, ...] = (
    DiveraStatusCountEntityDescription(
        key="status_active",
        translation_key="status_active",
        icon="mdi:check-circle",
        attribute_fn=lambda divera: {},
        status="active",
    ),
    DiveraStatusCountEntityDescription(
        key="status_inactive",
        translation_key="status_inactive",
        icon="mdi:close-circle",
        attribute_fn=lambda divera: {},
        status="inactive",
    ),
    DiveraStatusCountEntityDescription(
        key="status_on_duty",
        translation_key="status_on_duty",
        icon="mdi:briefcase",
        attribute_fn=lambda divera: {},
        status="on_duty",
    ),
)


class DiveraStatusCountSensorEntity(DiveraEntity, SensorEntity):
    """
    Sensor that counts helpers by a given status.

    Attributes:
        entity_description (DiveraStatusCountEntityDescription): Description of the sensor.
        _status (str): The status to count.
    """

    entity_description: DiveraStatusCountEntityDescription

    def __init__(
        self,
        coordinator: DiveraCoordinator,
        description: DiveraStatusCountEntityDescription,
    ) -> None:
        """
        Initialize a status count sensor.

        Args:
            coordinator (DiveraCoordinator): The coordinator for the integration.
            description (DiveraStatusCountEntityDescription): Description of the sensor.
        """
        super().__init__(coordinator, description)
        self._status = description.status

    def _divera_update(self) -> None:
        """
        Update the state of the entity.

        This method is called to update the state of the entity based on the latest data from the coordinator.
        """
        client = self.coordinator.data
        helpers = client.get_helpers() if client else []
        count = sum(1 for helper in helpers if helper.get("status") == self._status)
        self._attr_native_value = count


@dataclass(frozen=True, kw_only=True)
class DiveraStatusOverviewEntityDescription(DiveraEntityDescription, SensorEntityDescription):
    """Description for aggregated status overview sensor."""

    value_fn: Callable[[DiveraClient], Any]


class DiveraStatusOverviewSensorEntity(DiveraEntity, SensorEntity):
    """Aggregated sensor with helper status counts as attributes."""

    entity_description: DiveraStatusOverviewEntityDescription

    def _divera_update(self) -> None:  # noqa: D401
        client = self.coordinator.data
        if client is None:
            self._attr_native_value = None
            self._attr_extra_state_attributes = {}
            return
        helpers = client.get_helpers()
        counts: dict[str, int] = {}
        for helper in helpers:
            status = helper.get("status", "unknown")
            counts[status] = counts.get(status, 0) + 1
        # Native value = total helpers; attributes per status
        self._attr_native_value = len(helpers)
        self._attr_extra_state_attributes = counts


@dataclass(frozen=True, kw_only=True)
class DiveraAlarmAddressEntityDescription(DiveraEntityDescription, SensorEntityDescription):
    """Description for last alarm address sensor."""

    value_fn: Callable[[DiveraClient], Any]


class DiveraAlarmAddressSensorEntity(DiveraEntity, SensorEntity):
    """Sensor exposing the address of the latest alarm."""

    entity_description: DiveraAlarmAddressEntityDescription

    def __init__(
        self,
        coordinator: DiveraCoordinator,
        description: DiveraAlarmAddressEntityDescription,
    ) -> None:
        super().__init__(coordinator, description)

    def _divera_update(self) -> None:  # noqa: D401
        client = self.coordinator.data
        if client is None:
            self._attr_native_value = None
            self._attr_extra_state_attributes = {}
            return
        try:
            self._attr_native_value = self.entity_description.value_fn(client)
            attrs = client.get_last_alarm_attributes()
            # Enrich with cluster/unit context
            self._attr_extra_state_attributes = {
                **attrs,
                "cluster_name": self._cluster_name,
                "ucr_id": self._ucr_id,
            }
        except Exception:
            self._attr_native_value = None
            self._attr_extra_state_attributes = {}


async def async_setup_entry(
    hass: HomeAssistant,
    entry: DiveraConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """
    Set up Divera sensor entities.

    Args:
        hass (HomeAssistant): Home Assistant instance.
        entry (DiveraConfigEntry): Configuration entry for the integration.
        async_add_entities (AddEntitiesCallback): Function to add entities.
    """
    coordinators = entry.runtime_data.coordinators
    entities: list[SensorEntity] = []

    # Create individual sensors for each helper (name and status)
    for ucr_id, coordinator in coordinators.items():
        client = coordinator.data
        if client is None:
            continue
        helpers = client.get_helpers()
        for helper in helpers:
            for description in HELPER_SENSORS:
                entities.append(
                    DiveraHelperSensorEntity(coordinator, helper, description)
                )

        # Vehicle sensors
        try:
            vehicle_ids = client.get_vehicle_id_list()
        except Exception:
            vehicle_ids = []
        # Determine name mode once per entry
        mode = entry.options.get(CONF_VEHICLE_NAME_MODE, VEHICLE_NAME_MODE_AUTO)
        for vid in vehicle_ids:
            # Main vehicle status sensor
            description = DiveraVehicleEntityDescription(
                key=f"vehicle_{vid}_state",
                translation_key="vehicle",  # uses sensor.vehicle translation
                icon="mdi:truck-outline",
                attribute_fn=(
                    lambda divera, _vid=vid: divera.get_vehicle_attributes(_vid)
                ),
                value_fn=(lambda divera, _vid=vid: divera.get_vehicle_state(_vid)),
                name_mode=mode,
            )
            entities.append(DiveraVehicleSensorEntity(coordinator, vid, description))
            
            # Additional attribute sensors for each vehicle
            # Location sensor removed to avoid duplicate with device_tracker
            
            # OPTA sensor
            opta_desc = DiveraVehicleEntityDescription(
                key=f"vehicle_{vid}_opta",
                translation_key="vehicle_opta",
                icon="mdi:radio-tower",
                attribute_fn=(lambda divera, _vid=vid: {}),
                value_fn=(lambda divera, _vid=vid: divera.get_vehicle_attributes(_vid).get("opta")),
                name_mode=mode,
            )
            entities.append(DiveraVehicleSensorEntity(coordinator, vid, opta_desc))
            
            # ISSI sensor
            issi_desc = DiveraVehicleEntityDescription(
                key=f"vehicle_{vid}_issi",
                translation_key="vehicle_issi",
                icon="mdi:identifier",
                attribute_fn=(lambda divera, _vid=vid: {}),
                value_fn=(lambda divera, _vid=vid: divera.get_vehicle_attributes(_vid).get("issi")),
                name_mode=mode,
            )
            entities.append(DiveraVehicleSensorEntity(coordinator, vid, issi_desc))
            
            # Vehicle number sensor
            number_desc = DiveraVehicleEntityDescription(
                key=f"vehicle_{vid}_number",
                translation_key="vehicle_number",
                icon="mdi:train-car-box",
                attribute_fn=(lambda divera, _vid=vid: {}),
                value_fn=(lambda divera, _vid=vid: divera.get_vehicle_attributes(_vid).get("number")),
                name_mode=mode,
            )
            entities.append(DiveraVehicleSensorEntity(coordinator, vid, number_desc))

    # Intentionally omit helper count sensors and overview per user request

    # Add last alarm address sensor per coordinator
    for ucr_id, coordinator in coordinators.items():
        description = DiveraAlarmAddressEntityDescription(
            key="last_alarm_address",
            translation_key="alarm_address",
            icon="mdi:map-marker",
            attribute_fn=lambda divera: divera.get_last_alarm_attributes(),
            value_fn=lambda divera: divera.get_last_alarm_attributes().get("address"),
        )
        entities.append(DiveraAlarmAddressSensorEntity(coordinator, description))

    async_add_entities(entities, False)
