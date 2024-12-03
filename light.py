from homeassistant.components.light import LightEntity
from bleak import BleakClient

DOMAIN = "keepsimple_lights"

class KeepsimpleLight(LightEntity):
    """Representation of a Keepsimple Bluetooth Light."""

    def __init__(self, name, address):
        self._name = name
        self._address = address
        self._is_on = False

    async def async_turn_on(self, **kwargs):
        """Turn on the light."""
        async with BleakClient(self._address) as client:
            await client.write_gatt_char("CHARACTERISTIC_UUID", b"\x01")
        self._is_on = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        """Turn off the light."""
        async with BleakClient(self._address) as client:
            await client.write_gatt_char("CHARACTERISTIC_UUID", b"\x00")
        self._is_on = False
        self.async_write_ha_state()

    @property
    def is_on(self):
        """Return the light status."""
        return self._is_on

    @property
    def name(self):
        """Return the name of the light."""
        return self._name
