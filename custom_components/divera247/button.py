"""Button Module for Divera 24/7 Integration."""

from homeassistant.components.button import ButtonEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import DiveraConfigEntry, DiveraCoordinator
from .const import DOMAIN
from dataclasses import dataclass
from typing import MutableMapping, Any

from .entity import DiveraEntity, DiveraEntityDescription
from .divera247 import DiveraClient


@dataclass(frozen=True, kw_only=True)
class DiveraButtonEntityDescription(DiveraEntityDescription):
    """Description for Divera test alarm button."""
    # No extra fields needed; button has no native value


TEST_ALARM_BUTTON_DESCRIPTION = DiveraButtonEntityDescription(
    key="trigger_test_alarm_button",
    translation_key="trigger_test_alarm_button",
    icon="mdi:bell-ring-outline",
    attribute_fn=lambda divera: {},
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: DiveraConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """
    Set up Divera button entities.

    Args:
        hass (HomeAssistant): Home Assistant instance.
        entry (DiveraConfigEntry): Configuration entry for the integration.
        async_add_entities (AddEntitiesCallback): Function to add entities.
    """
    coordinators = entry.runtime_data.coordinators
    entities = [
        DiveraTestAlarmButton(coordinator) for coordinator in coordinators.values()
    ]
    async_add_entities(entities, False)


class DiveraTestAlarmButton(DiveraEntity, ButtonEntity):
    """
    Representation of a Divera Test Alarm Button.

    Attributes:
        _attr_name (str): The name of the button.
        _attr_unique_id (str): The unique ID of the button.
    """

    def __init__(self, coordinator: DiveraCoordinator) -> None:
        super().__init__(coordinator, TEST_ALARM_BUTTON_DESCRIPTION)
        self._attr_name = "Trigger Test Alarm"
        # Unique id already includes DOMAIN, ucr, description.key from base; keep explicit for clarity
        self._attr_unique_id = f"{DOMAIN}_{self._ucr_id}_trigger_test_alarm"

    def _divera_update(self) -> None:  # noqa: D401
        # Button has no meaningful state; ensure no exception
        self._attr_extra_state_attributes = {}

    async def async_press(self) -> None:
        """
        Handle the button press.

        This method is called when the button is pressed. It triggers a test alarm.
        """
        client = self.coordinator.data
        if client is not None:
            await client.trigger_probe_alarm()
