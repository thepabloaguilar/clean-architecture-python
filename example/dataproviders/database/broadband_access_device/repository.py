from .model import BroadbandAccessDeviceModel
from example.core.entity.broadband_access_device import BroadbandAccessDevice
from example.core.usecase.broadband_access_device.get_details import GetDeviceDetails


class GetDeviceDetailsBroadbandAccessDeviceRepository(GetDeviceDetails):
    def __call__(self, hostname: str) -> BroadbandAccessDevice:
        result_model = BroadbandAccessDeviceModel.query.filter(
            BroadbandAccessDeviceModel.hostname == hostname
        ).one_or_none()
        if result_model:
            return result_model.to_entity()
