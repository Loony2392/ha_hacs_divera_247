"""Select Module for Divera 24/7 Integration."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType

from . import DiveraConfigEntry
from .coordinator import DiveraCoordinator
from .divera import DiveraClient
from .entity import DiveraEntity, DiveraEntityDescription


@dataclass(frozen=True, kw_only=True)
class DiveraSensorEntityDescription(DiveraEntityDescription, SensorEntityDescription):
    """Description of a Divera sensor entity.

    Inherits from both DiveraEntityDescription and SensorEntityDescription.

    Attributes:
        value_fn (Callable[[DiveraClient], StateType]):
            Function that returns the value of the sensor.

    """

    value_fn: Callable[[DiveraClient], StateType]


SENSORS: tuple[DiveraSensorEntityDescription, ...] = (
    DiveraSensorEntityDescription(
        key="alarm",
        translation_key="alarm",
        icon="mdi:message-alert",
        value_fn=lambda divera: divera.get_last_alarm(),
        attribute_fn=lambda divera: divera.get_last_alarm_attributes(),
    ),
    DiveraSensorEntityDescription(
        key="news",
        translation_key="news",
        icon="mdi:message-text",
        value_fn=lambda divera: divera.get_last_news(),
        attribute_fn=lambda divera: divera.get_last_news_attributes(),
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: DiveraConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Divera 24/7 sensor entities.

    Args:
        hass (HomeAssistant): Home Assistant instance.
        entry (ConfigEntry): Configuration entry for the integration.
        async_add_entities (AddEntitiesCallback): Function to add entities.

    """

    coordinators = entry.runtime_data.coordinators

    entities: list[DiveraSensorEntity] = [
        DiveraSensorEntity(coordinators[ucr_id], description)
        for ucr_id in coordinators
        for description in SENSORS
    ]

    for ucr_id in coordinators:
        divera_client = coordinators[ucr_id]
        vehicle_id_list = divera_client.data.get_vehicle_id_list()
        for vehicle_id in vehicle_id_list:
            vehicle_attributes = divera_client.data.get_vehicle_attributes(vehicle_id)
            vehicle_name = vehicle_attributes.get("name", f"Vehicle {vehicle_id}")

            vehicle_entity = DiveraSensorEntity(
                coordinators[ucr_id],
                DiveraSensorEntityDescription(
                    key=vehicle_id,
                    translation_key="vehicle",
                    translation_placeholders={
                        "vehicle_name": vehicle_name,
                    },
                    icon="mdi:fire-truck",
                    value_fn=lambda divera, vid=vehicle_id: divera.get_vehicle_state(vid),
                    attribute_fn=lambda divera,
                    vid=vehicle_id: divera.get_vehicle_attributes(vid),
                ),
            )
            entities.append(vehicle_entity)

    async_add_entities(entities, False)


class DiveraSensorEntity(DiveraEntity, SensorEntity):
    """Represents a Divera sensor entity.

    Inherits from both DiveraEntity and SensorEntity.

    Attributes:
        entity_description (DiveraSensorEntityDescription):
            Description of the sensor entity.

    """

    entity_description: DiveraSensorEntityDescription

    def __init__(
        self,
        coordinator: DiveraCoordinator,
        description: DiveraSensorEntityDescription,
    ) -> None:
        """Initialize DiveraSensorEntity.

        Args:
            coordinator (DiveraCoordinator): The coordinator managing this entity.
            description (DiveraSensorEntityDescription): Description of the sensor entity.

        """
        super().__init__(coordinator, description)

    def _divera_update(self) -> None:
        self._attr_native_value = self.entity_description.value_fn(
            self.coordinator.data
        )
        self._attr_extra_state_attributes = self.entity_description.attribute_fn(
            self.coordinator.data
        )
