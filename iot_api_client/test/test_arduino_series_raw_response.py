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
from iot_api_client.models.arduino_series_raw_response import ArduinoSeriesRawResponse  # noqa: E501
from iot_api_client.rest import ApiException

class TestArduinoSeriesRawResponse(unittest.TestCase):
    """ArduinoSeriesRawResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ArduinoSeriesRawResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = iot_api_client.models.arduino_series_raw_response.ArduinoSeriesRawResponse()  # noqa: E501
        if include_optional :
            return ArduinoSeriesRawResponse(
                count_values = 56, 
                from_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                message = '0', 
                query = '0', 
                resp_version = 56, 
                series = iot_api_client.models.batch_query_raw_response_series_media_v1.BatchQueryRawResponseSeriesMediaV1(
                    metric = '0', ), 
                series_limit = 56, 
                sort = 'ASC', 
                status = '0', 
                times = [
                    datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                    ], 
                to_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                values = [
                    null
                    ]
            )
        else :
            return ArduinoSeriesRawResponse(
                count_values = 56,
                from_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                query = '0',
                resp_version = 56,
                series = iot_api_client.models.batch_query_raw_response_series_media_v1.BatchQueryRawResponseSeriesMediaV1(
                    metric = '0', ),
                sort = 'ASC',
                status = '0',
                times = [
                    datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                    ],
                to_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                values = [
                    null
                    ],
        )

    def testArduinoSeriesRawResponse(self):
        """Test ArduinoSeriesRawResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
