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
from iot_api_client.models.arduino_dashboardv2template import ArduinoDashboardv2template  # noqa: E501
from iot_api_client.rest import ApiException

class TestArduinoDashboardv2template(unittest.TestCase):
    """ArduinoDashboardv2template unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ArduinoDashboardv2template
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArduinoDashboardv2template`
        """
        model = iot_api_client.models.arduino_dashboardv2template.ArduinoDashboardv2template()  # noqa: E501
        if include_optional :
            return ArduinoDashboardv2template(
                cover_image = '', 
                id = '', 
                name = '', 
                widgets = [
                    iot_api_client.models.mediatype_identifier:_application/vnd/arduino/widgetv2template+json;_view=default.Mediatype identifier: application/vnd.arduino.widgetv2template+json; view=default(
                        height = 56, 
                        height_mobile = 56, 
                        name = '', 
                        options = { }, 
                        type = '', 
                        variables = [
                            iot_api_client.models.mediatype_identifier:_application/vnd/arduino/templatevariable+json;_view=default.Mediatype identifier: application/vnd.arduino.templatevariable+json; view=default(
                                name = '', 
                                permission = '', 
                                thing_id = '', 
                                thing_timezone = iot_api_client.models.mediatype_identifier:_application/vnd/arduino/timezone+json;_view=default.Mediatype identifier: application/vnd.arduino.timezone+json; view=default(
                                    name = '', 
                                    offset = 56, 
                                    until = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                type = '', 
                                variable_id = '', )
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
            return ArduinoDashboardv2template(
                name = '',
        )
        """

    def testArduinoDashboardv2template(self):
        """Test ArduinoDashboardv2template"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
