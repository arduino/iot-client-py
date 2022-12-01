# coding: utf-8

"""
    Arduino IoT Cloud API

     Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import iot_api_client
from iot_api_client.models.arduino_series_raw_batch_lastvalue import ArduinoSeriesRawBatchLastvalue  # noqa: E501
from iot_api_client.rest import ApiException

class TestArduinoSeriesRawBatchLastvalue(unittest.TestCase):
    """ArduinoSeriesRawBatchLastvalue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ArduinoSeriesRawBatchLastvalue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = iot_api_client.models.arduino_series_raw_batch_lastvalue.ArduinoSeriesRawBatchLastvalue()  # noqa: E501
        if include_optional :
            return ArduinoSeriesRawBatchLastvalue(
                responses = [
                    iot_api_client.models.mediatype_identifier:_application/vnd/arduino/series/raw/last/value/response+json;_view=default.Mediatype identifier: application/vnd.arduino.series.raw.last.value.response+json; view=default(
                        count_values = 56, 
                        property_id = '0', 
                        thing_id = '0', 
                        times = [
                            datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                            ], 
                        values = [
                            null
                            ], )
                    ], 
                status = '0'
            )
        else :
            return ArduinoSeriesRawBatchLastvalue(
                responses = [
                    iot_api_client.models.mediatype_identifier:_application/vnd/arduino/series/raw/last/value/response+json;_view=default.Mediatype identifier: application/vnd.arduino.series.raw.last.value.response+json; view=default(
                        count_values = 56, 
                        property_id = '0', 
                        thing_id = '0', 
                        times = [
                            datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                            ], 
                        values = [
                            null
                            ], )
                    ],
                status = '0',
        )

    def testArduinoSeriesRawBatchLastvalue(self):
        """Test ArduinoSeriesRawBatchLastvalue"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
