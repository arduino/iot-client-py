# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import iot_api_client
from iot_api_client.paths.v2_things_id_tags import get  # noqa: E501
from iot_api_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2ThingsIdTags(ApiTestMixin, unittest.TestCase):
    """
    V2ThingsIdTags unit test stubs
        list things_v2_tags  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
