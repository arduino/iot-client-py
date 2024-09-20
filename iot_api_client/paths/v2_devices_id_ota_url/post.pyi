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

from iot_api_client.model.error import Error
from iot_api_client.model.devicev2_otaurlpyalod import Devicev2Otaurlpyalod

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
SchemaForRequestBodyApplicationJson = Devicev2Otaurlpyalod
SchemaForRequestBodyApplicationXWwwFormUrlencoded = Devicev2Otaurlpyalod


request_body_devicev2_otaurlpyalod = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
    required=True,
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
)


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
)
SchemaFor400ResponseBodyApplicationVndGoaErrorjson = Error
SchemaFor400ResponseBodyTextPlain = Error


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyApplicationVndGoaErrorjson,
        SchemaFor400ResponseBodyTextPlain,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndGoaErrorjson),
        'text/plain': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextPlain),
    },
)
SchemaFor401ResponseBodyApplicationVndGoaErrorjson = Error
SchemaFor401ResponseBodyTextPlain = Error


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor401ResponseBodyApplicationVndGoaErrorjson,
        SchemaFor401ResponseBodyTextPlain,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    content={
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationVndGoaErrorjson),
        'text/plain': api_client.MediaType(
            schema=SchemaFor401ResponseBodyTextPlain),
    },
)
SchemaFor404ResponseBodyApplicationVndGoaErrorjson = Error
SchemaFor404ResponseBodyTextPlain = Error


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor404ResponseBodyApplicationVndGoaErrorjson,
        SchemaFor404ResponseBodyTextPlain,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    content={
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationVndGoaErrorjson),
        'text/plain': api_client.MediaType(
            schema=SchemaFor404ResponseBodyTextPlain),
    },
)
SchemaFor410ResponseBodyApplicationVndGoaErrorjson = Error
SchemaFor410ResponseBodyTextPlain = Error


@dataclass
class ApiResponseFor410(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor410ResponseBodyApplicationVndGoaErrorjson,
        SchemaFor410ResponseBodyTextPlain,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_410 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor410,
    content={
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor410ResponseBodyApplicationVndGoaErrorjson),
        'text/plain': api_client.MediaType(
            schema=SchemaFor410ResponseBodyTextPlain),
    },
)
SchemaFor412ResponseBodyApplicationVndGoaErrorjson = Error
SchemaFor412ResponseBodyTextPlain = Error


@dataclass
class ApiResponseFor412(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor412ResponseBodyApplicationVndGoaErrorjson,
        SchemaFor412ResponseBodyTextPlain,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_412 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor412,
    content={
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor412ResponseBodyApplicationVndGoaErrorjson),
        'text/plain': api_client.MediaType(
            schema=SchemaFor412ResponseBodyTextPlain),
    },
)
SchemaFor500ResponseBodyApplicationVndGoaErrorjson = Error
SchemaFor500ResponseBodyTextPlain = Error


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor500ResponseBodyApplicationVndGoaErrorjson,
        SchemaFor500ResponseBodyTextPlain,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    content={
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationVndGoaErrorjson),
        'text/plain': api_client.MediaType(
            schema=SchemaFor500ResponseBodyTextPlain),
    },
)
_all_accept_content_types = (
    'application/vnd.goa.error+json',
    'text/plain',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _devices_v2_ota_url_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"] = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
    ]: ...

    @typing.overload
    def _devices_v2_ota_url_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: typing_extensions.Literal["application/x-www-form-urlencoded"],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
    ]: ...

    @typing.overload
    def _devices_v2_ota_url_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
    ]: ...


    @typing.overload
    def _devices_v2_ota_url_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _devices_v2_ota_url_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _devices_v2_ota_url_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = 'application/json',
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        url devices_v2_ota
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_devicev2_otaurlpyalod.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
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


class DevicesV2OtaUrl(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def devices_v2_ota_url(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"] = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
    ]: ...

    @typing.overload
    def devices_v2_ota_url(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: typing_extensions.Literal["application/x-www-form-urlencoded"],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
    ]: ...

    @typing.overload
    def devices_v2_ota_url(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
    ]: ...


    @typing.overload
    def devices_v2_ota_url(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def devices_v2_ota_url(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def devices_v2_ota_url(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = 'application/json',
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._devices_v2_ota_url_oapg(
            body=body,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"] = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
    ]: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: typing_extensions.Literal["application/x-www-form-urlencoded"],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
    ]: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
    ]: ...


    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = 'application/json',
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._devices_v2_ota_url_oapg(
            body=body,
            path_params=path_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


