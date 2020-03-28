from dataclasses import dataclass

from flask import Response
from flask_restful import Resource
from dataclasses_json import dataclass_json

from example.configuration.dependency_injection import di_container
from example.core.entity.broadband_access_device import BroadbandAccessDevice
from example.core.usecase.broadband_access_device.get_details import (
    GetBroadbandDeviceDetailUsecase,
    DeviceNotFoundException,
)
from ..exception import NotFoundException


@dataclass_json
@dataclass
class BroadbandAccessDeviceDto:
    exchange_code: str
    hostname: str
    serial_number: str
    type: str


class GetBroadbandAccessDeviceEndpoint(Resource):
    API_PATH = "/broadbandaccessdevice/<hostname>/"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_broadband_access_device_details_usecase = di_container.resolve(
            GetBroadbandDeviceDetailUsecase
        )

    def get(self, hostname: str):
        try:
            device_details = self.get_broadband_access_device_details_usecase(hostname)
            return Response(
                self.__to_dto(device_details).to_json(),
                status=200,
                mimetype="application/json",
            )
        except DeviceNotFoundException:
            raise NotFoundException(f"Broadband access device not found: {hostname}")

    def __to_dto(self, device_details: BroadbandAccessDevice):
        return BroadbandAccessDeviceDto(
            device_details.exchange.code,
            device_details.hostname,
            device_details.serial_number,
            device_details.type.name,
        )
