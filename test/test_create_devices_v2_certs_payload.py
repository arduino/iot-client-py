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
from iot_api_client.models.create_devices_v2_certs_payload import CreateDevicesV2CertsPayload  # noqa: E501
from iot_api_client.rest import ApiException

class TestCreateDevicesV2CertsPayload(unittest.TestCase):
    """CreateDevicesV2CertsPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateDevicesV2CertsPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateDevicesV2CertsPayload`
        """
        model = iot_api_client.models.create_devices_v2_certs_payload.CreateDevicesV2CertsPayload()  # noqa: E501
        if include_optional :
            return CreateDevicesV2CertsPayload(
                ca = '', 
                csr = '-----BEGIN CERTIFICATE-----
			MIIBeDCCAR4CAQAwgY0xCzAJBgNVBAYTAkFVMRMwEQYDVQQIEwpTb21lLVN0YXRl
			MQ8wDQYDVQQHEwZNeUNpdHkxFDASBgNVBAoTC0NvbXBhbnkgTHRkMQswCQYDVQQL
			EwJJVDEUMBIGA1UEAxMLZXhhbXBsZS5jb20xHzAdBgkqhkiG9w0BCQEMEHRlc3RA
			ZXhhbXBsZS5jb20wWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATf6J9Gk79XGJ2I
			+v6p/r0UmPufUcUwtlx7gx87+DaI8Vpj9R5KN71HsHYw5uq+Lm0cr0CZIdtZU4cP
			upd6jDQToC4wLAYJKoZIhvcNAQkOMR8wHTAbBgNVHREEFDASgRB0ZXN0QGV4YW1w
			bGUuY29tMAoGCCqGSM49BAMCA0gAMEUCIGQqtlGzYdjPwYZYJ41albMBcdrKI7+8
			oiNSNWyDxJSGAiEAqQPPxMdr6vaXCCjr5s1J01WLKHzGoPFCR40rqAPs8eQ=
			-----END CERTIFICATE-----
			', 
                enabled = True
            )
        else :
            return CreateDevicesV2CertsPayload(
                csr = '-----BEGIN CERTIFICATE-----
			MIIBeDCCAR4CAQAwgY0xCzAJBgNVBAYTAkFVMRMwEQYDVQQIEwpTb21lLVN0YXRl
			MQ8wDQYDVQQHEwZNeUNpdHkxFDASBgNVBAoTC0NvbXBhbnkgTHRkMQswCQYDVQQL
			EwJJVDEUMBIGA1UEAxMLZXhhbXBsZS5jb20xHzAdBgkqhkiG9w0BCQEMEHRlc3RA
			ZXhhbXBsZS5jb20wWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATf6J9Gk79XGJ2I
			+v6p/r0UmPufUcUwtlx7gx87+DaI8Vpj9R5KN71HsHYw5uq+Lm0cr0CZIdtZU4cP
			upd6jDQToC4wLAYJKoZIhvcNAQkOMR8wHTAbBgNVHREEFDASgRB0ZXN0QGV4YW1w
			bGUuY29tMAoGCCqGSM49BAMCA0gAMEUCIGQqtlGzYdjPwYZYJ41albMBcdrKI7+8
			oiNSNWyDxJSGAiEAqQPPxMdr6vaXCCjr5s1J01WLKHzGoPFCR40rqAPs8eQ=
			-----END CERTIFICATE-----
			',
                enabled = True,
        )
        """

    def testCreateDevicesV2CertsPayload(self):
        """Test CreateDevicesV2CertsPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
