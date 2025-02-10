import asyncio
import logging
from bleak import BleakClient, BleakError
import voluptuous as vol

from homeassistant.components.light import (
    ATTR_BRIGHTNESS, LightEntity, PLATFORM_SCHEMA, SUPPORT_BRIGHTNESS
)
from homeassistant.const import CONF_MAC
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, DEFAULT_MAC, CHARACTERISTIC_UUID

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_MAC, default=DEFAULT_MAC): cv.string,
})

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the KeepSimple BLE Light."""
    mac_address = config[CONF_MAC]
    light = KeepSimpleBLELight(mac_address)
    async_add_entities([light], True)

class KeepSimpleBLELight(LightEntity):
    """Representation of a KeepSimple BLE Light."""

    def __init__(self, mac):
        """Initialize the light."""
        self._mac = mac
        self._is_on = False
        self._brightness = 255

    async def async_turn_on(self, **kwargs):
        """Turn the light on."""
        try:
            async with BleakClient(self._mac) as client:
                if ATTR_BRIGHTNESS in kwargs:
                    self._brightness = kwargs[ATTR_BRIGHTNESS]
                    await client.write_gatt_char(CHARACTERISTIC_UUID, bytearray([self._brightness]))
                else:
                    await client.write_gatt_char(CHARACTERISTIC_UUID, bytearray([0xFF]))  # Max brightness
                self._is_on = True
                self.async_write_ha_state()
        except BleakError as e:
            _LOGGER.error(f"Failed to turn on KeepSimple BLE light: {e}")

    async def async_turn_off(self, **kwargs):
        """Turn the light off."""
        try:
            async with BleakClient(self._mac) as client:
                await client.write_gatt_char(CHARACTERISTIC_UUID, bytearray([0x00]))  # Off command
                self._is_on = False
                self.async_write_ha_state()
        except BleakError as e:
            _LOGGER.error(f"Failed to turn off KeepSimple BLE light: {e}")

    async def async_update(self):
        """Fetch new state data (not always possible for BLE devices)."""
        pass  # Some BLE devices do not report state back

    @property
    def supported_features(self):
        """Return supported features (e.g., brightness)."""
        return SUPPORT_BRIGHTNESS

    @property
    def is_on(self):
        """Return true if the light is on."""
        return self._is_on

    @property
    def brightness(self):
        """Return the current brightness."""
        return self._brightness
