# ha-keepsimple
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/sysofwan/ha-keepsimple)
![Hassfest](https://github.com/sysofwan/ha-keepsimple/actions/workflows/hassfest.yaml/badge.svg)
![HACS](https://github.com/sysofwan/ha-keepsimple/actions/workflows/hacs.yml/badge.svg)

Home Assistant integration for BLE based keepsimple or HappyLighting lights.

Supports controlling BLE based lights controllable through the keepsimple or HappyLighting apps.

## Installation

Note: Restart is always required after installation.

### [HACS](https://hacs.xyz/) (recommended)
Installation can be done through [HACS custom repository](https://hacs.xyz/docs/faq/custom_repositories).

### Manual installation
You can manually clone this repository inside `config/custom_components/keepsimple`.

For  example, from Terminal plugin:
```
cd /config/custom_components
git clone https://github.com/sysofwan/ha-keepsimple keepsimple
```

## Setup
After installation, you should find keepsimple under the Configuration -> Integrations -> Add integration.

The setup step includes discovery which will list out all keepsimple lights discovered. The setup will validate connection by toggling the selected light. Make sure your light is in-sight to validate this.

The setup needs to be repeated for each light.

## Features
1. Discovery: Automatically discover keepsimple based lights without manually hunting for Bluetooth MAC address
2. On/Off/RGB/Brightness support
3. Live state polling: External control (i.e. IR remote) state changes will reflect in Home Assistant
4. Emulated RGB brightness: Supports adjusting brightness of RGB lights
5. Multiple light support

## Not supported
[Light modes](https://github.com/madhead/saberlight/blob/master/protocols/keepsimple/protocol.md#built-in-modes) (blinking, fading, etc) is not yet supported.

## Known issues
1. Light connection may fail a few times after Home Assistant reboot. The integration will usually reconnect and the issue will resolve itself.
2. After toggling lights, Home Assistant may not reflect state changes for up to 30 seconds. This is due to a lag in keepsimple status API.

## Debugging
Add the following to `configuration.yml` to show debugging logs. Please make sure to include debug logs when filing an issue.

See [logger intergration docs](https://www.home-assistant.io/integrations/logger/) for more information to configure logging.

```yml
logger:
  default: warn
  logs:
    custom_components.keepsimple: debug
```

## Credits
This integration will not be possible without the awesome work of reverse engineering and documenting the keepsimple BLE protocol [here](https://github.com/madhead/saberlight/blob/master/protocols/keepsimple/protocol.md).
