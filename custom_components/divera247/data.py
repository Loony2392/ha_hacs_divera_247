"""module contains the data structures used in the Divera 24/7 custom component."""

from dataclasses import dataclass

from custom_components.divera import DiveraCoordinator


@dataclass
class DiveraRuntimeData:
    """Represents the runtime data for the Divera component.

    Attributes:
        coordinators (dict[str, DiveraCoordinator]): A dictionary mapping
        coordinator IDs to their respective DiveraCoordinator instances.

    """

    coordinators: dict[str, DiveraCoordinator]
