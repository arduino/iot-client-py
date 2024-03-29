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
from iot_api_client.models.dashboardv2 import Dashboardv2  # noqa: E501
from iot_api_client.rest import ApiException

class TestDashboardv2(unittest.TestCase):
    """Dashboardv2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Dashboardv2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = iot_api_client.models.dashboardv2.Dashboardv2()  # noqa: E501
        if include_optional :
            return Dashboardv2(
                name = 'a', 
                widgets = [
                    iot_api_client.models.widget.widget(
                        height = 56, 
                        height_mobile = 56, 
                        id = '0', 
                        name = '0', 
                        options = { }, 
                        type = '0', 
                        variables = [
                            '0'
                            ], 
                        width = 56, 
                        width_mobile = 56, 
                        x = 56, 
                        x_mobile = 56, 
                        y = 56, 
                        y_mobile = 56, )
                    ]
            )
        else :
            return Dashboardv2(
        )

    def testDashboardv2(self):
        """Test Dashboardv2"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
