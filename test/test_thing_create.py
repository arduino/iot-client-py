# coding: utf-8

"""
    Arduino IoT Cloud API

    Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import iot_api_client
from iot_api_client.models.thing_create import ThingCreate  # noqa: E501
from iot_api_client.rest import ApiException

class TestThingCreate(unittest.TestCase):
    """ThingCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ThingCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ThingCreate`
        """
        model = iot_api_client.models.thing_create.ThingCreate()  # noqa: E501
        if include_optional :
            return ThingCreate(
                assistant = 'ALEXA', 
                device_id = '', 
                id = '', 
                name = '.', 
                properties = [
                    iot_api_client.models.property.property(
                        max_value = 1.337, 
                        min_value = 1.337, 
                        name = '', 
                        permission = 'READ_ONLY', 
                        persist = True, 
                        tag = 56, 
                        type = 'ANALOG', 
                        update_parameter = 1.337, 
                        update_strategy = 'ON_CHANGE', 
                        variable_name = 'MqXzyCBw3_uufVPIPFhB9JcGRYnua', )
                    ], 
                tags = [
                    iot_api_client.models.tag.tag(
                        key = '0', 
                        value = '0', )
                    ], 
                timezone = 'America/New_York', 
                webhook_active = True, 
                webhook_uri = ''
            )
        else :
            return ThingCreate(
        )
        """

    def testThingCreate(self):
        """Test ThingCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
