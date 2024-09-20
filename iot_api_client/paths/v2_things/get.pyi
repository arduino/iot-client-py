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
from iot_api_client.model.arduino_thing_collection import ArduinoThingCollection

# Query params
AcrossUserIdsSchema = schemas.BoolSchema
DeviceIdSchema = schemas.StrSchema


class IdsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IdsSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
ShowDeletedSchema = schemas.BoolSchema
ShowPropertiesSchema = schemas.BoolSchema


class TagsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.StrSchema
        ):
            pass

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TagsSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'across_user_ids': typing.Union[AcrossUserIdsSchema, bool, ],
        'device_id': typing.Union[DeviceIdSchema, str, ],
        'ids': typing.Union[IdsSchema, list, tuple, ],
        'show_deleted': typing.Union[ShowDeletedSchema, bool, ],
        'show_properties': typing.Union[ShowPropertiesSchema, bool, ],
        'tags': typing.Union[TagsSchema, list, tuple, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_across_user_ids = api_client.QueryParameter(
    name="across_user_ids",
    style=api_client.ParameterStyle.FORM,
    schema=AcrossUserIdsSchema,
    explode=True,
)
request_query_device_id = api_client.QueryParameter(
    name="device_id",
    style=api_client.ParameterStyle.FORM,
    schema=DeviceIdSchema,
    explode=True,
)
request_query_ids = api_client.QueryParameter(
    name="ids",
    style=api_client.ParameterStyle.FORM,
    schema=IdsSchema,
    explode=True,
)
request_query_show_deleted = api_client.QueryParameter(
    name="show_deleted",
    style=api_client.ParameterStyle.FORM,
    schema=ShowDeletedSchema,
    explode=True,
)
request_query_show_properties = api_client.QueryParameter(
    name="show_properties",
    style=api_client.ParameterStyle.FORM,
    schema=ShowPropertiesSchema,
    explode=True,
)
request_query_tags = api_client.QueryParameter(
    name="tags",
    style=api_client.ParameterStyle.FORM,
    schema=TagsSchema,
    explode=True,
)
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
SchemaFor200ResponseBodyApplicationVndArduinoThingjsonTypecollection = ArduinoThingCollection
SchemaFor200ResponseBodyApplicationVndGoaErrorjson = ArduinoThingCollection


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationVndArduinoThingjsonTypecollection,
        SchemaFor200ResponseBodyApplicationVndGoaErrorjson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/vnd.arduino.thing+json; type=collection': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndArduinoThingjsonTypecollection),
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndGoaErrorjson),
    },
)
SchemaFor400ResponseBodyApplicationVndArduinoThingjsonTypecollection = Error
SchemaFor400ResponseBodyApplicationVndGoaErrorjson = Error


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyApplicationVndArduinoThingjsonTypecollection,
        SchemaFor400ResponseBodyApplicationVndGoaErrorjson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'application/vnd.arduino.thing+json; type=collection': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndArduinoThingjsonTypecollection),
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndGoaErrorjson),
    },
)
SchemaFor401ResponseBodyApplicationVndArduinoThingjsonTypecollection = Error
SchemaFor401ResponseBodyApplicationVndGoaErrorjson = Error


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor401ResponseBodyApplicationVndArduinoThingjsonTypecollection,
        SchemaFor401ResponseBodyApplicationVndGoaErrorjson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    content={
        'application/vnd.arduino.thing+json; type=collection': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationVndArduinoThingjsonTypecollection),
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationVndGoaErrorjson),
    },
)
SchemaFor403ResponseBodyApplicationVndArduinoThingjsonTypecollection = Error
SchemaFor403ResponseBodyApplicationVndGoaErrorjson = Error


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor403ResponseBodyApplicationVndArduinoThingjsonTypecollection,
        SchemaFor403ResponseBodyApplicationVndGoaErrorjson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    content={
        'application/vnd.arduino.thing+json; type=collection': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndArduinoThingjsonTypecollection),
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndGoaErrorjson),
    },
)
SchemaFor500ResponseBodyApplicationVndArduinoThingjsonTypecollection = Error
SchemaFor500ResponseBodyApplicationVndGoaErrorjson = Error


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor500ResponseBodyApplicationVndArduinoThingjsonTypecollection,
        SchemaFor500ResponseBodyApplicationVndGoaErrorjson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    content={
        'application/vnd.arduino.thing+json; type=collection': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationVndArduinoThingjsonTypecollection),
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationVndGoaErrorjson),
    },
)
_all_accept_content_types = (
    'application/vnd.arduino.thing+json; type=collection',
    'application/vnd.goa.error+json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _things_v2_list_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _things_v2_list_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _things_v2_list_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _things_v2_list_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        list things_v2
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_across_user_ids,
            request_query_device_id,
            request_query_ids,
            request_query_show_deleted,
            request_query_show_properties,
            request_query_tags,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

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

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
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


class ThingsV2List(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def things_v2_list(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def things_v2_list(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def things_v2_list(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def things_v2_list(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._things_v2_list_oapg(
            query_params=query_params,
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._things_v2_list_oapg(
            query_params=query_params,
            header_params=header_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


