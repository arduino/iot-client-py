# coding: utf-8

"""
    Arduino IoT Cloud API

    Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import iot_api_client
from iot_api_client.models.arduino_devicev2propertyvalues import ArduinoDevicev2propertyvalues  # noqa: E501
from iot_api_client.rest import ApiException

class TestArduinoDevicev2propertyvalues(unittest.TestCase):
    """ArduinoDevicev2propertyvalues unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ArduinoDevicev2propertyvalues
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArduinoDevicev2propertyvalues`
        """
        model = iot_api_client.models.arduino_devicev2propertyvalues.ArduinoDevicev2propertyvalues()  # noqa: E501
        if include_optional :
            return ArduinoDevicev2propertyvalues(
                id = '', 
                last_evaluated_key = iot_api_client.models.arduino_devicev2propertyvalues_last_evaluated_key.ArduinoDevicev2propertyvalues_last_evaluated_key(
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', 
                    name = '', ), 
                name = '', 
                values = [
                    iot_api_client.models.mediatype_identifier:_application/vnd/arduino/devicev2propertyvalue+json;_view=default.Mediatype identifier: application/vnd.arduino.devicev2propertyvalue+json; view=default(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = iot_api_client.models.arduino_devicev2propertyvalue_value.ArduinoDevicev2propertyvalue_value(
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
                                time = 1.337, ), ), )
                    ]
            )
        else :
            return ArduinoDevicev2propertyvalues(
                id = '',
                last_evaluated_key = iot_api_client.models.arduino_devicev2propertyvalues_last_evaluated_key.ArduinoDevicev2propertyvalues_last_evaluated_key(
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', 
                    name = '', ),
                name = '',
                values = [
                    iot_api_client.models.mediatype_identifier:_application/vnd/arduino/devicev2propertyvalue+json;_view=default.Mediatype identifier: application/vnd.arduino.devicev2propertyvalue+json; view=default(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = iot_api_client.models.arduino_devicev2propertyvalue_value.ArduinoDevicev2propertyvalue_value(
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
                                time = 1.337, ), ), )
                    ],
        )
        """

    def testArduinoDevicev2propertyvalues(self):
        """Test ArduinoDevicev2propertyvalues"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
