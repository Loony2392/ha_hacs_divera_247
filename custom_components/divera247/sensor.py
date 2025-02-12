"""Sensor Module for Divera 24/7 Integration."""

from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import DiveraConfigEntry
from .coordinator import DiveraCoordinator
from .divera247 import DiveraClient
from .entity import DiveraEntity, DiveraEntityDescription

# -------------------------------------------------------------------
# Beschreibung für Helfer-Infos (ohne E-Mail)
# -------------------------------------------------------------------


@dataclass(frozen=True, kw_only=True)
class DiveraHelperEntityDescription(DiveraEntityDescription, SensorEntityDescription):
    """Description of a Divera helper sensor entity.

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
        value_fn=lambda divera, helper: f"{helper.get('firstname', '')} {helper.get('lastname', '')}",
    ),
    DiveraHelperEntityDescription(
        key="helper_status",
        translation_key="helper_status",
        icon="mdi:account-check",
        value_fn=lambda divera, helper: helper.get("status", "unknown"),
    ),
)


class DiveraHelperSensorEntity(DiveraEntity, SensorEntity):
    """Sensor representing an individual helper with personal info."""

    entity_description: DiveraHelperEntityDescription

    def __init__(
        self,
        coordinator: DiveraCoordinator,
        helper: dict,
        description: DiveraHelperEntityDescription,
    ) -> None:
        """Initialize a helper sensor entity.

        Args:
            coordinator (DiveraCoordinator): The coordinator for the integration.
            helper (dict): A dictionary with the helper's data.
            description (DiveraHelperEntityDescription): Description of the sensor.
        """
        super().__init__(coordinator, description)
        self._helper = helper

    def _divera_update(self) -> None:
        self._attr_native_value = self.entity_description.value_fn(
            self.coordinator.data, self._helper
        )
        # Optional: Setze weitere Attribute aus dem Helfer-Dict
        self._attr_extra_state_attributes = self._helper


# -------------------------------------------------------------------
# Sensor für die Anzahl der Helfer pro Status
# -------------------------------------------------------------------


@dataclass(frozen=True, kw_only=True)
class DiveraStatusCountEntityDescription(
    DiveraEntityDescription, SensorEntityDescription
):
    """Description of a status count sensor.

    Attributes:
        status (str): The status to count.
    """

    status: str


STATUS_SENSORS: tuple[DiveraStatusCountEntityDescription, ...] = (
    DiveraStatusCountEntityDescription(
        key="status_active",
        translation_key="status_active",
        icon="mdi:check-circle",
        status="active",
    ),
    DiveraStatusCountEntityDescription(
        key="status_inactive",
        translation_key="status_inactive",
        icon="mdi:close-circle",
        status="inactive",
    ),
    DiveraStatusCountEntityDescription(
        key="status_on_duty",
        translation_key="status_on_duty",
        icon="mdi:briefcase",
        status="on_duty",
    ),
)


class DiveraStatusCountSensorEntity(DiveraEntity, SensorEntity):
    """Sensor that counts helpers by a given status."""

    entity_description: DiveraStatusCountEntityDescription

    def __init__(
        self,
        coordinator: DiveraCoordinator,
        description: DiveraStatusCountEntityDescription,
    ) -> None:
        """Initialize a status count sensor.

        Args:
            coordinator (DiveraCoordinator): The coordinator for the integration.
            description (DiveraStatusCountEntityDescription): Description of the sensor.
        """
        super().__init__(coordinator, description)
        self._status = description.status

    def _divera_update(self) -> None:
        # Angenommen, die Liste der Helfer steht unter dem Schlüssel "helpers" im Daten-Dict
        helpers = self.coordinator.data.get("helpers", [])
        count = sum(1 for helper in helpers if helper.get("status") == self._status)
        self._attr_native_value = count


# -------------------------------------------------------------------
# async_setup_entry für Sensoren
# -------------------------------------------------------------------


async def async_setup_entry(
    hass: HomeAssistant,
    entry: DiveraConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Divera sensor entities."""
    coordinators = entry.runtime_data.coordinators
    entities: list[SensorEntity] = []

    # Erstelle für jeden Helfer individuelle Sensoren (Name und Status)
    for ucr_id in coordinators:
        coordinator = coordinators[ucr_id]
        helpers = coordinator.data.get(
            "helpers", []
        )  # Erwartet, dass die Helferdaten hier liegen
        for helper in helpers:
            for description in HELPER_SENSORS:
                entities.append(
                    DiveraHelperSensorEntity(coordinator, helper, description)
                )

    # Erstelle Sensoren, die den Status aggregieren (z.B. Anzahl aktiver Helfer)
    for ucr_id in coordinators:
        coordinator = coordinators[ucr_id]
        for description in STATUS_SENSORS:
            entities.append(DiveraStatusCountSensorEntity(coordinator, description))

    async_add_entities(entities, False)
