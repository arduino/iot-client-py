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

from iot_api_client.model.arduino_credentialsv1_collection import ArduinoCredentialsv1Collection
from iot_api_client.model.error import Error

# Query params


class ConnectionSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def WIFI(cls):
        return cls("wifi")
    
    @schemas.classproperty
    def ETH(cls):
        return cls("eth")
    
    @schemas.classproperty
    def WIFIANDSECRET(cls):
        return cls("wifiandsecret")
    
    @schemas.classproperty
    def GSM(cls):
        return cls("gsm")
    
    @schemas.classproperty
    def NB(cls):
        return cls("nb")
    
    @schemas.classproperty
    def LORA(cls):
        return cls("lora")
    
    @schemas.classproperty
    def CATM1(cls):
        return cls("catm1")
    
    @schemas.classproperty
    def CELLULAR(cls):
        return cls("cellular")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'connection': typing.Union[ConnectionSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_connection = api_client.QueryParameter(
    name="connection",
    style=api_client.ParameterStyle.FORM,
    schema=ConnectionSchema,
    explode=True,
)
# Path params


class TypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def MKRWIFI1010(cls):
        return cls("mkrwifi1010")
    
    @schemas.classproperty
    def MKR1000(cls):
        return cls("mkr1000")
    
    @schemas.classproperty
    def NANO_33_IOT(cls):
        return cls("nano_33_iot")
    
    @schemas.classproperty
    def MKRGSM1400(cls):
        return cls("mkrgsm1400")
    
    @schemas.classproperty
    def MKRWAN1310(cls):
        return cls("mkrwan1310")
    
    @schemas.classproperty
    def MKRWAN1300(cls):
        return cls("mkrwan1300")
    
    @schemas.classproperty
    def MKRNB1500(cls):
        return cls("mkrnb1500")
    
    @schemas.classproperty
    def LORADEVICE(cls):
        return cls("lora-device")
    
    @schemas.classproperty
    def LOGIN_AND_SECRETKEY_WIFI(cls):
        return cls("login_and_secretkey_wifi")
    
    @schemas.classproperty
    def ENVIE_M7(cls):
        return cls("envie_m7")
    
    @schemas.classproperty
    def NANORP2040CONNECT(cls):
        return cls("nanorp2040connect")
    
    @schemas.classproperty
    def NICLA_VISION(cls):
        return cls("nicla_vision")
    
    @schemas.classproperty
    def OPTA(cls):
        return cls("opta")
    
    @schemas.classproperty
    def GIGA(cls):
        return cls("giga")
    
    @schemas.classproperty
    def PORTENTA_C33(cls):
        return cls("portenta_c33")
    
    @schemas.classproperty
    def UNOR4WIFI(cls):
        return cls("unor4wifi")
    
    @schemas.classproperty
    def NANO_NORA(cls):
        return cls("nano_nora")
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'type': typing.Union[TypeSchema, str, ],
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


request_path_type = api_client.PathParameter(
    name="type",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TypeSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationVndArduinoCredentialsv1jsonTypecollection = ArduinoCredentialsv1Collection
SchemaFor200ResponseBodyApplicationVndGoaErrorjson = ArduinoCredentialsv1Collection


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationVndArduinoCredentialsv1jsonTypecollection,
        SchemaFor200ResponseBodyApplicationVndGoaErrorjson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/vnd.arduino.credentialsv1+json; type=collection': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndArduinoCredentialsv1jsonTypecollection),
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndGoaErrorjson),
    },
)
SchemaFor401ResponseBodyApplicationVndArduinoCredentialsv1jsonTypecollection = Error
SchemaFor401ResponseBodyApplicationVndGoaErrorjson = Error


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor401ResponseBodyApplicationVndArduinoCredentialsv1jsonTypecollection,
        SchemaFor401ResponseBodyApplicationVndGoaErrorjson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    content={
        'application/vnd.arduino.credentialsv1+json; type=collection': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationVndArduinoCredentialsv1jsonTypecollection),
        'application/vnd.goa.error+json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationVndGoaErrorjson),
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
_all_accept_content_types = (
    'application/vnd.arduino.credentialsv1+json; type=collection',
    'application/vnd.goa.error+json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _network_credentials_v1_show_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _network_credentials_v1_show_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _network_credentials_v1_show_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _network_credentials_v1_show_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        show network_credentials_v1
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_type,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        prefix_separator_iterator = None
        for parameter in (
            request_query_connection,
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
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
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


class NetworkCredentialsV1Show(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def network_credentials_v1_show(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def network_credentials_v1_show(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def network_credentials_v1_show(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def network_credentials_v1_show(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._network_credentials_v1_show_oapg(
            query_params=query_params,
            path_params=path_params,
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
        path_params: RequestPathParams = frozendict.frozendict(),
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
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
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
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._network_credentials_v1_show_oapg(
            query_params=query_params,
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


