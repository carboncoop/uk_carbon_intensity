"""Config flow for Uk Carbon Intensity."""
import logging

import requests
from homeassistant import config_entries

from . import const

_LOGGER = logging.getLogger(__name__)


@config_entries.HANDLERS.register(const.DOMAIN)
class UkCarbonIntensityFlowHandler(config_entries.ConfigFlow):
    """Config flow for the uk carbon intensity component"""

    async def async_step_user(self, user_input):
        _LOGGER.info("Setting up uk carbon intensity sensor")
        _LOGGER.info(self.hass.config.latitude)
        _LOGGER.info(self.hass.config.longitude)
        latitude = self.hass.config.latitude
        longitude = self.hass.config.longitude
        outcode = _get_outcode_for_coords(latitude, longitude)
        self.hass.data[const.DOMAIN] = {}
        self.hass.data[const.DOMAIN][const.OUTCODE] = outcode
        return self.async_create_entry(
            title=const.BINARY_SENSOR_NAME,
            data={"carbon_intensity_outcode_used": outcode},
        )


def _get_outcode_for_coords(lat, lon):
    response = requests.get(f"https://api.postcodes.io/outcodes?lon={lon}&lat={lat}")
    response.raise_for_status()
    try:
        outcode = response.json()["result"][0]["outcode"]
        return outcode
    except KeyError:
        _LOGGER.info("outcode not found")
