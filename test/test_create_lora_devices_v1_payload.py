# coding: utf-8

"""
    Arduino IoT Cloud API

    Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iot_api_client.models.create_lora_devices_v1_payload import CreateLoraDevicesV1Payload

class TestCreateLoraDevicesV1Payload(unittest.TestCase):
    """CreateLoraDevicesV1Payload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateLoraDevicesV1Payload:
        """Test CreateLoraDevicesV1Payload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateLoraDevicesV1Payload`
        """
        model = CreateLoraDevicesV1Payload()
        if include_optional:
            return CreateLoraDevicesV1Payload(
                app = '',
                app_eui = 'w8q6zgckec0l3o4g',
                app_key = 'w8q6zgckec0l3o4g',
                eui = 'w8q6zgckec0l3o4g',
                frequency_plan = 'EU_863_870_TTN',
                name = '',
                serial = '',
                type = 'lora-device',
                user_id = ''
            )
        else:
            return CreateLoraDevicesV1Payload(
                app = '',
                eui = 'w8q6zgckec0l3o4g',
                frequency_plan = 'EU_863_870_TTN',
                name = '',
                type = 'lora-device',
                user_id = '',
        )
        """

    def testCreateLoraDevicesV1Payload(self):
        """Test CreateLoraDevicesV1Payload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
