from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType

DOMAIN = "keepsimple_lights"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up Keepsimple Lights integration."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry."""
    hass.config_entries.async_setup_platforms(entry, ["light"])
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload Keepsimple Lights."""
    return await hass.config_entries.async_unload_platforms(entry, ["light"])
