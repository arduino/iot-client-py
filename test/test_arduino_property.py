# coding: utf-8

"""
    Arduino IoT Cloud API

    Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iot_api_client.models.arduino_property import ArduinoProperty

class TestArduinoProperty(unittest.TestCase):
    """ArduinoProperty unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArduinoProperty:
        """Test ArduinoProperty
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArduinoProperty`
        """
        model = ArduinoProperty()
        if include_optional:
            return ArduinoProperty(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                href = '',
                id = '',
                last_value = None,
                linked_to_trigger = True,
                max_value = 1.337,
                min_value = 1.337,
                name = '',
                permission = '',
                persist = True,
                sync_id = '',
                tag = 56,
                thing_id = '',
                thing_name = '',
                type = '',
                update_parameter = 1.337,
                update_strategy = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                value_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                variable_name = ''
            )
        else:
            return ArduinoProperty(
                href = '',
                id = '',
                name = '',
                permission = '',
                thing_id = '',
                type = '',
                update_strategy = '',
        )
        """

    def testArduinoProperty(self):
        """Test ArduinoProperty"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
