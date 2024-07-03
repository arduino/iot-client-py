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


class ArduinoTemplateproperty(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ArduinoTemplateproperty media type (default view)
    """


    class MetaOapg:
        required = {
            "update_strategy",
            "name",
            "permission",
            "type",
        }
        
        class properties:
            name = schemas.StrSchema
            permission = schemas.StrSchema
            type = schemas.StrSchema
            update_strategy = schemas.StrSchema
            id = schemas.StrSchema
            update_parameter = schemas.Float64Schema
            variable_name = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "permission": permission,
                "type": type,
                "update_strategy": update_strategy,
                "id": id,
                "update_parameter": update_parameter,
                "variable_name": variable_name,
            }
    
    update_strategy: MetaOapg.properties.update_strategy
    name: MetaOapg.properties.name
    permission: MetaOapg.properties.permission
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permission"]) -> MetaOapg.properties.permission: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_strategy"]) -> MetaOapg.properties.update_strategy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_parameter"]) -> MetaOapg.properties.update_parameter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variable_name"]) -> MetaOapg.properties.variable_name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "permission", "type", "update_strategy", "id", "update_parameter", "variable_name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permission"]) -> MetaOapg.properties.permission: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_strategy"]) -> MetaOapg.properties.update_strategy: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_parameter"]) -> typing.Union[MetaOapg.properties.update_parameter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variable_name"]) -> typing.Union[MetaOapg.properties.variable_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "permission", "type", "update_strategy", "id", "update_parameter", "variable_name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        update_strategy: typing.Union[MetaOapg.properties.update_strategy, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        permission: typing.Union[MetaOapg.properties.permission, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        update_parameter: typing.Union[MetaOapg.properties.update_parameter, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        variable_name: typing.Union[MetaOapg.properties.variable_name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ArduinoTemplateproperty':
        return super().__new__(
            cls,
            *_args,
            update_strategy=update_strategy,
            name=name,
            permission=permission,
            type=type,
            id=id,
            update_parameter=update_parameter,
            variable_name=variable_name,
            _configuration=_configuration,
            **kwargs,
        )
