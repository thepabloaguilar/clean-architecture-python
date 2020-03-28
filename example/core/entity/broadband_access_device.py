from dataclasses import dataclass

from .exchange import Exchange
from .device_type import DeviceType


@dataclass
class BroadbandAccessDevice:
    id: int
    exchange: Exchange
    hostname: str
    serial_number: str
    type: DeviceType
    available_port: int
