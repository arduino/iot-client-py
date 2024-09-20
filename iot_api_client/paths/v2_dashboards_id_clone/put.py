# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from iot_api_client import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from iot_api_client import schemas  # noqa: F401

from iot_api_client.model.clone import Clone
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_dashboardv2 import ArduinoDashboardv2

from . import path

# Header params
XOrganizationSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'X-Organization': typing.Union[XOrganizationSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_organization = api_client.HeaderParameter(
    name="X-Organization",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XOrganizationSchema,
)
# Path params
IdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'id': typing.Union[IdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id = api_client.PathParameter(
    name="id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = Clone
SchemaForRequestBodyApplicationXWwwFormUrlencoded = Clone


request_body_clone = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
    required=True,
)
_auth = [
    'oauth2',
]
SchemaFor201ResponseBodyApplicationVndArduinoDashboardv2json = ArduinoDashboardv2
SchemaFor201ResponseBodyApplicationVndGoaErrorjson = ArduinoDashboardv2


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor201ResponseBodyApplicationVndArduinoDashboardv2json,
        SchemaFor201ResponseBodyApplicationVndGoaErrorjson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    content={
        'application/vnd.arduino.dashboardv2+json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationVndArduinoDashboardv2json),
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationVndGoaErrorjson),
    },
)
SchemaFor400ResponseBodyApplicationVndArduinoDashboardv2json = Error
SchemaFor400ResponseBodyApplicationVndGoaErrorjson = Error


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyApplicationVndArduinoDashboardv2json,
        SchemaFor400ResponseBodyApplicationVndGoaErrorjson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'application/vnd.arduino.dashboardv2+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndArduinoDashboardv2json),
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndGoaErrorjson),
    },
)
SchemaFor401ResponseBodyApplicationVndArduinoDashboardv2json = Error
SchemaFor401ResponseBodyApplicationVndGoaErrorjson = Error


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor401ResponseBodyApplicationVndArduinoDashboardv2json,
        SchemaFor401ResponseBodyApplicationVndGoaErrorjson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    content={
        'application/vnd.arduino.dashboardv2+json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationVndArduinoDashboardv2json),
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationVndGoaErrorjson),
    },
)
SchemaFor403ResponseBodyApplicationVndArduinoDashboardv2json = Error
SchemaFor403ResponseBodyApplicationVndGoaErrorjson = Error


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor403ResponseBodyApplicationVndArduinoDashboardv2json,
        SchemaFor403ResponseBodyApplicationVndGoaErrorjson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    content={
        'application/vnd.arduino.dashboardv2+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndArduinoDashboardv2json),
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndGoaErrorjson),
    },
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
)
SchemaFor500ResponseBodyApplicationVndArduinoDashboardv2json = Error
SchemaFor500ResponseBodyApplicationVndGoaErrorjson = Error


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor500ResponseBodyApplicationVndArduinoDashboardv2json,
        SchemaFor500ResponseBodyApplicationVndGoaErrorjson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    content={
        'application/vnd.arduino.dashboardv2+json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationVndArduinoDashboardv2json),
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationVndGoaErrorjson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/vnd.arduino.dashboardv2+json',
    'application/vnd.goa.error+json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _dashboards_v2_clone_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"] = ...,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor201,
    ]: ...

    @typing.overload
    def _dashboards_v2_clone_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: typing_extensions.Literal["application/x-www-form-urlencoded"],
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor201,
    ]: ...

    @typing.overload
    def _dashboards_v2_clone_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor201,
    ]: ...


    @typing.overload
    def _dashboards_v2_clone_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _dashboards_v2_clone_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _dashboards_v2_clone_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = 'application/json',
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        clone dashboards_v2
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_organization,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_clone.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='put'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class DashboardsV2Clone(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def dashboards_v2_clone(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"] = ...,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor201,
    ]: ...

    @typing.overload
    def dashboards_v2_clone(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: typing_extensions.Literal["application/x-www-form-urlencoded"],
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor201,
    ]: ...

    @typing.overload
    def dashboards_v2_clone(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor201,
    ]: ...


    @typing.overload
    def dashboards_v2_clone(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def dashboards_v2_clone(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def dashboards_v2_clone(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = 'application/json',
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._dashboards_v2_clone_oapg(
            body=body,
            header_params=header_params,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"] = ...,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor201,
    ]: ...

    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: typing_extensions.Literal["application/x-www-form-urlencoded"],
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor201,
    ]: ...

    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor201,
    ]: ...


    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = 'application/json',
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._dashboards_v2_clone_oapg(
            body=body,
            header_params=header_params,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


