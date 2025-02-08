"""Select Module for Divera 24/7 Integration."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime

from homeassistant.components.calendar import (
    CalendarEntity,
    CalendarEntityDescription,
    CalendarEvent,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType

from . import DiveraConfigEntry, DiveraCoordinator
from .divera import DiveraClient
from .entity import DiveraEntity, DiveraEntityDescription


@dataclass(frozen=True, kw_only=True)
class DiveraCalendarEntityDescription(
    DiveraEntityDescription, CalendarEntityDescription
):
    """Description of a Divera calendar entity.

    Attributes:
        event_fn (Callable[[DiveraClient], StateType]): A function that retrieves the event
            from the Divera client.

    """

    event_fn: Callable[[DiveraClient], StateType]


CALENDARS: tuple[DiveraCalendarEntityDescription, ...] = (
    DiveraCalendarEntityDescription(
        key="events",
        translation_key="events",
        icon="mdi:calendar-text",
        event_fn=lambda divera: divera.get_last_event(),
        attribute_fn=lambda divera: divera.get_last_event_attributes(),
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: DiveraConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Divera select entities.

    Args:
        hass (HomeAssistant): Home Assistant instance.
        entry (ConfigEntry): Configuration entry for the integration.
        async_add_entities (AddEntitiesCallback): Function to add entities.

    """
    coordinators = entry.runtime_data.coordinators
    entities: list[DiveraCalendarEntity] = [
        DiveraCalendarEntity(coordinators[ucr_id], description)
        for ucr_id in coordinators
        for description in CALENDARS
    ]
    async_add_entities(entities, False)


class DiveraCalendarEntity(DiveraEntity, CalendarEntity):
    """Representation of a Divera calendar entity.

    This class manages the calendar events retrieved from the Divera service.

    Attributes:
        entity_description (DiveraCalendarEntityDescription): The description of the entity.
        _event (CalendarEvent | None): The current event associated with this entity.

    """

    entity_description: DiveraCalendarEntityDescription

    def __init__(
        self,
        coordinator: DiveraCoordinator,
        description: DiveraCalendarEntityDescription,
    ) -> None:
        """Initialize the Divera calendar entity.

        Args:
            coordinator (DiveraCoordinator): The coordinator for managing data from Divera.
            description (DiveraCalendarEntityDescription): The description of the calendar entity.

        """
        super().__init__(coordinator, description)
        self._event: CalendarEvent | None = None

    def _divera_update(self) -> None:
        self._event = self.entity_description.event_fn(self.coordinator.data)

    @property
    def event(self) -> CalendarEvent | None:
        """Return the next upcoming event.

        Returns:
            CalendarEvent | None: The next upcoming event, or None if there are no events.

        """
        return self._event

    async def async_get_events(
        self, hass: HomeAssistant, start_date: datetime, end_date: datetime
    ) -> list[CalendarEvent]:
        """Get all events in a specific time frame.

        Args:
            hass (HomeAssistant): Home Assistant instance.
            start_date (datetime): The start date for the event retrieval.
            end_date (datetime): The end date for the event retrieval.

        Returns:
            list[CalendarEvent]: A list of calendar events within the specified time frame.

        """
        return self.coordinator.data.get_events(start_date, end_date)
