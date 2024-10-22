# coding: utf-8

"""
    Arduino IoT Cloud API

    Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iot_api_client.models.arduino_devicev2_otaupload import ArduinoDevicev2Otaupload

class TestArduinoDevicev2Otaupload(unittest.TestCase):
    """ArduinoDevicev2Otaupload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArduinoDevicev2Otaupload:
        """Test ArduinoDevicev2Otaupload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArduinoDevicev2Otaupload`
        """
        model = ArduinoDevicev2Otaupload()
        if include_optional:
            return ArduinoDevicev2Otaupload(
                file_sha = '',
                ota_id = '',
                ota_version = 56,
                status = ''
            )
        else:
            return ArduinoDevicev2Otaupload(
                ota_version = 56,
        )
        """

    def testArduinoDevicev2Otaupload(self):
        """Test ArduinoDevicev2Otaupload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
