import logging

import requests
from homeassistant.components.binary_sensor import BinarySensorDevice
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import HomeAssistantType

from . import const

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistantType, config: ConfigEntry, async_add_devices
) -> bool:
    async_add_devices([UkCarbonIntensitySensor(hass)])
    return True


class UkCarbonIntensitySensor(BinarySensorDevice):
    def __init__(self, hass):
        self._name = const.BINARY_SENSOR_NAME
        self._state = False
        self._attributes = {}

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._state

    @property
    def device_state_attributes(self):
        return self._attributes

    def update(self):
        outcode = self.hass.data[const.DOMAIN][const.OUTCODE]
        if not outcode:
            response = requests.get("https://api.carbonintensity.org.uk/intensity")
            response.raise_for_status()
            intensity = response.json()["data"][0]["intensity"]
        else:
            response = requests.get(
                f"https://api.carbonintensity.org.uk/regional/postcode/{outcode}"
            )
            response.raise_for_status()
            intensity = response.json()["data"][0]["data"][0]["intensity"]
        index = intensity[const.INDEX]
        self._attributes = {
            const.OUTCODE: outcode,
            const.INDEX: index,
            const.FORECAST: intensity[const.FORECAST],
        }
        if index in const.LOW_VALUES:
            self._state = True
        else:
            self._state = False
