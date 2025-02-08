"""Divera Http Client Module for Divera 24/7 Integration."""

from datetime import datetime
from http.client import UNAUTHORIZED

from aiohttp import ClientError, ClientResponseError, ClientSession

from homeassistant.components.calendar import CalendarEvent
from homeassistant.const import STATE_UNKNOWN
from homeassistant.util.dt import get_default_time_zone

from .const import (
    DIVERA_API_PULL_PATH,
    DIVERA_API_STATUS_PATH,
    DIVERA_BASE_URL,
    LOGGER,
    PARAM_ACCESSKEY,
    PARAM_LOCALMONITOR,
    PARAM_MONITOR,
    PARAM_STATUSPLAN,
    PARAM_UCR,
    VERSION_ALARM,
    VERSION_FREE,
    VERSION_PRO,
    VERSION_UNKNOWN,
)
from .utils import remove_params_from_url


class DiveraClient:
    """Represents a client for interacting with the Divera API."""

    def __init__(
        self, session: ClientSession, accesskey, base_url=DIVERA_BASE_URL, ucr_id=None
    ) -> None:
        """Initialize DiveraClient.

        Args:
            session (ClientSession): Client session for making HTTP requests.
            accesskey (str): Access key for accessing Divera data.
            base_url (str, optional): Base URL for Divera API. Defaults to DIVERA_BASE_URL.
            ucr_id (str, optional): Unique identifier for the organization. Defaults to None.

        """
        self.__session = session
        self.__data = None
        self.__accesskey = accesskey
        self.__base_url = base_url
        self.__ucr_id = ucr_id

    async def pull_data(self):
        """Pull data from the Divera API.

        Retrieves data from the Divera API and updates the internal data store.

        Raises:
            DiveraConnectionError: If an error occurs while connecting to the Divera API.
            DiveraAuthError: If authentication fails while connecting to the Divera API.

        """
        url = "".join([self.__base_url, DIVERA_API_PULL_PATH])
        time = int(datetime.now().timestamp())
        params = {
            PARAM_ACCESSKEY: self.__accesskey,
            PARAM_STATUSPLAN: time,
            PARAM_LOCALMONITOR: time,
            PARAM_MONITOR: time,
        }
        if self.__ucr_id is not None:
            params[PARAM_UCR] = self.__ucr_id
        try:
            async with self.__session.get(url=url, params=params) as response:
                response.raise_for_status()
                self.__data = await response.json()
        except ClientResponseError as exc:
            # TODO Exception Tests
            url = remove_params_from_url(exc.request_info.url)
            LOGGER.error(f"Error response {exc.status} while requesting {url!r}.")
            if exc.status == UNAUTHORIZED:
                raise DiveraAuthError from None
            raise DiveraConnectionError from None
        except ClientError as exc:
            url = remove_params_from_url(exc.request_info.url)
            LOGGER.error(f"An error occurred while requesting {url!r}.")
            raise DiveraConnectionError from None

    def get_base_url(self) -> str:
        """Get the base URL of the Divera API.

        Returns:
            str: The base URL.

        """
        return self.__base_url

    def get_full_name(self) -> str:
        """Retrieve the full name of the user associated with the data.

        Returns:
            str: The full name of the user, combining the first name and last name.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        firstname = self.__data["data"]["user"]["firstname"]
        lastname = self.__data["data"]["user"]["lastname"]
        return firstname + " " + lastname

    def get_user(self) -> dict:
        """Return information about the user.

        Returns:
            dict: A dictionary containing information about the user including first name, last name,
                  full name, and email.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        data = {}
        data["firstname"] = self.__data["data"]["user"]["firstname"]
        data["lastname"] = self.__data["data"]["user"]["lastname"]
        data["fullname"] = self.get_full_name()
        data["email"] = self.get_email()
        return data

    def get_state_id_by_name(self, name) -> str:
        """Return the state_id of the given state name.

        Args:
            name (str): The name of the state.

        Returns:
            int or None: The state_id corresponding to the given state name,
                         or None if the state name is not found.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        status = self.__data["data"]["cluster"]["status"]
        status_sorting = self.__data["data"]["cluster"]["statussorting"]

        for state_id in status_sorting:
            if status.get(str(state_id), {}).get("name") == name:
                return state_id
        raise ValueError(f"State name '{name}' not found.")

    def get_all_state_name(self) -> list:
        """Return the list of all available names of the states.

        Returns:
            list: A list containing all the names of the states.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        states = []
        for state_id in self.__data["data"]["cluster"]["statussorting"]:
            state_name = self.__data["data"]["cluster"]["status"][str(state_id)]["name"]
            states.append(state_name)
        return states

    def get_user_state(self) -> str:
        """Give the name of the current status of the user.

        Returns:
            str: The name of the current status of the user.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        status_id = self.__data["data"]["status"]["status_id"]
        return self.get_state_name_by_id(status_id)

    def get_state_name_by_id(self, status_id) -> str:
        """Return the name of the state of the user by given id.

        Args:
            status_id (int): The ID of the status.

        Returns:
            str: The name of the state corresponding to the given ID.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        return self.__data["data"]["cluster"]["status"][str(status_id)]["name"]

    def get_user_state_attributes(self) -> dict:
        """Return additional information of the user's state.

        Returns:
            dict: A dictionary containing additional information of the user's state,
                  including timestamp and ID.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        data = {}
        timestamp = self.__data["data"]["status"]["status_set_date"]
        data["timestamp"] = datetime.fromtimestamp(
            timestamp, tz=get_default_time_zone()
        )
        data["id"] = self.__data["data"]["status"]["status_id"]
        return data

    def get_last_event(self) -> CalendarEvent | None:
        """Retrieve the last event from the Divera data.

        This method fetches the last event based on the sorting order defined in the
        Divera data. If there are no events, it returns None.

        Returns:
            CalendarEvent | None: The last event as a CalendarEvent object if available,
            otherwise None.

        """
        sorting_list = self.__data["data"]["events"]["sorting"]
        if sorting_list:
            last_event_id = sorting_list[0]
            event = self.__data["data"]["events"]["items"].get(str(last_event_id), {})
            return self.__map_event_to_calendar(event)
        return None

    @staticmethod
    def __map_event_to_calendar(event) -> CalendarEvent:
        """Map a raw event from Divera data to a CalendarEvent.

        This private method converts a raw event dictionary from the Divera data
        into a CalendarEvent object. It extracts the start and end times, title,
        location, description, and unique identifier.

        Args:
            event (dict): A dictionary representing the raw event data from Divera.

        Returns:
            CalendarEvent: A CalendarEvent object populated with the event data.

        """
        timezone = get_default_time_zone()
        start = datetime.fromtimestamp(event.get("start"), tz=timezone)
        end = datetime.fromtimestamp(event.get("end"), tz=timezone)
        return CalendarEvent(
            start=start,
            end=end,
            summary=event.get("title"),
            location=event.get("address"),
            description=event.get("text"),
            uid=event.get("id"),
        )

    def get_events(
        self, start_date: datetime, end_date: datetime
    ) -> list[CalendarEvent]:
        """Retrieve all events within a specified date range.

        This method fetches all events from the Divera data that fall within the
        specified start and end dates. It uses the sorting order to iterate through
        events and maps them to CalendarEvent objects.

        Args:
            start_date (datetime): The start date for filtering events.
            end_date (datetime): The end date for filtering events.

        Returns:
            list[CalendarEvent]: A list of CalendarEvent objects that fall within
            the specified date range.

        """
        sorting_list = self.__data["data"]["events"]["sorting"]
        events = []
        for event_id in sorting_list:
            event = self.__data["data"]["events"]["items"].get(str(event_id), {})
            cal_event = self.__map_event_to_calendar(event)
            if cal_event.start >= start_date and cal_event.end <= end_date:
                events.append(cal_event)
        return events

    def has_open_alarms(self) -> bool:
        """Check if there are any open alarms.

        This method iterates through the list of alarm IDs specified in the
        sorting order and checks if any of the corresponding alarms are not closed.

        Returns:
            bool: True if there is at least one open alarm; False otherwise.

        """
        sorting_list = self.__data["data"]["alarm"]["sorting"]
        items = self.__data["data"]["alarm"]["items"]
        return any(
            not items.get(str(alarm_id), {}).get("closed") for alarm_id in sorting_list
        )

    def get_last_alarm_attributes(self) -> dict:
        """Return additional information of the last alarm.

        Returns information about the most recent alarm, including its attributes like ID,
        text, date, address, location coordinates, groups involved, priority, closed status,
        new status, self-addressed status, and answered status.

        Returns:
            dict: A dictionary containing information about the last alarm.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        sorting_list = self.__data["data"]["alarm"]["sorting"]
        if not sorting_list:
            return {}

        last_alarm_id = sorting_list[0]
        alarm = self.__data["data"]["alarm"]["items"].get(str(last_alarm_id), {})

        cross_unit_meta = alarm.get("cross_unit_meta", {})
        cross_unit_groups = cross_unit_meta.get("groups", [])
        cross_unit_clusters = cross_unit_meta.get("clusters", [])

        groups = []

        for group_id in alarm.get("group", []):
            group_name = self.get_group_name_by_id(group_id)
            if group_name is not None:
                groups.append(group_name)
            else:
                cug = cross_unit_groups.get(str(group_id))
                if cug:
                    cluster_id = cug.get("cluster_id")
                    cluster_name = cross_unit_clusters.get(str(cluster_id), {}).get(
                        "name", ""
                    )
                    name = f"{cug.get('name', '')} ({cluster_name})"
                    groups.append(name)

        return {
            "id": alarm.get("id"),
            "foreign_id": alarm.get("foreign_id"),
            "text": alarm.get("text"),
            "date": datetime.fromtimestamp(
                alarm.get("date"), tz=get_default_time_zone()
            ),
            "address": alarm.get("address"),
            "latitude": str(alarm.get("lat")),
            "longitude": str(alarm.get("lng")),
            "groups": groups,
            "priority": alarm.get("priority"),
            "closed": alarm.get("closed"),
            "new": alarm.get("new"),
            "self_addressed": alarm.get("ucr_self_addressed"),
            "answered": self.get_answered_state(alarm),
        }

    def get_answered_state(self, alarm):
        """Return the state of the user who answered the alarm.

        Args:
            alarm (dict): The alarm data.

        Returns:
            str: The state of the user who answered the alarm.

        """
        ucr_id = str(self.get_active_ucr())
        answered = alarm.get("ucr_answered", {})

        for state_id, answer in answered.items():
            if ucr_id in answer:
                return self.get_state_name_by_id(state_id)
        return "not answered"

    def get_last_alarm(self) -> dict:
        """Return information of the last alarm.

        Returns:
            str: The title of the last alarm, or 'unknown' if no alarm exists.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        sorting_list = self.__data["data"]["alarm"]["sorting"]
        if sorting_list:
            last_alarm_id = sorting_list[0]
            alarm = self.__data["data"]["alarm"]["items"].get(str(last_alarm_id), {})
            return alarm.get("title", STATE_UNKNOWN)
        return STATE_UNKNOWN

    def get_last_news(self) -> dict:
        """Return information of the last news.

        Returns:
            str: The title of the last news, or 'unknown' if no news exists.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        sorting_list = self.__data["data"]["news"]["sorting"]
        if sorting_list:
            last_news_id = sorting_list[0]
            news = self.__data["data"]["news"]["items"].get(str(last_news_id), {})
            return news.get("title", STATE_UNKNOWN)
        return STATE_UNKNOWN

    def get_last_news_attributes(self) -> dict:
        """Return additional information of the last news.

        This method retrieves the attributes of the most recent news item, including
        its ID, text, date, address, location coordinates, groups involved, new status,
        and self-addressed status.

        Returns:
            dict: A dictionary containing information about the last news item.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        sorting_list = self.__data["data"]["news"]["sorting"]
        if not sorting_list:
            return {}

        last_news_id = sorting_list[0]
        news = self.__data["data"]["news"]["items"].get(str(last_news_id), {})

        groups = [
            self.get_group_name_by_id(group_id) for group_id in news.get("group", [])
        ]

        return {
            "id": news.get("id"),
            "text": news.get("text"),
            "date": datetime.fromtimestamp(
                news.get("date"), tz=get_default_time_zone()
            ),
            "address": news.get("address"),
            "latitude": str(news.get("lat")),
            "longitude": str(news.get("lng")),
            "groups": groups,
            "new": news.get("new"),
            "self_addressed": news.get("ucr_self_addressed"),
        }

    def get_vehicle_id_list(self):
        """Retrieve the IDs of all vehicles.

        Returns:
            list[int]: A list containing all the vehicle IDs.

        """
        return list(self.__data["data"]["cluster"]["vehicle"].keys())

    def get_vehicle_state(self, vehicle_id: str) -> dict:
        """Retrieve the state of a vehicle by its ID.

        Args:
            vehicle_id (str): The ID of the vehicle.

        Returns:
            dict: The state of the vehicle, or an empty dictionary if the vehicle or key 'fmsstatus_id' is not found.

        Raises:
            KeyError: If the vehicle ID or key 'fmsstatus_id' is not found in the data dictionary.

        """
        try:
            vehicle = self.__data["data"]["cluster"]["vehicle"][vehicle_id]
            return vehicle.get("fmsstatus_id", STATE_UNKNOWN)
        except KeyError:
            LOGGER.error(
                f"Vehicle with ID {vehicle_id} or key 'fmsstatus_id' not found."
            )
            return {}

    def get_vehicle_attributes(self, vehicle_id: str) -> dict:
        """Retrieve the status attributes of a vehicle by its ID.

        Args:
            vehicle_id (str): The ID of the vehicle.

        Returns:
            dict: A dictionary containing the status attributes of the vehicle, including
                  fullname, shortname, name, fmsstatus_note, fmsstatus_ts, latitude, longitude,
                  opta, issi, and number. If the vehicle or required keys are not found, an
                  empty dictionary is returned.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        try:
            vehicle_status = self.__data["data"]["cluster"]["vehicle"][vehicle_id]
            fmsstatus_timestamp = datetime.fromtimestamp(
                vehicle_status.get("fmsstatus_ts"), tz=get_default_time_zone()
            )
            return {
                "fullname": vehicle_status.get("fullname"),
                "shortname": vehicle_status.get("shortname"),
                "name": vehicle_status.get("name"),
                "fmsstatus_note": vehicle_status.get("fmsstatus_note"),
                "fmsstatus_ts": fmsstatus_timestamp,
                "latitude": vehicle_status.get("lat"),
                "longitude": vehicle_status.get("lng"),
                "opta": vehicle_status.get("opta"),
                "issi": vehicle_status.get("issi"),
                "number": vehicle_status.get("number"),
            }
        except KeyError:
            LOGGER.error(
                f"Vehicle with ID {vehicle_id} or one of the required keys not found."
            )
            return {}

    def get_group_name_by_id(self, group_id):
        """Return the name from the given group id.

        Args:
            group_id (int): The ID of the group.

        Returns:
            str or None: The name of the group corresponding to the given ID,
                         or None if the group ID is not found.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        try:
            group = self.__data["data"]["cluster"]["group"][str(group_id)]
            return group["name"]
        except KeyError:
            return None

    def get_default_ucr(self) -> int:
        """Retrieve the default User Cluster Relation (UCR) associated with the data.

        Returns:
            int: The default UCR representing the relation between a user and a cluster.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        return self.__data["data"]["ucr_default"]

    def get_active_ucr(self) -> int:
        """Retrieve the active User Cluster Relation (UCR) associated with the data.

        Returns:
            int: The active UCR representing the current relation between a user and a cluster.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        return self.__data["data"]["ucr_active"]

    def get_default_cluster_name(self) -> str:
        """Retrieve the name of the default cluster associated with the data.

        Returns:
            str: The name of the default cluster.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        ucr_id = self.get_default_ucr()
        return self.get_cluster_name_from_ucr(ucr_id)

    def get_ucr_count(self) -> int:
        """Return the count of User Cluster Relations (UCRs) associated with the data.

        Returns:
            int: The count of UCRs.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        return len(self.get_all_ucrs())

    def get_all_cluster_names(self) -> list:
        """Return a list of all cluster names associated with the data.

        Returns:
            list: A list containing all the cluster names.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        ucr_ids = list(self.__data["data"]["ucr"])
        cluster_names = []
        for ucr_id in ucr_ids:
            ucr_name = self.get_cluster_name_from_ucr(ucr_id)
            cluster_names.append(ucr_name)
        return cluster_names

    def get_all_ucrs(self) -> list:
        """Retrieve a list of all User Cluster Relations (UCRs) associated with the data.

        Returns:
            list: A list containing all the UCR IDs.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        return list(self.__data["data"]["ucr"])

    def get_cluster_names_from_ucrs(self, ucr_ids: list[int]) -> list[str]:
        """Get cluster names from a list of UCR IDs.

        Args:
            ucr_ids (List[int]): List of UCR IDs.

        Returns:
            List[str]: List of cluster names corresponding to the given UCR IDs.

        """
        return [self.get_cluster_name_from_ucr(id) for id in ucr_ids]

    def get_cluster_name_from_ucr(self, ucr_id) -> str:
        """Retrieve the name of the cluster associated with the given User Cluster Relation (UCR) ID.

        Args:
            ucr_id (int): The ID of the User Cluster Relation (UCR) to retrieve the cluster name for.

        Returns:
            str: The name of the cluster associated with the specified UCR ID.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        return self.__data["data"]["ucr"][str(ucr_id)]["name"]

    def get_cluster_id_from_ucr(self, ucr_id) -> int:
        """Retrieve the ID of the cluster associated with the given User Cluster Relation (UCR) ID.

        Args:
            ucr_id (int): The ID of the User Cluster Relation (UCR) to retrieve the cluster ID for.

        Returns:
            int: The ID of the cluster associated with the specified UCR ID.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        return self.__data["data"]["ucr"][str(ucr_id)]["cluster_id"]

    def get_ucr_ids(self, ucr_names) -> list:
        """Retrieve the IDs of User Cluster Relations (UCRs) associated with the given names.

        Args:
            ucr_names (list): A list of UCR names.

        Returns:
            list: A list containing the IDs of the UCRs with the specified names.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        ucr_ids = list(self.__data["data"]["ucr"])
        ucr_name_ids = []
        for ucr_id in ucr_ids:
            ucr_name = self.get_cluster_name_from_ucr(ucr_id)
            if ucr_name in ucr_names:
                ucr_name_ids.append(ucr_id)
        return ucr_name_ids

    def get_accesskey(self) -> str:
        """Retrieve the access key of the user associated with the data.

        Returns:
            str: The access key of the user.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        return self.__data["data"]["user"]["accesskey"]

    def get_email(self) -> str:
        """Retrieve the email of the user associated with the data.

        Returns:
            str: The email address of the user.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        """
        return self.__data["data"]["user"]["email"]

    async def set_user_state_by_id(self, state_id: str):
        """Set the state of the user to the given id.

        This method sends a POST request to the Divera API with the specified
        access key and UCR to update the user's state.

        Args:
            state_id (str): The ID of the state to set the user to.

        Raises:
            DiveraAuthError: If authentication fails while connecting to the Divera API.
            DiveraConnectionError: If an error occurs while connecting to the Divera API.

        """
        state = {"Status": {"id": state_id}}
        params = {PARAM_ACCESSKEY: self.__accesskey, PARAM_UCR: self.__ucr_id}
        url = f"{self.__base_url}{DIVERA_API_STATUS_PATH}"

        try:
            async with self.__session.post(
                url=url, params=params, json=state
            ) as response:
                response.raise_for_status()
        except (ClientError, ClientResponseError) as exc:
            url = remove_params_from_url(exc.request.url)
            LOGGER.error(f"An error occurred while requesting {url!r}.")
            if isinstance(exc, ClientResponseError) and exc.status == UNAUTHORIZED:
                raise DiveraAuthError from None
            raise DiveraConnectionError from None

    def get_cluster_version(self) -> str:
        """Retrieve the version of the cluster.

        Returns:
            str: The version of the cluster, indicating whether it's a free version,
                an alarm version, a pro version, or unknown.

        Raises:
            KeyError: If the required keys are not found in the data dictionary.

        Note:
            The version_id is extracted from the 'data' dictionary attribute of the instance.

        """
        version = self.__data["data"]["cluster"]["version_id"]
        match version:
            case 1:
                return VERSION_FREE
            case 2:
                return VERSION_ALARM
            case 3:
                return VERSION_PRO
            case _:
                return VERSION_UNKNOWN

    async def set_user_state_by_name(self, option: str):
        """Set user state by name.

        Args:
            option (str): The name of the option to set the user state.

        """
        sid = self.get_state_id_by_name(option)
        await self.set_user_state_by_id(sid)

    def check_usergroup_id(self):
        """Check if the user's group ID is allowed.

        This method retrieves the user's group ID from the stored data and verifies whether it belongs
        to the set of allowed group IDs (4 or 8). If the ID is valid, it returns True. Otherwise, it logs
        a warning and returns False.

        Returns:
            bool: True if the user belongs to an allowed group (ID 4 or 8), False otherwise.

        """
        # normal users only have group id 8 or 4
        ucr_id = self.get_default_ucr()
        usergroup_id = self.__data["data"]["ucr"][str(ucr_id)]["usergroup_id"]
        if usergroup_id in {8, 4}:
            return True

        LOGGER.warning("Unsupported Usergroup ID: %s", usergroup_id)
        return False
    
    async def trigger_probe_alarm(self):
        """Trigger a test push (probe alarm) via the Divera API."""
        url = f"{self.__base_url}/api/test-push"  # Passe den Endpunkt ggf. an
        params = {PARAM_ACCESSKEY: self.__accesskey}
        try:
            async with self.__session.post(url, params=params) as response:
                response.raise_for_status()
                LOGGER.info("Probealarm successfully triggered: %s", await response.text())
                return await response.json()
        except (ClientError, ClientResponseError) as exc:
            LOGGER.error("Failed to trigger probe alarm: %s", exc)
            raise

class DiveraError(Exception):
    """Base class for Divera-related exceptions."""


class DiveraAuthError(DiveraError):
    """Exception raised for authentication errors in Divera."""


class DiveraConnectionError(DiveraError):
    """Exception raised for errors occurring during connection to Divera."""
