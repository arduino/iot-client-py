# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import iot_api_client
from iot_api_client.paths.v2_series_batch_query_raw_lastvalue import post  # noqa: E501
from iot_api_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2SeriesBatchQueryRawLastvalue(ApiTestMixin, unittest.TestCase):
    """
    V2SeriesBatchQueryRawLastvalue unit test stubs
        batch_query_raw_last_value series_v2  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200








if __name__ == '__main__':
    unittest.main()
