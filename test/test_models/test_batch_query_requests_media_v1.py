# coding: utf-8

"""
    Arduino IoT Cloud API

     Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

import unittest

import iot_api_client
from iot_api_client.model.batch_query_requests_media_v1 import BatchQueryRequestsMediaV1
from iot_api_client import configuration


class TestBatchQueryRequestsMediaV1(unittest.TestCase):
    """BatchQueryRequestsMediaV1 unit test stubs"""
    _configuration = configuration.Configuration()


if __name__ == '__main__':
    unittest.main()
