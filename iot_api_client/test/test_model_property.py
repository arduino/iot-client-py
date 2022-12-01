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
from iot_api_client.models.model_property import ModelProperty  # noqa: E501
from iot_api_client.rest import ApiException

class TestModelProperty(unittest.TestCase):
    """ModelProperty unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ModelProperty
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = iot_api_client.models.model_property.ModelProperty()  # noqa: E501
        if include_optional :
            return ModelProperty(
                max_value = 1.337, 
                min_value = 1.337, 
                name = '0', 
                permission = 'READ_ONLY', 
                persist = True, 
                tag = 1.337, 
                type = 'ANALOG', 
                update_parameter = 1.337, 
                update_strategy = 'ON_CHANGE', 
                variable_name = 'a'
            )
        else :
            return ModelProperty(
                name = '0',
                permission = 'READ_ONLY',
                type = 'ANALOG',
                update_strategy = 'ON_CHANGE',
        )

    def testModelProperty(self):
        """Test ModelProperty"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()