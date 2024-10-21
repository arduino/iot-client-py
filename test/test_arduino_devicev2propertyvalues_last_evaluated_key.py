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
from iot_api_client.models.arduino_devicev2propertyvalues_last_evaluated_key import ArduinoDevicev2propertyvaluesLastEvaluatedKey  # noqa: E501
from iot_api_client.rest import ApiException

class TestArduinoDevicev2propertyvaluesLastEvaluatedKey(unittest.TestCase):
    """ArduinoDevicev2propertyvaluesLastEvaluatedKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ArduinoDevicev2propertyvaluesLastEvaluatedKey
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArduinoDevicev2propertyvaluesLastEvaluatedKey`
        """
        model = iot_api_client.models.arduino_devicev2propertyvalues_last_evaluated_key.ArduinoDevicev2propertyvaluesLastEvaluatedKey()  # noqa: E501
        if include_optional :
            return ArduinoDevicev2propertyvaluesLastEvaluatedKey(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                id = '', 
                name = ''
            )
        else :
            return ArduinoDevicev2propertyvaluesLastEvaluatedKey(
        )
        """

    def testArduinoDevicev2propertyvaluesLastEvaluatedKey(self):
        """Test ArduinoDevicev2propertyvaluesLastEvaluatedKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
