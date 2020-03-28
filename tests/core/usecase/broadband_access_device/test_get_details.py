from unittest import TestCase
from unittest.mock import Mock

from example.core.entity.broadband_access_device import BroadbandAccessDevice
from example.core.entity.device_type import DeviceType
from example.core.entity.exchange import Exchange
from example.core.usecase.broadband_access_device.get_details import (
    GetBroadbandDeviceDetailUsecase,
    DeviceNotFoundException,
)


class GetBroadbandDeviceDetailUsecaseTest(TestCase):
    def setUp(self):
        self.get_device_details = Mock()
        self.get_broadband_device_detail_usecase = GetBroadbandDeviceDetailUsecase(
            self.get_device_details
        )

    def test_should_return_device_details(self):
        expected_device = BroadbandAccessDevice(
            id=98,
            exchange=Exchange(code="Code", name="Exchange Name", post_code="Post Code"),
            hostname="Hostname",
            serial_number="Serial Number",
            type=DeviceType.ADSL,
            available_port=2020,
        )

        actual_device = self.get_device_details.return_value = expected_device

        self.assertEqual(expected_device, actual_device)

    def test_should_raise_error_when_device_is_not_found(self):
        self.get_device_details.return_value = None
        with self.assertRaises(DeviceNotFoundException):
            self.get_broadband_device_detail_usecase("ANY_HOSTNAME")
