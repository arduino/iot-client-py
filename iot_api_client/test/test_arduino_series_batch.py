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
from iot_api_client.models.arduino_series_batch import ArduinoSeriesBatch  # noqa: E501
from iot_api_client.rest import ApiException

class TestArduinoSeriesBatch(unittest.TestCase):
    """ArduinoSeriesBatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ArduinoSeriesBatch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = iot_api_client.models.arduino_series_batch.ArduinoSeriesBatch()  # noqa: E501
        if include_optional :
            return ArduinoSeriesBatch(
                resp_version = 56, 
                responses = [
                    iot_api_client.models.mediatype_identifier:_application/vnd/arduino/series/response+json;_view=default.Mediatype identifier: application/vnd.arduino.series.response+json; view=default(
                        count_values = 56, 
                        from_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        interval = 56, 
                        message = '0', 
                        query = '0', 
                        resp_version = 56, 
                        series_limit = 56, 
                        status = '0', 
                        times = [
                            datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                            ], 
                        to_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        values = [
                            1.337
                            ], )
                    ]
            )
        else :
            return ArduinoSeriesBatch(
                resp_version = 56,
                responses = [
                    iot_api_client.models.mediatype_identifier:_application/vnd/arduino/series/response+json;_view=default.Mediatype identifier: application/vnd.arduino.series.response+json; view=default(
                        count_values = 56, 
                        from_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        interval = 56, 
                        message = '0', 
                        query = '0', 
                        resp_version = 56, 
                        series_limit = 56, 
                        status = '0', 
                        times = [
                            datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                            ], 
                        to_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        values = [
                            1.337
                            ], )
                    ],
        )

    def testArduinoSeriesBatch(self):
        """Test ArduinoSeriesBatch"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
