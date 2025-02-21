"""Binary Sensor Module for Divera 24/7 Integration."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from homeassistant.components.binary_sensor import (
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType

from . import DiveraConfigEntry
from .coordinator import DiveraCoordinator
from .divera247 import DiveraClient
from .entity import DiveraEntity, DiveraEntityDescription


@dataclass(frozen=True, kw_only=True)
class DiveraBinarySensorEntityDescription(
    DiveraEntityDescription, BinarySensorEntityDescription
):
    """
    Description of a Divera binary sensor entity.

    Inherits from both DiveraEntityDescription and BinarySensorEntityDescription.

    Attributes:
        value_fn (Callable[[DiveraClient], StateType]):
            Function that returns the value of the sensor.
    """

    value_fn: Callable[[DiveraClient], StateType]


BINARY_SENSORS: tuple[DiveraBinarySensorEntityDescription, ...] = (
    DiveraBinarySensorEntityDescription(
        key="active_alarm",
        translation_key="active_alarm",
        icon="mdi:alarm-light",
        value_fn=lambda divera: divera.has_open_alarms(),
        attribute_fn=lambda divera: divera.get_last_alarm_attributes(),
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: DiveraConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """
    Set up Divera binary sensor entities.

    Args:
        hass (HomeAssistant): Home Assistant instance.
        entry (DiveraConfigEntry): Configuration entry for the integration.
        async_add_entities (AddEntitiesCallback): Function to add entities.
    """
    coordinators = entry.runtime_data.coordinators
    entities: list[DiveraBinarySensorEntity] = [
        DiveraBinarySensorEntity(coordinators[ucr_id], description)
        for ucr_id in coordinators
        for description in BINARY_SENSORS
    ]
    async_add_entities(entities, False)


class DiveraBinarySensorEntity(DiveraEntity, BinarySensorEntity):
    """
    Represents a Divera binary sensor entity.

    Inherits from both DiveraEntity and BinarySensorEntity.

    Attributes:
        entity_description (DiveraBinarySensorEntityDescription):
            Description of the binary sensor entity.
    """

    entity_description: DiveraBinarySensorEntityDescription

    def __init__(
        self,
        coordinator: DiveraCoordinator,
        description: DiveraBinarySensorEntityDescription,
    ) -> None:
        """
        Initialize DiveraBinarySensorEntity.

        Args:
            coordinator (DiveraCoordinator): The coordinator managing this entity.
            description (DiveraBinarySensorEntityDescription): Description of the binary sensor entity.
        """
        super().__init__(coordinator, description)

    def _divera_update(self) -> None:
        """
        Update the state of the binary sensor.

        This method is called to update the state of the binary sensor based on the latest data from the coordinator.
        """
        self._attr_is_on = self.entity_description.value_fn(self.coordinator.data)
        self._attr_extra_state_attributes = self.entity_description.attribute_fn(
            self.coordinator.data
        )
