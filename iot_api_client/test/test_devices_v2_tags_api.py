# coding: utf-8

"""
    Arduino IoT Cloud API

     Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import iot_api_client
from iot_api_client.api.devices_v2_tags_api import DevicesV2TagsApi  # noqa: E501
from iot_api_client.rest import ApiException


class TestDevicesV2TagsApi(unittest.TestCase):
    """DevicesV2TagsApi unit test stubs"""

    def setUp(self):
        self.api = iot_api_client.api.devices_v2_tags_api.DevicesV2TagsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_devices_v2_tags_delete(self):
        """Test case for devices_v2_tags_delete

        delete devices_v2_tags  # noqa: E501
        """
        pass

    def test_devices_v2_tags_list(self):
        """Test case for devices_v2_tags_list

        list devices_v2_tags  # noqa: E501
        """
        pass

    def test_devices_v2_tags_upsert(self):
        """Test case for devices_v2_tags_upsert

        upsert devices_v2_tags  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
