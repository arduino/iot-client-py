# coding: utf-8

"""
    Arduino IoT Cloud API

    Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iot_api_client.models.arduino_devicev2propertyvalue_value import ArduinoDevicev2propertyvalueValue

class TestArduinoDevicev2propertyvalueValue(unittest.TestCase):
    """ArduinoDevicev2propertyvalueValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArduinoDevicev2propertyvalueValue:
        """Test ArduinoDevicev2propertyvalueValue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArduinoDevicev2propertyvalueValue`
        """
        model = ArduinoDevicev2propertyvalueValue()
        if include_optional:
            return ArduinoDevicev2propertyvalueValue(
                payload = '',
                seqno = 56,
                statistics = iot_api_client.models.arduino_devicev2propertyvalue_value_statistics.ArduinoDevicev2propertyvalue_value_statistics(
                    adr = 1.337, 
                    channel = 1.337, 
                    duplicate = 1.337, 
                    freq = 1.337, 
                    mod_bw = 1.337, 
                    rssi = 1.337, 
                    seqno = 1.337, 
                    sf = 1.337, 
                    snr = 1.337, 
                    time = 1.337, )
            )
        else:
            return ArduinoDevicev2propertyvalueValue(
        )
        """

    def testArduinoDevicev2propertyvalueValue(self):
        """Test ArduinoDevicev2propertyvalueValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()