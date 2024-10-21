# coding: utf-8

"""
    Arduino IoT Cloud API

    Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iot_api_client.models.arduino_devicev2templatedevice import ArduinoDevicev2templatedevice

class TestArduinoDevicev2templatedevice(unittest.TestCase):
    """ArduinoDevicev2templatedevice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArduinoDevicev2templatedevice:
        """Test ArduinoDevicev2templatedevice
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArduinoDevicev2templatedevice`
        """
        model = ArduinoDevicev2templatedevice()
        if include_optional:
            return ArduinoDevicev2templatedevice(
                fqbn = '',
                name = ''
            )
        else:
            return ArduinoDevicev2templatedevice(
        )
        """

    def testArduinoDevicev2templatedevice(self):
        """Test ArduinoDevicev2templatedevice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
