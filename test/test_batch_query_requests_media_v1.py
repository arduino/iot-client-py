# coding: utf-8

"""
    Arduino IoT Cloud API

    Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iot_api_client.models.batch_query_requests_media_v1 import BatchQueryRequestsMediaV1

class TestBatchQueryRequestsMediaV1(unittest.TestCase):
    """BatchQueryRequestsMediaV1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BatchQueryRequestsMediaV1:
        """Test BatchQueryRequestsMediaV1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BatchQueryRequestsMediaV1`
        """
        model = BatchQueryRequestsMediaV1()
        if include_optional:
            return BatchQueryRequestsMediaV1(
                requests = [
                    iot_api_client.models.batch_query_request_media_v1.BatchQueryRequestMediaV1(
                        aggregation = 'AVG', 
                        from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        interval = 56, 
                        q = '', 
                        series_limit = 56, 
                        to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                resp_version = 56
            )
        else:
            return BatchQueryRequestsMediaV1(
                requests = [
                    iot_api_client.models.batch_query_request_media_v1.BatchQueryRequestMediaV1(
                        aggregation = 'AVG', 
                        from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        interval = 56, 
                        q = '', 
                        series_limit = 56, 
                        to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                resp_version = 56,
        )
        """

    def testBatchQueryRequestsMediaV1(self):
        """Test BatchQueryRequestsMediaV1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()