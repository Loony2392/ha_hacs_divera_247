"""Button Module for Divera 24/7 Integration."""

from homeassistant.components.button import ButtonEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import DiveraConfigEntry, DiveraCoordinator
from .const import DOMAIN
from .entity import DiveraEntity


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
        """
        Initialize the button.

        Args:
            coordinator (DiveraCoordinator): The coordinator managing this entity.
        """
        super().__init__(coordinator)
        self._attr_name = "Trigger Test Alarm"
        self._attr_unique_id = f"{DOMAIN}_trigger_test_alarm"

    async def async_press(self) -> None:
        """
        Handle the button press.

        This method is called when the button is pressed. It triggers a test alarm.
        """
        await self.coordinator.data.trigger_probe_alarm()
