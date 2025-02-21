import pytest
from custom_components.divera247.divera247 import DiveraClient
import os


@pytest.fixture


def divera_client():
    """Fixture to create a DiveraClient instance."""
    access_key = os.getenv("DIVERA_ACCESS_KEY")
    return DiveraClient(access_key=access_key, base_url="https://api.divera247.com")


def test_trigger_probe_alarm_success(divera_client, mocker):
    """Test successful triggering of probe alarm."""
    mock_response = mocker.Mock()
    mock_response.status = 200
    mock_response.json.return_value = {"status": "success"}
    mocker.patch("aiohttp.ClientSession.post", return_value=mock_response)

    response = divera_client.trigger_probe_alarm()
    assert response["status"] == "success"


def test_trigger_probe_alarm_failure(divera_client, mocker):
    """Test failure in triggering probe alarm."""
    mock_response = mocker.Mock()
    mock_response.status = 400
    mock_response.json.return_value = {"status": "failure"}
    mocker.patch("aiohttp.ClientSession.post", return_value=mock_response)

    with pytest.raises(Exception):
        divera_client.trigger_probe_alarm()
