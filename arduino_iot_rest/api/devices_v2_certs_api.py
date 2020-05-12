# coding: utf-8

"""
    Arduino IoT Cloud API

     Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from arduino_iot_rest.api_client import ApiClient
from arduino_iot_rest.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DevicesV2CertsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def devices_v2_certs_create(self, id, create_devices_v2_certs_payload, **kwargs):  # noqa: E501
        """create devices_v2_certs  # noqa: E501

        Creates a new cert associated to a device. The csr is signed and saved in database. The CommonName will be replaced with the device id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_v2_certs_create(id, create_devices_v2_certs_payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The id of the device (required)
        :param CreateDevicesV2CertsPayload create_devices_v2_certs_payload: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ArduinoDevicev2Cert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.devices_v2_certs_create_with_http_info(id, create_devices_v2_certs_payload, **kwargs)  # noqa: E501

    def devices_v2_certs_create_with_http_info(self, id, create_devices_v2_certs_payload, **kwargs):  # noqa: E501
        """create devices_v2_certs  # noqa: E501

        Creates a new cert associated to a device. The csr is signed and saved in database. The CommonName will be replaced with the device id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_v2_certs_create_with_http_info(id, create_devices_v2_certs_payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The id of the device (required)
        :param CreateDevicesV2CertsPayload create_devices_v2_certs_payload: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ArduinoDevicev2Cert, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id',
            'create_devices_v2_certs_payload'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method devices_v2_certs_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `devices_v2_certs_create`")  # noqa: E501
        # verify the required parameter 'create_devices_v2_certs_payload' is set
        if self.api_client.client_side_validation and ('create_devices_v2_certs_payload' not in local_var_params or  # noqa: E501
                                                        local_var_params['create_devices_v2_certs_payload'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `create_devices_v2_certs_payload` when calling `devices_v2_certs_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_devices_v2_certs_payload' in local_var_params:
            body_params = local_var_params['create_devices_v2_certs_payload']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v2/devices/{id}/certs', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArduinoDevicev2Cert',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def devices_v2_certs_delete(self, cid, id, **kwargs):  # noqa: E501
        """delete devices_v2_certs  # noqa: E501

        Removes a cert associated to a device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_v2_certs_delete(cid, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str cid: The id of the cert (required)
        :param str id: The id of the device (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.devices_v2_certs_delete_with_http_info(cid, id, **kwargs)  # noqa: E501

    def devices_v2_certs_delete_with_http_info(self, cid, id, **kwargs):  # noqa: E501
        """delete devices_v2_certs  # noqa: E501

        Removes a cert associated to a device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_v2_certs_delete_with_http_info(cid, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str cid: The id of the cert (required)
        :param str id: The id of the device (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'cid',
            'id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method devices_v2_certs_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cid' is set
        if self.api_client.client_side_validation and ('cid' not in local_var_params or  # noqa: E501
                                                        local_var_params['cid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cid` when calling `devices_v2_certs_delete`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `devices_v2_certs_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cid' in local_var_params:
            path_params['cid'] = local_var_params['cid']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v2/devices/{id}/certs/{cid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def devices_v2_certs_list(self, id, **kwargs):  # noqa: E501
        """list devices_v2_certs  # noqa: E501

        Returns the list of certs associated to the device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_v2_certs_list(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The id of the device (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[ArduinoDevicev2Cert]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.devices_v2_certs_list_with_http_info(id, **kwargs)  # noqa: E501

    def devices_v2_certs_list_with_http_info(self, id, **kwargs):  # noqa: E501
        """list devices_v2_certs  # noqa: E501

        Returns the list of certs associated to the device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_v2_certs_list_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The id of the device (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ArduinoDevicev2Cert], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method devices_v2_certs_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `devices_v2_certs_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v2/devices/{id}/certs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ArduinoDevicev2Cert]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def devices_v2_certs_show(self, cid, id, **kwargs):  # noqa: E501
        """show devices_v2_certs  # noqa: E501

        Returns the cert requested by the user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_v2_certs_show(cid, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str cid: The id of the cert (required)
        :param str id: The id of the device (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ArduinoDevicev2Cert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.devices_v2_certs_show_with_http_info(cid, id, **kwargs)  # noqa: E501

    def devices_v2_certs_show_with_http_info(self, cid, id, **kwargs):  # noqa: E501
        """show devices_v2_certs  # noqa: E501

        Returns the cert requested by the user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_v2_certs_show_with_http_info(cid, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str cid: The id of the cert (required)
        :param str id: The id of the device (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ArduinoDevicev2Cert, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'cid',
            'id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method devices_v2_certs_show" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cid' is set
        if self.api_client.client_side_validation and ('cid' not in local_var_params or  # noqa: E501
                                                        local_var_params['cid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cid` when calling `devices_v2_certs_show`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `devices_v2_certs_show`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cid' in local_var_params:
            path_params['cid'] = local_var_params['cid']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v2/devices/{id}/certs/{cid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArduinoDevicev2Cert',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def devices_v2_certs_update(self, cid, id, devicev2_cert, **kwargs):  # noqa: E501
        """update devices_v2_certs  # noqa: E501

        Updates a cert associated to a device. The csr is signed and saved in database. The CommonName will be replaced with the device id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_v2_certs_update(cid, id, devicev2_cert, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str cid: The id of the cert (required)
        :param str id: The id of the device (required)
        :param Devicev2Cert devicev2_cert: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ArduinoDevicev2Cert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.devices_v2_certs_update_with_http_info(cid, id, devicev2_cert, **kwargs)  # noqa: E501

    def devices_v2_certs_update_with_http_info(self, cid, id, devicev2_cert, **kwargs):  # noqa: E501
        """update devices_v2_certs  # noqa: E501

        Updates a cert associated to a device. The csr is signed and saved in database. The CommonName will be replaced with the device id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_v2_certs_update_with_http_info(cid, id, devicev2_cert, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str cid: The id of the cert (required)
        :param str id: The id of the device (required)
        :param Devicev2Cert devicev2_cert: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ArduinoDevicev2Cert, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'cid',
            'id',
            'devicev2_cert'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method devices_v2_certs_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cid' is set
        if self.api_client.client_side_validation and ('cid' not in local_var_params or  # noqa: E501
                                                        local_var_params['cid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cid` when calling `devices_v2_certs_update`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `devices_v2_certs_update`")  # noqa: E501
        # verify the required parameter 'devicev2_cert' is set
        if self.api_client.client_side_validation and ('devicev2_cert' not in local_var_params or  # noqa: E501
                                                        local_var_params['devicev2_cert'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `devicev2_cert` when calling `devices_v2_certs_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cid' in local_var_params:
            path_params['cid'] = local_var_params['cid']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'devicev2_cert' in local_var_params:
            body_params = local_var_params['devicev2_cert']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v2/devices/{id}/certs/{cid}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArduinoDevicev2Cert',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
