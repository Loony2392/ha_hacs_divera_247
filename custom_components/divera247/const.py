"""Constants for Divera 24/7 integration."""

import logging

LOGGER = logging.getLogger(__package__)
"""Logger for the Divera 24/7 integration."""

DOMAIN: str = "divera247"
"""Domain for the Divera 24/7 integration."""

INTEGRATION_FULL_NAME: str = "DIVERA 24/7"
"""Full name of the integration."""

INTEGRATION_SHORT_NAME: str = "DIVERA"
"""Short name of the integration."""

DIVERA_GMBH: str = "DIVERA GmbH"
"""Name of the company providing the service."""

ATTR_NAME: str = "state"
"""Attribute name for the state."""

ATTR_LATEST_UPDATE: str = "latest_update_utc"
"""Attribute name for the latest update timestamp."""

DIVERA_DATA: str = "divera_data"
"""Key for storing Divera data."""

USER_NAME: str = "user_name"
"""Key for storing the user name."""

DIVERA_BASE_URL: str = "https://app.divera247.com"
"""Base URL for the Divera 24/7 API."""

DIVERA_API_PULL_PATH: str = "/api/v2/pull/all"
"""API path for pulling data."""

DIVERA_API_STATUS_PATH: str = "/api/v2/statusgeber/set-status"
"""API path for setting status."""

DEFAULT_SCAN_INTERVAL: int = 60
"""Default scan interval in seconds."""

DATA_ACCESSKEY: str = "accesskey"
"""Key for storing the access key."""

DATA_UCRS: str = "ucrs"
"""Key for storing UCRs."""

DATA_SCAN_INTERVAL: str = "scan_interval"
"""Key for storing the scan interval."""

DATA_BASE_URL: str = "base_url"
"""Key for storing the base URL."""

CONF_CLUSTERS: str = "clusters"
"""Configuration key for clusters."""

CONF_ACCESSKEY: str = "accesskey"
"""Configuration key for the access key."""

CONF_SCAN_INTERVAL: str = "scan_interval"
"""Configuration key for the scan interval."""

CONF_VEHICLE_NAME_MODE: str = "vehicle_name_mode"
"""Configuration key for vehicle name display mode."""

VEHICLE_NAME_MODE_AUTO: str = "auto"
VEHICLE_NAME_MODE_SHORT: str = "shortname"
VEHICLE_NAME_MODE_NAME: str = "name"
VEHICLE_NAME_MODE_FULL: str = "fullname"

VEHICLE_NAME_MODES: list[str] = [
	VEHICLE_NAME_MODE_AUTO,
	VEHICLE_NAME_MODE_SHORT,
	VEHICLE_NAME_MODE_NAME,
	VEHICLE_NAME_MODE_FULL,
]

CONF_BASE_URL: str = "base_url"
"""Configuration key for the base URL."""

PARAM_ACCESSKEY: str = "accesskey"
"""Parameter key for the access key."""

PARAM_UCR: str = "ucr"
"""Parameter key for UCR."""

PARAM_NEWS: str = "ts_news"
"""Parameter key for news timestamp."""

PARAM_EVENT: str = "ts_event"
"""Parameter key for event timestamp."""

PARAM_STATUSPLAN: str = "ts_statusplan"
"""Parameter key for status plan timestamp."""

PARAM_LOCALMONITOR: str = "ts_localmonitor"
"""Parameter key for local monitor timestamp."""

PARAM_MONITOR: str = "ts_monitor"
"""Parameter key for monitor timestamp."""

VERSION_FREE: str = "Free"
"""Version name for the free version."""

VERSION_ALARM: str = "Alarm"
"""Version name for the alarm version."""

VERSION_PRO: str = "Pro"
"""Version name for the pro version."""

VERSION_UNKNOWN: str = "Unknown"
"""Version name for an unknown version."""

CONF_FLOW_VERSION: int = 3
"""Configuration flow version."""

CONF_FLOW_MINOR_VERSION: int = 1
"""Configuration flow minor version."""

CONF_FLOW_NAME_UCR: str = "user_cluster_relation"
"""Configuration flow name for user cluster relation."""

CONF_FLOW_NAME_API: str = "api"
"""Configuration flow name for API."""

CONF_FLOW_NAME_RECONFIGURE: str = "reconfigure_confirm"
"""Configuration flow name for reconfiguration confirmation."""

CONF_FLOW_NAME_SCAN_INTERVAL: str = "scan_interval"
"""Configuration flow name for scan interval."""

ERROR_AUTH = "authentication"
"""Error code for authentication errors."""

ERROR_CONNECTION = "cannot_connect"
"""Error code for connection errors."""
