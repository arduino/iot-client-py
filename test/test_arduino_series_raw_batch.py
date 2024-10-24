# coding: utf-8

"""
    Arduino IoT Cloud API

    Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iot_api_client.models.arduino_series_raw_batch import ArduinoSeriesRawBatch

class TestArduinoSeriesRawBatch(unittest.TestCase):
    """ArduinoSeriesRawBatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArduinoSeriesRawBatch:
        """Test ArduinoSeriesRawBatch
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArduinoSeriesRawBatch`
        """
        model = ArduinoSeriesRawBatch()
        if include_optional:
            return ArduinoSeriesRawBatch(
                resp_version = 56,
                responses = [
                    iot_api_client.models.mediatype_identifier:_application/vnd/arduino/series/raw/response+json;_view=default.Mediatype identifier: application/vnd.arduino.series.raw.response+json; view=default(
                        count_values = 56, 
                        from_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        property_id = '', 
                        property_name = '', 
                        property_type = '', 
                        query = '', 
                        resp_version = 56, 
                        series = iot_api_client.models.batch_query_raw_response_series_media_v1.BatchQueryRawResponseSeriesMediaV1(
                            metric = '', ), 
                        series_limit = 56, 
                        sort = 'ASC', 
                        status = '', 
                        thing_id = '', 
                        times = [
                            datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                            ], 
                        to_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        values = [
                            null
                            ], )
                    ]
            )
        else:
            return ArduinoSeriesRawBatch(
                resp_version = 56,
                responses = [
                    iot_api_client.models.mediatype_identifier:_application/vnd/arduino/series/raw/response+json;_view=default.Mediatype identifier: application/vnd.arduino.series.raw.response+json; view=default(
                        count_values = 56, 
                        from_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        property_id = '', 
                        property_name = '', 
                        property_type = '', 
                        query = '', 
                        resp_version = 56, 
                        series = iot_api_client.models.batch_query_raw_response_series_media_v1.BatchQueryRawResponseSeriesMediaV1(
                            metric = '', ), 
                        series_limit = 56, 
                        sort = 'ASC', 
                        status = '', 
                        thing_id = '', 
                        times = [
                            datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                            ], 
                        to_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        values = [
                            null
                            ], )
                    ],
        )
        """

    def testArduinoSeriesRawBatch(self):
        """Test ArduinoSeriesRawBatch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
