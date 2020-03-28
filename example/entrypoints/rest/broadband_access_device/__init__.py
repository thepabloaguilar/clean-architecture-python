from flask import Blueprint
from flask_restful import Api

from .get_broadband_access_device_endpoint import GetBroadbandAccessDeviceEndpoint


broadband_access_device_bp = Blueprint("broadband_access_device", __name__)
broadband_access_device_api = Api(broadband_access_device_bp)

broadband_access_device_api.add_resource(
    GetBroadbandAccessDeviceEndpoint, GetBroadbandAccessDeviceEndpoint.API_PATH,
)
