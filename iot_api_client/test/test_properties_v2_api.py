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
from iot_api_client.api.properties_v2_api import PropertiesV2Api  # noqa: E501
from iot_api_client.rest import ApiException


class TestPropertiesV2Api(unittest.TestCase):
    """PropertiesV2Api unit test stubs"""

    def setUp(self):
        self.api = iot_api_client.api.properties_v2_api.PropertiesV2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_properties_v2_create(self):
        """Test case for properties_v2_create

        create properties_v2  # noqa: E501
        """
        pass

    def test_properties_v2_delete(self):
        """Test case for properties_v2_delete

        delete properties_v2  # noqa: E501
        """
        pass

    def test_properties_v2_list(self):
        """Test case for properties_v2_list

        list properties_v2  # noqa: E501
        """
        pass

    def test_properties_v2_publish(self):
        """Test case for properties_v2_publish

        publish properties_v2  # noqa: E501
        """
        pass

    def test_properties_v2_show(self):
        """Test case for properties_v2_show

        show properties_v2  # noqa: E501
        """
        pass

    def test_properties_v2_timeseries(self):
        """Test case for properties_v2_timeseries

        timeseries properties_v2  # noqa: E501
        """
        pass

    def test_properties_v2_update(self):
        """Test case for properties_v2_update

        update properties_v2  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()