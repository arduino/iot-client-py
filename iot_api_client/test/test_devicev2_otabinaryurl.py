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
from iot_api_client.models.devicev2_otabinaryurl import Devicev2Otabinaryurl  # noqa: E501
from iot_api_client.rest import ApiException

class TestDevicev2Otabinaryurl(unittest.TestCase):
    """Devicev2Otabinaryurl unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Devicev2Otabinaryurl
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = iot_api_client.models.devicev2_otabinaryurl.Devicev2Otabinaryurl()  # noqa: E501
        if include_optional :
            return Devicev2Otabinaryurl(
                _async = True, 
                binary_key = 'a', 
                expire_in_mins = 56
            )
        else :
            return Devicev2Otabinaryurl(
                binary_key = 'a',
        )

    def testDevicev2Otabinaryurl(self):
        """Test Devicev2Otabinaryurl"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
