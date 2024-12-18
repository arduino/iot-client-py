# coding: utf-8

"""
    Arduino IoT Cloud API

    Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iot_api_client.models.batch_query_raw_request_media_v1 import BatchQueryRawRequestMediaV1

class TestBatchQueryRawRequestMediaV1(unittest.TestCase):
    """BatchQueryRawRequestMediaV1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BatchQueryRawRequestMediaV1:
        """Test BatchQueryRawRequestMediaV1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BatchQueryRawRequestMediaV1`
        """
        model = BatchQueryRawRequestMediaV1()
        if include_optional:
            return BatchQueryRawRequestMediaV1(
                var_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                q = '',
                series_limit = 56,
                sort = 'DESC',
                to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return BatchQueryRawRequestMediaV1(
                q = '',
        )
        """

    def testBatchQueryRawRequestMediaV1(self):
        """Test BatchQueryRawRequestMediaV1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
