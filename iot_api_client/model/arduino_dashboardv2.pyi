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


class ArduinoDashboardv2(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Dashboard is a collection of widgets (default view)
    """


    class MetaOapg:
        required = {
            "updated_at",
            "name",
            "id",
        }
        
        class properties:
            id = schemas.UUIDSchema
            name = schemas.StrSchema
            updated_at = schemas.DateTimeSchema
            
            
            class cover_image(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def created_by() -> typing.Type['ArduinoDashboardowner']:
                return ArduinoDashboardowner
            organization_id = schemas.UUIDSchema
        
            @staticmethod
            def shared_by() -> typing.Type['ArduinoDashboardshare']:
                return ArduinoDashboardshare
        
            @staticmethod
            def shared_with() -> typing.Type['ArduinoDashboardshareCollection']:
                return ArduinoDashboardshareCollection
        
            @staticmethod
            def widgets() -> typing.Type['ArduinoWidgetv2Collection']:
                return ArduinoWidgetv2Collection
            __annotations__ = {
                "id": id,
                "name": name,
                "updated_at": updated_at,
                "cover_image": cover_image,
                "created_by": created_by,
                "organization_id": organization_id,
                "shared_by": shared_by,
                "shared_with": shared_with,
                "widgets": widgets,
            }
    
    updated_at: MetaOapg.properties.updated_at
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cover_image"]) -> MetaOapg.properties.cover_image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_by"]) -> 'ArduinoDashboardowner': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization_id"]) -> MetaOapg.properties.organization_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shared_by"]) -> 'ArduinoDashboardshare': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shared_with"]) -> 'ArduinoDashboardshareCollection': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["widgets"]) -> 'ArduinoWidgetv2Collection': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "updated_at", "cover_image", "created_by", "organization_id", "shared_by", "shared_with", "widgets", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cover_image"]) -> typing.Union[MetaOapg.properties.cover_image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_by"]) -> typing.Union['ArduinoDashboardowner', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization_id"]) -> typing.Union[MetaOapg.properties.organization_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shared_by"]) -> typing.Union['ArduinoDashboardshare', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shared_with"]) -> typing.Union['ArduinoDashboardshareCollection', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["widgets"]) -> typing.Union['ArduinoWidgetv2Collection', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "updated_at", "cover_image", "created_by", "organization_id", "shared_by", "shared_with", "widgets", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        cover_image: typing.Union[MetaOapg.properties.cover_image, str, schemas.Unset] = schemas.unset,
        created_by: typing.Union['ArduinoDashboardowner', schemas.Unset] = schemas.unset,
        organization_id: typing.Union[MetaOapg.properties.organization_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        shared_by: typing.Union['ArduinoDashboardshare', schemas.Unset] = schemas.unset,
        shared_with: typing.Union['ArduinoDashboardshareCollection', schemas.Unset] = schemas.unset,
        widgets: typing.Union['ArduinoWidgetv2Collection', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ArduinoDashboardv2':
        return super().__new__(
            cls,
            *_args,
            updated_at=updated_at,
            name=name,
            id=id,
            cover_image=cover_image,
            created_by=created_by,
            organization_id=organization_id,
            shared_by=shared_by,
            shared_with=shared_with,
            widgets=widgets,
            _configuration=_configuration,
            **kwargs,
        )

from iot_api_client.model.arduino_dashboardowner import ArduinoDashboardowner
from iot_api_client.model.arduino_dashboardshare import ArduinoDashboardshare
from iot_api_client.model.arduino_dashboardshare_collection import ArduinoDashboardshareCollection
from iot_api_client.model.arduino_widgetv2_collection import ArduinoWidgetv2Collection
