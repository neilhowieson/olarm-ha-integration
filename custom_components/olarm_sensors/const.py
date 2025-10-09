"""Module that stores all the constants for the integration."""
from __future__ import annotations

import logging

from homeassistant.components.alarm_control_panel import AlarmControlPanelState
from homeassistant.components.binary_sensor import BinarySensorDeviceClass

VERSION = "2.3.3"
LOGGER = logging.getLogger(__package__)

DOMAIN = "olarm_sensors"

AUTHENTICATION_ERROR = "invalid_credentials"
CONF_DEVICE_FIRMWARE = "olarm_device_firmware"
CONF_ALARM_CODE = "olarm_arm_code"
CONF_OLARM_DEVICES = "selected_olarm_devices"
OLARM_DEVICE_NAMES = "olarm_device_names"
OLARM_DEVICES = "olarm_devices"
OLARM_DEVICE_AMOUNT = "olarm_device_amount"

# Olarm -> HA alarm state mapping (new enum-based)
OLARM_STATE_TO_HA = {
    "disarm":    AlarmControlPanelState.DISARMED,
    "notready":  AlarmControlPanelState.DISARMED,
    "countdown": AlarmControlPanelState.ARMING,
    "sleep":     AlarmControlPanelState.ARMED_NIGHT,
    "stay":      AlarmControlPanelState.ARMED_HOME,
    "arm":       AlarmControlPanelState.ARMED_AWAY,
    "alarm":     AlarmControlPanelState.TRIGGERED,
    "fire":      AlarmControlPanelState.TRIGGERED,
    "emergency": AlarmControlPanelState.TRIGGERED,
}

# Action change -> HA alarm state mapping (new enum-based)
OLARM_CHANGE_TO_HA = {
    "area-disarm": AlarmControlPanelState.DISARMED,
    "area-stay":   AlarmControlPanelState.ARMED_HOME,
    "area-sleep":  AlarmControlPanelState.ARMED_NIGHT,
    "area-arm":    AlarmControlPanelState.ARMED_AWAY,
    None: None,
    "null": None,
}

# Zone type -> BinarySensor device class mapping
OLARM_ZONE_TYPE_TO_HA = {
    "":    BinarySensorDeviceClass.MOTION,
    0:     BinarySensorDeviceClass.MOTION,
    10:    BinarySensorDeviceClass.DOOR,
    11:    BinarySensorDeviceClass.WINDOW,
    20:    BinarySensorDeviceClass.MOTION,
    21:    BinarySensorDeviceClass.MOTION,
    90:    BinarySensorDeviceClass.PROBLEM,
    50:    BinarySensorDeviceClass.SAFETY,
    51:    BinarySensorDeviceClass.SAFETY,
    1000:  BinarySensorDeviceClass.PLUG,
    1001:  BinarySensorDeviceClass.POWER,
}

class TempEntry:
    """Representation of a temporary config entry."""
    scan_interval: int = 10
    api_key: str = ""

    def __init__(self, scan_interval: int, api_key: str) -> None:
        self.scan_interval = scan_interval
        self.api_key = api_key

    @property
    def data(self) -> dict:
        return {"scan_interval": self.scan_interval, "api_key": self.api_key}

class BypassZone:
    """Representation of a bypassed zone."""
    zone: int = 0

    def __init__(self, zone: int) -> None:
        self.zone = zone

    @property
    def data(self) -> dict:
        return {"zone_num": self.zone}
