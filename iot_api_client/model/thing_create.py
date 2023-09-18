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


class ThingCreate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Payload to create a new thing
    """


    class MetaOapg:
        
        class properties:
            device_id = schemas.UUIDSchema
            id = schemas.UUIDSchema
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
                    regex=[{
                        'pattern': r'^[a-zA-Z0-9_.@ -]+$',  # noqa: E501
                    }]
            
            
            class properties(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ModelProperty']:
                        return ModelProperty
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ModelProperty'], typing.List['ModelProperty']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'properties':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ModelProperty':
                    return super().__getitem__(i)
            timezone = schemas.StrSchema
            webhook_active = schemas.BoolSchema
            webhook_uri = schemas.StrSchema
            __annotations__ = {
                "device_id": device_id,
                "id": id,
                "name": name,
                "properties": properties,
                "timezone": timezone,
                "webhook_active": webhook_active,
                "webhook_uri": webhook_uri,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_id"]) -> MetaOapg.properties.device_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["properties"]) -> MetaOapg.properties.properties: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_active"]) -> MetaOapg.properties.webhook_active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_uri"]) -> MetaOapg.properties.webhook_uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["device_id", "id", "name", "properties", "timezone", "webhook_active", "webhook_uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_id"]) -> typing.Union[MetaOapg.properties.device_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["properties"]) -> typing.Union[MetaOapg.properties.properties, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> typing.Union[MetaOapg.properties.timezone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_active"]) -> typing.Union[MetaOapg.properties.webhook_active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_uri"]) -> typing.Union[MetaOapg.properties.webhook_uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["device_id", "id", "name", "properties", "timezone", "webhook_active", "webhook_uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        device_id: typing.Union[MetaOapg.properties.device_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        properties: typing.Union[MetaOapg.properties.properties, list, tuple, schemas.Unset] = schemas.unset,
        timezone: typing.Union[MetaOapg.properties.timezone, str, schemas.Unset] = schemas.unset,
        webhook_active: typing.Union[MetaOapg.properties.webhook_active, bool, schemas.Unset] = schemas.unset,
        webhook_uri: typing.Union[MetaOapg.properties.webhook_uri, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ThingCreate':
        return super().__new__(
            cls,
            *_args,
            device_id=device_id,
            id=id,
            name=name,
            properties=properties,
            timezone=timezone,
            webhook_active=webhook_active,
            webhook_uri=webhook_uri,
            _configuration=_configuration,
            **kwargs,
        )

from iot_api_client.model.model_property import ModelProperty
