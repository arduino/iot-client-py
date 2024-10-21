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
from iot_api_client.models.arduino_devicev2_cert import ArduinoDevicev2Cert  # noqa: E501
from iot_api_client.rest import ApiException

class TestArduinoDevicev2Cert(unittest.TestCase):
    """ArduinoDevicev2Cert unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ArduinoDevicev2Cert
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArduinoDevicev2Cert`
        """
        model = iot_api_client.models.arduino_devicev2_cert.ArduinoDevicev2Cert()  # noqa: E501
        if include_optional :
            return ArduinoDevicev2Cert(
                ca = '', 
                compressed = iot_api_client.models.mediatype_identifier:_application/vnd/arduino/compressedv2;_view=default.Mediatype identifier: application/vnd.arduino.compressedv2; view=default(
                    authority_key_identifier = '', 
                    not_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    not_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    serial = '', 
                    signature = '', 
                    signature_asn1_x = '', 
                    signature_asn1_y = '', ), 
                der = '', 
                device_id = '', 
                enabled = True, 
                href = '', 
                id = '', 
                pem = '-----BEGIN CERTIFICATE-----
			MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAryQICCl6NZ5gDKrnSztO
			3Hy8PEUcuyvg/ikC+VcIo2SFFSf18a3IMYldIugqqqZCs4/4uVW3sbdLs/6PfgdX
			7O9D22ZiFWHPYA2k2N744MNiCD1UE+tJyllUhSblK48bn+v1oZHCM0nYQ2NqUkvS
			j+hwUU3RiWl7x3D2s9wSdNt7XUtW05a/FXehsPSiJfKvHJJnGOX0BgTvkLnkAOTd
			OrUZ/wK69Dzu4IvrN4vs9Nes8vbwPa/ddZEzGR0cQMt0JBkhk9kU/qwqUseP1QRJ
			5I1jR4g8aYPL/ke9K35PxZWuDp3U0UPAZ3PjFAh+5T+fc7gzCs9dPzSHloruU+gl
			FQIDAQAB
			-----END CERTIFICATE-----'
            )
        else :
            return ArduinoDevicev2Cert(
                compressed = iot_api_client.models.mediatype_identifier:_application/vnd/arduino/compressedv2;_view=default.Mediatype identifier: application/vnd.arduino.compressedv2; view=default(
                    authority_key_identifier = '', 
                    not_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    not_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    serial = '', 
                    signature = '', 
                    signature_asn1_x = '', 
                    signature_asn1_y = '', ),
                der = '',
                device_id = '',
                enabled = True,
                href = '',
                id = '',
                pem = '-----BEGIN CERTIFICATE-----
			MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAryQICCl6NZ5gDKrnSztO
			3Hy8PEUcuyvg/ikC+VcIo2SFFSf18a3IMYldIugqqqZCs4/4uVW3sbdLs/6PfgdX
			7O9D22ZiFWHPYA2k2N744MNiCD1UE+tJyllUhSblK48bn+v1oZHCM0nYQ2NqUkvS
			j+hwUU3RiWl7x3D2s9wSdNt7XUtW05a/FXehsPSiJfKvHJJnGOX0BgTvkLnkAOTd
			OrUZ/wK69Dzu4IvrN4vs9Nes8vbwPa/ddZEzGR0cQMt0JBkhk9kU/qwqUseP1QRJ
			5I1jR4g8aYPL/ke9K35PxZWuDp3U0UPAZ3PjFAh+5T+fc7gzCs9dPzSHloruU+gl
			FQIDAQAB
			-----END CERTIFICATE-----',
        )
        """

    def testArduinoDevicev2Cert(self):
        """Test ArduinoDevicev2Cert"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
