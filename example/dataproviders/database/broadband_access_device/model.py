from sqlalchemy import Column, String, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship

from ..exchange.model import ExchangeModel
from example.core.entity.broadband_access_device import BroadbandAccessDevice
from example.core.entity.device_type import DeviceType
from example.configuration.database import DatabaseBase


class BroadbandAccessDeviceModel(DatabaseBase):
    __tablename__ = "broadband_access_device"

    id = Column("id", Integer, primary_key=True)
    exchange_id = Column("exchange_id", Integer, ForeignKey("exchange.id"))
    hostname = Column("hostname", String)
    serial_number = Column("serial_number", String)
    type = Column("type", Enum(DeviceType))
    available_port = Column("available_port", Integer)

    exchange = relationship(ExchangeModel, backref="broadband_access_devices")

    def to_entity(self) -> BroadbandAccessDevice:
        return BroadbandAccessDevice(
            id=self.id,
            exchange=self.exchange.to_entity(),
            hostname=self.hostname,
            serial_number=self.serial_number,
            type=self.type,
            available_port=self.available_port,
        )
