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


class ArduinoThing(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ArduinoThing media type (default view)
    """


    class MetaOapg:
        required = {
            "user_id",
            "timezone",
            "name",
            "href",
            "id",
        }
        
        class properties:
            href = schemas.StrSchema
            id = schemas.UUIDSchema
            name = schemas.StrSchema
            timezone = schemas.StrSchema
            user_id = schemas.UUIDSchema
            
            
            class assistant(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ALEXA(cls):
                    return cls("ALEXA")
                
                @schemas.classproperty
                def GOOGLE(cls):
                    return cls("GOOGLE")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("NONE")
            created_at = schemas.DateTimeSchema
            deleted_at = schemas.DateTimeSchema
            device_fqbn = schemas.StrSchema
            device_id = schemas.UUIDSchema
            device_name = schemas.StrSchema
            device_type = schemas.StrSchema
            organization_id = schemas.UUIDSchema
        
            @staticmethod
            def properties() -> typing.Type['ArduinoPropertyCollection']:
                return ArduinoPropertyCollection
            properties_count = schemas.Int64Schema
            sketch_id = schemas.UUIDSchema
            
            
            class tags(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.AnyTypeSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            updated_at = schemas.DateTimeSchema
            webhook_active = schemas.BoolSchema
            webhook_uri = schemas.StrSchema
            __annotations__ = {
                "href": href,
                "id": id,
                "name": name,
                "timezone": timezone,
                "user_id": user_id,
                "assistant": assistant,
                "created_at": created_at,
                "deleted_at": deleted_at,
                "device_fqbn": device_fqbn,
                "device_id": device_id,
                "device_name": device_name,
                "device_type": device_type,
                "organization_id": organization_id,
                "properties": properties,
                "properties_count": properties_count,
                "sketch_id": sketch_id,
                "tags": tags,
                "updated_at": updated_at,
                "webhook_active": webhook_active,
                "webhook_uri": webhook_uri,
            }
    
    user_id: MetaOapg.properties.user_id
    timezone: MetaOapg.properties.timezone
    name: MetaOapg.properties.name
    href: MetaOapg.properties.href
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assistant"]) -> MetaOapg.properties.assistant: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted_at"]) -> MetaOapg.properties.deleted_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_fqbn"]) -> MetaOapg.properties.device_fqbn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_id"]) -> MetaOapg.properties.device_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_name"]) -> MetaOapg.properties.device_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_type"]) -> MetaOapg.properties.device_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization_id"]) -> MetaOapg.properties.organization_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["properties"]) -> 'ArduinoPropertyCollection': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["properties_count"]) -> MetaOapg.properties.properties_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sketch_id"]) -> MetaOapg.properties.sketch_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_active"]) -> MetaOapg.properties.webhook_active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_uri"]) -> MetaOapg.properties.webhook_uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["href", "id", "name", "timezone", "user_id", "assistant", "created_at", "deleted_at", "device_fqbn", "device_id", "device_name", "device_type", "organization_id", "properties", "properties_count", "sketch_id", "tags", "updated_at", "webhook_active", "webhook_uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assistant"]) -> typing.Union[MetaOapg.properties.assistant, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted_at"]) -> typing.Union[MetaOapg.properties.deleted_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_fqbn"]) -> typing.Union[MetaOapg.properties.device_fqbn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_id"]) -> typing.Union[MetaOapg.properties.device_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_name"]) -> typing.Union[MetaOapg.properties.device_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_type"]) -> typing.Union[MetaOapg.properties.device_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization_id"]) -> typing.Union[MetaOapg.properties.organization_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["properties"]) -> typing.Union['ArduinoPropertyCollection', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["properties_count"]) -> typing.Union[MetaOapg.properties.properties_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sketch_id"]) -> typing.Union[MetaOapg.properties.sketch_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_active"]) -> typing.Union[MetaOapg.properties.webhook_active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_uri"]) -> typing.Union[MetaOapg.properties.webhook_uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["href", "id", "name", "timezone", "user_id", "assistant", "created_at", "deleted_at", "device_fqbn", "device_id", "device_name", "device_type", "organization_id", "properties", "properties_count", "sketch_id", "tags", "updated_at", "webhook_active", "webhook_uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        user_id: typing.Union[MetaOapg.properties.user_id, str, uuid.UUID, ],
        timezone: typing.Union[MetaOapg.properties.timezone, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        href: typing.Union[MetaOapg.properties.href, str, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        assistant: typing.Union[MetaOapg.properties.assistant, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        deleted_at: typing.Union[MetaOapg.properties.deleted_at, str, datetime, schemas.Unset] = schemas.unset,
        device_fqbn: typing.Union[MetaOapg.properties.device_fqbn, str, schemas.Unset] = schemas.unset,
        device_id: typing.Union[MetaOapg.properties.device_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        device_name: typing.Union[MetaOapg.properties.device_name, str, schemas.Unset] = schemas.unset,
        device_type: typing.Union[MetaOapg.properties.device_type, str, schemas.Unset] = schemas.unset,
        organization_id: typing.Union[MetaOapg.properties.organization_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        properties: typing.Union['ArduinoPropertyCollection', schemas.Unset] = schemas.unset,
        properties_count: typing.Union[MetaOapg.properties.properties_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sketch_id: typing.Union[MetaOapg.properties.sketch_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        tags: typing.Union[MetaOapg.properties.tags, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        webhook_active: typing.Union[MetaOapg.properties.webhook_active, bool, schemas.Unset] = schemas.unset,
        webhook_uri: typing.Union[MetaOapg.properties.webhook_uri, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ArduinoThing':
        return super().__new__(
            cls,
            *_args,
            user_id=user_id,
            timezone=timezone,
            name=name,
            href=href,
            id=id,
            assistant=assistant,
            created_at=created_at,
            deleted_at=deleted_at,
            device_fqbn=device_fqbn,
            device_id=device_id,
            device_name=device_name,
            device_type=device_type,
            organization_id=organization_id,
            properties=properties,
            properties_count=properties_count,
            sketch_id=sketch_id,
            tags=tags,
            updated_at=updated_at,
            webhook_active=webhook_active,
            webhook_uri=webhook_uri,
            _configuration=_configuration,
            **kwargs,
        )

from iot_api_client.model.arduino_property_collection import ArduinoPropertyCollection
