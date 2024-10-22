# coding: utf-8

"""
    Arduino IoT Cloud API

    Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iot_api_client.models.arduino_thingtemplate import ArduinoThingtemplate

class TestArduinoThingtemplate(unittest.TestCase):
    """ArduinoThingtemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArduinoThingtemplate:
        """Test ArduinoThingtemplate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArduinoThingtemplate`
        """
        model = ArduinoThingtemplate()
        if include_optional:
            return ArduinoThingtemplate(
                device_metadata = iot_api_client.models.mediatype_identifier:_application/vnd/arduino/devicev2templatedevice+json;_view=default.Mediatype identifier: application/vnd.arduino.devicev2templatedevice+json; view=default(
                    fqbn = '', 
                    name = '', ),
                id = '',
                name = '',
                organization_id = '',
                sketch_template = '',
                tags = [
                    iot_api_client.models.tag.tag(
                        key = '0', 
                        value = '0', )
                    ],
                timezone = '',
                variables = [
                    iot_api_client.models.mediatype_identifier:_application/vnd/arduino/templateproperty+json;_view=default.Mediatype identifier: application/vnd.arduino.templateproperty+json; view=default(
                        id = '', 
                        name = '', 
                        permission = '', 
                        type = '', 
                        update_parameter = 1.337, 
                        update_strategy = '', 
                        variable_name = '', )
                    ],
                webhook_uri = ''
            )
        else:
            return ArduinoThingtemplate(
                name = '',
                timezone = '',
        )
        """

    def testArduinoThingtemplate(self):
        """Test ArduinoThingtemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
