# coding: utf-8

"""
    Arduino IoT Cloud API

    Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iot_api_client.models.update_action import UpdateAction

class TestUpdateAction(unittest.TestCase):
    """UpdateAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateAction:
        """Test UpdateAction
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateAction`
        """
        model = UpdateAction()
        if include_optional:
            return UpdateAction(
                description = '',
                email = iot_api_client.models.email_action.email_action(
                    body = iot_api_client.models.body_expression.body_expression(
                        expression = '', 
                        variables = [
                            iot_api_client.models.variable.variable(
                                attribute = 'PROPERTY', 
                                entity = 'PROPERTY', 
                                id = '', 
                                placeholder = '', 
                                property_id = '', 
                                thing_id = '', )
                            ], ), 
                    delivery = iot_api_client.models.email_delivery_opts.email_delivery_opts(
                        bcc = [
                            iot_api_client.models.user_recipient.user_recipient(
                                email = '', 
                                id = '', 
                                username = '', )
                            ], 
                        cc = [
                            iot_api_client.models.user_recipient.user_recipient(
                                email = '', 
                                id = '', 
                                username = '', )
                            ], 
                        to = [
                            
                            ], ), 
                    subject = iot_api_client.models.title_expression.title_expression(
                        expression = '', ), ),
                name = '',
                push_notification = iot_api_client.models.push_action.push_action(
                    body = iot_api_client.models.body_expression.body_expression(
                        expression = '', 
                        variables = [
                            iot_api_client.models.variable.variable(
                                attribute = 'PROPERTY', 
                                entity = 'PROPERTY', 
                                id = '', 
                                placeholder = '', 
                                property_id = '', 
                                thing_id = '', )
                            ], ), 
                    delivery = iot_api_client.models.push_delivery_opts.push_delivery_opts(
                        to = [
                            iot_api_client.models.user_recipient.user_recipient(
                                email = '', 
                                id = '', 
                                username = '', )
                            ], ), 
                    title = iot_api_client.models.title_expression.title_expression(
                        expression = '', ), ),
                trigger_id = ''
            )
        else:
            return UpdateAction(
        )
        """

    def testUpdateAction(self):
        """Test UpdateAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
