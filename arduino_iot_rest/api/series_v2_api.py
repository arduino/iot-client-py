# coding: utf-8

"""
    Iot API

    Collection of all public API endpoints.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from arduino_iot_rest.api_client import ApiClient
from arduino_iot_rest.exceptions import (
    ApiTypeError,
    ApiValueError
)


class SeriesV2Api(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def series_v2_batch_query(self, batch_query_requests_media_v1, **kwargs):  # noqa: E501
        """batch_query series_v2  # noqa: E501

        Returns the batch of time-series data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.series_v2_batch_query(batch_query_requests_media_v1, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchQueryRequestsMediaV1 batch_query_requests_media_v1: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ArduinoSeriesBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.series_v2_batch_query_with_http_info(batch_query_requests_media_v1, **kwargs)  # noqa: E501

    def series_v2_batch_query_with_http_info(self, batch_query_requests_media_v1, **kwargs):  # noqa: E501
        """batch_query series_v2  # noqa: E501

        Returns the batch of time-series data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.series_v2_batch_query_with_http_info(batch_query_requests_media_v1, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchQueryRequestsMediaV1 batch_query_requests_media_v1: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ArduinoSeriesBatch, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['batch_query_requests_media_v1']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method series_v2_batch_query" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'batch_query_requests_media_v1' is set
        if ('batch_query_requests_media_v1' not in local_var_params or
                local_var_params['batch_query_requests_media_v1'] is None):
            raise ApiValueError("Missing the required parameter `batch_query_requests_media_v1` when calling `series_v2_batch_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'batch_query_requests_media_v1' in local_var_params:
            body_params = local_var_params['batch_query_requests_media_v1']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.arduino.series.batch+json', 'application/vnd.goa.error+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v2/series/batch_query', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArduinoSeriesBatch',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def series_v2_batch_query_raw(self, batch_query_raw_requests_media_v1, **kwargs):  # noqa: E501
        """batch_query_raw series_v2  # noqa: E501

        Returns the batch of time-series data raw  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.series_v2_batch_query_raw(batch_query_raw_requests_media_v1, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchQueryRawRequestsMediaV1 batch_query_raw_requests_media_v1: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ArduinoSeriesRawBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.series_v2_batch_query_raw_with_http_info(batch_query_raw_requests_media_v1, **kwargs)  # noqa: E501

    def series_v2_batch_query_raw_with_http_info(self, batch_query_raw_requests_media_v1, **kwargs):  # noqa: E501
        """batch_query_raw series_v2  # noqa: E501

        Returns the batch of time-series data raw  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.series_v2_batch_query_raw_with_http_info(batch_query_raw_requests_media_v1, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchQueryRawRequestsMediaV1 batch_query_raw_requests_media_v1: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ArduinoSeriesRawBatch, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['batch_query_raw_requests_media_v1']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method series_v2_batch_query_raw" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'batch_query_raw_requests_media_v1' is set
        if ('batch_query_raw_requests_media_v1' not in local_var_params or
                local_var_params['batch_query_raw_requests_media_v1'] is None):
            raise ApiValueError("Missing the required parameter `batch_query_raw_requests_media_v1` when calling `series_v2_batch_query_raw`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'batch_query_raw_requests_media_v1' in local_var_params:
            body_params = local_var_params['batch_query_raw_requests_media_v1']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.arduino.series.raw.batch+json', 'application/vnd.goa.error+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v2/series/batch_query_raw', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArduinoSeriesRawBatch',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def series_v2_batch_query_raw_last_value(self, batch_last_value_requests_media_v1, **kwargs):  # noqa: E501
        """batch_query_raw_last_value series_v2  # noqa: E501

        Returns the batch of time-series data raw  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.series_v2_batch_query_raw_last_value(batch_last_value_requests_media_v1, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchLastValueRequestsMediaV1 batch_last_value_requests_media_v1: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ArduinoSeriesRawBatchLastvalue
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.series_v2_batch_query_raw_last_value_with_http_info(batch_last_value_requests_media_v1, **kwargs)  # noqa: E501

    def series_v2_batch_query_raw_last_value_with_http_info(self, batch_last_value_requests_media_v1, **kwargs):  # noqa: E501
        """batch_query_raw_last_value series_v2  # noqa: E501

        Returns the batch of time-series data raw  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.series_v2_batch_query_raw_last_value_with_http_info(batch_last_value_requests_media_v1, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchLastValueRequestsMediaV1 batch_last_value_requests_media_v1: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ArduinoSeriesRawBatchLastvalue, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['batch_last_value_requests_media_v1']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method series_v2_batch_query_raw_last_value" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'batch_last_value_requests_media_v1' is set
        if ('batch_last_value_requests_media_v1' not in local_var_params or
                local_var_params['batch_last_value_requests_media_v1'] is None):
            raise ApiValueError("Missing the required parameter `batch_last_value_requests_media_v1` when calling `series_v2_batch_query_raw_last_value`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'batch_last_value_requests_media_v1' in local_var_params:
            body_params = local_var_params['batch_last_value_requests_media_v1']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.arduino.series.raw.batch.lastvalue+json', 'application/vnd.goa.error+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v2/series/batch_query_raw/lastvalue', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArduinoSeriesRawBatchLastvalue',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
