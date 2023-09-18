# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import iot_api_client
from iot_api_client.paths.v2_devices_id_certs_cid import delete  # noqa: E501
from iot_api_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2DevicesIdCertsCid(ApiTestMixin, unittest.TestCase):
    """
    V2DevicesIdCertsCid unit test stubs
        delete devices_v2_certs  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
