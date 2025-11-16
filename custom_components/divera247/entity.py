"""Entity Module for Divera 24/7 Integration."""

from __future__ import annotations

from collections.abc import Callable, MutableMapping
from dataclasses import dataclass
from typing import Any

from homeassistant.core import callback
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DIVERA_BASE_URL, DIVERA_GMBH, DOMAIN
from .coordinator import DiveraCoordinator
from .divera247 import DiveraClient


@dataclass(frozen=True, kw_only=True)
class DiveraEntityDescription(EntityDescription):
    """
    Description of a Divera entity.

    Attributes:
        attribute_fn (Callable[[DiveraClient], MutableMapping[str, Any]]):
            Function that returns a mapping of attributes for the entity,
            based on a DiveraClient instance.
    """

    attribute_fn: Callable[[DiveraClient], MutableMapping[str, Any]]


class DiveraEntity(CoordinatorEntity[DiveraCoordinator]):
    """
    Represents a Divera entity.

    Attributes:
        entity_description (DiveraEntityDescription):
            Description of the entity.
    """

    _attr_has_entity_name = True
    entity_description: DiveraEntityDescription

    def __init__(
        self, coordinator: DiveraCoordinator, description: DiveraEntityDescription
    ) -> None:
        """
        Initialize DiveraEntity.

        Args:
            coordinator (DiveraCoordinator): The coordinator managing this entity.
            description (DiveraEntityDescription): Description of the entity.
        """
        super().__init__(coordinator)
        self.entity_description = description

        client = self.coordinator.data
        if client is not None:
            try:
                self._ucr_id = client.get_active_ucr()
            except Exception:
                self._ucr_id = client.get_ucr_id()
            try:
                self._cluster_name = client.get_cluster_name_from_ucr(self._ucr_id)
            except Exception:
                self._cluster_name = "unknown"
        else:
            # Data not loaded yet; use configured ucr id if possible
            self._ucr_id = self.coordinator.divera_client.get_ucr_id()
            self._cluster_name = "unknown"

        self._attr_unique_id = "_".join(
            [
                DOMAIN,
                str(self._ucr_id),
                description.key,
            ]
        )

        self._divera_update()

    @callback
    def _handle_coordinator_update(self) -> None:
        """
        Handle updates from the coordinator.

        This method is called when the coordinator has new data.
        """
        self._divera_update()
        self.async_write_ha_state()

    def _divera_update(self) -> None:
        """
        Update the state of the entity.

        This method should be implemented by subclasses to update the state of the entity.
        """
        raise NotImplementedError

    @property
    def device_info(self) -> DeviceInfo:
        """
        Device information property.

        Returns:
            DeviceInfo: Device information object.
        """
        from . import __version__
        
        config_url = DIVERA_BASE_URL
        client = self.coordinator.data
        cluster_version = client.get_cluster_version() if client else "unknown"
        return DeviceInfo(
            identifiers={
                (
                    DOMAIN,
                    str(self._ucr_id),
                )
            },
            manufacturer=DIVERA_GMBH,
            name=self._cluster_name,
            model=f"Divera {cluster_version}",
            sw_version=__version__,
            configuration_url=config_url,
        )
