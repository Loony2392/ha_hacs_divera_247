"""Device tracker platform for Divera 24/7 vehicles."""
from __future__ import annotations

from typing import Any

from homeassistant.components.device_tracker import SourceType, TrackerEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import DiveraConfigEntry
from .coordinator import DiveraCoordinator
from .divera247 import DiveraClient
from .entity import DiveraEntity, DiveraEntityDescription
from .const import (
    CONF_VEHICLE_NAME_MODE,
    VEHICLE_NAME_MODE_AUTO,
    VEHICLE_NAME_MODE_NAME,
    VEHICLE_NAME_MODE_SHORT,
    VEHICLE_NAME_MODE_FULL,
)


class DiveraVehicleTrackerEntity(DiveraEntity, TrackerEntity):
    """Device tracker entity for a single vehicle using GPS coordinates."""

    _attr_icon = "mdi:map-marker"

    def __init__(self, coordinator: DiveraCoordinator, vehicle_id: str, name_mode: str) -> None:
        self._vehicle_id = vehicle_id
        self._name_mode = name_mode or VEHICLE_NAME_MODE_AUTO
        super().__init__(
            coordinator,
            DiveraEntityDescription(
                key=f"vehicle_{vehicle_id}_tracker",
                attribute_fn=lambda client: {},
            ),
        )
        self._latitude: float | None = None
        self._longitude: float | None = None
        self._assign_name()

    # TrackerEntity properties
    @property
    def latitude(self) -> float | None:
        return self._latitude

    @property
    def longitude(self) -> float | None:
        return self._longitude

    @property
    def source_type(self) -> SourceType:
        return SourceType.GPS

    def _assign_name(self) -> None:
        client = self.coordinator.data
        mode = self._name_mode
        name: str = self._vehicle_id
        if client is not None:
            try:
                attrs = client.get_vehicle_attributes(self._vehicle_id)
                if mode == VEHICLE_NAME_MODE_SHORT:
                    name = attrs.get("shortname") or name
                elif mode == VEHICLE_NAME_MODE_NAME:
                    name = attrs.get("name") or name
                elif mode == VEHICLE_NAME_MODE_FULL:
                    name = attrs.get("fullname") or name
                else:  # auto
                    name = (
                        attrs.get("shortname")
                        or attrs.get("name")
                        or attrs.get("fullname")
                        or name
                    )
            except Exception:
                pass
        self._attr_name = name

    def _divera_update(self) -> None:
        client: DiveraClient | None = self.coordinator.data
        if client is None:
            self._latitude = None
            self._longitude = None
            return
        self._assign_name()
        try:
            attrs: dict[str, Any] = client.get_vehicle_attributes(self._vehicle_id)
            lat = attrs.get("latitude")
            lon = attrs.get("longitude")
            # Convert to float when possible
            self._latitude = float(lat) if lat is not None else None
            self._longitude = float(lon) if lon is not None else None
            # Expose minimal attributes on entity state for UI
            self._attr_extra_state_attributes = {
                "latitude": self._latitude,
                "longitude": self._longitude,
            }
        except Exception:
            self._latitude = None
            self._longitude = None
            self._attr_extra_state_attributes = {}


async def async_setup_entry(
    hass: HomeAssistant,
    entry: DiveraConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Divera vehicle trackers based on a config entry."""
    entities: list[DiveraVehicleTrackerEntity] = []
    coordinators = entry.runtime_data.coordinators

    name_mode = entry.options.get(CONF_VEHICLE_NAME_MODE, VEHICLE_NAME_MODE_AUTO)

    for _ucr, coordinator in coordinators.items():
        client: DiveraClient | None = coordinator.data
        if client is None:
            continue
        try:
            for vid in client.get_vehicle_id_list():
                entities.append(DiveraVehicleTrackerEntity(coordinator, vid, name_mode))
        except Exception:
            continue

    if entities:
        async_add_entities(entities, False)
