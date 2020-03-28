from abc import ABC, abstractmethod

from example.core.entity.broadband_access_device import BroadbandAccessDevice


class GetDeviceDetails(ABC):
    @abstractmethod
    def __call__(self, hostname: str) -> BroadbandAccessDevice:
        pass


class DeviceNotFoundException(RuntimeError):
    pass


class GetBroadbandDeviceDetailUsecase:
    def __init__(self, get_device_details: GetDeviceDetails) -> None:
        self.__get_device_details = get_device_details

    def __call__(self, hostname: str) -> BroadbandAccessDevice:
        device = self.__get_device_details(hostname)

        print("#" * 20)
        print(self.__get_device_details)
        print("#" * 20)

        if not device:
            raise DeviceNotFoundException()

        return device
