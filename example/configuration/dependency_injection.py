from punq import Container

from ..core.usecase.broadband_access_device.get_details import (
    GetBroadbandDeviceDetailUsecase,
    GetDeviceDetails,
)
from ..dataproviders.database.broadband_access_device.repository import (
    GetDeviceDetailsBroadbandAccessDeviceRepository,
)


di_container = Container()

# Dependencies
di_container.register(GetDeviceDetails, GetDeviceDetailsBroadbandAccessDeviceRepository)

# Usecases
di_container.register(GetBroadbandDeviceDetailUsecase)
