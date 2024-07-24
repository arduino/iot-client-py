# coding: utf-8

"""
    Arduino IoT Cloud API

     Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

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


class ArduinoSeriesBatchSampled(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ArduinoSeriesBatchSampled media type (default view)
    """


    class MetaOapg:
        required = {
            "resp_version",
            "responses",
        }
        
        class properties:
            resp_version = schemas.Int64Schema
            
            
            class responses(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ArduinoSeriesSampledResponse']:
                        return ArduinoSeriesSampledResponse
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ArduinoSeriesSampledResponse'], typing.List['ArduinoSeriesSampledResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'responses':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ArduinoSeriesSampledResponse':
                    return super().__getitem__(i)
            __annotations__ = {
                "resp_version": resp_version,
                "responses": responses,
            }
    
    resp_version: MetaOapg.properties.resp_version
    responses: MetaOapg.properties.responses
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resp_version"]) -> MetaOapg.properties.resp_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["responses"]) -> MetaOapg.properties.responses: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resp_version", "responses", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resp_version"]) -> MetaOapg.properties.resp_version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["responses"]) -> MetaOapg.properties.responses: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resp_version", "responses", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        resp_version: typing.Union[MetaOapg.properties.resp_version, decimal.Decimal, int, ],
        responses: typing.Union[MetaOapg.properties.responses, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ArduinoSeriesBatchSampled':
        return super().__new__(
            cls,
            *_args,
            resp_version=resp_version,
            responses=responses,
            _configuration=_configuration,
            **kwargs,
        )

from iot_api_client.model.arduino_series_sampled_response import ArduinoSeriesSampledResponse
