"""The UK Carbon Intensity Component"""
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import HomeAssistantType

from . import const

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistantType, config: ConfigEntry) -> bool:
    """ Set up the uk carbon intensity integration"""
    return True


async def async_setup_entry(hass: HomeAssistantType, entry: ConfigEntry) -> bool:
    """Setup UK carbon intensity integration from a config flow entry"""

    hass.async_add_job(
        hass.config_entries.async_forward_entry_setup(entry, "binary_sensor")
    )

    # Return boolean to indicate that initialization was successful.
    _LOGGER.debug("UK carbon intensity integration entry setup complete")
    return True


async def async_unload_entry(hass, entry):
    """Unload a config entry."""
    bridge = hass.data[const.DOMAIN].pop(entry.data["binary_sensor"])
    return await bridge.async_reset()
