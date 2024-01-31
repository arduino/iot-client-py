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


class ArduinoWidgetv2(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ArduinoWidgetv2 media type (default view)
    """


    class MetaOapg:
        required = {
            "options",
            "width",
            "x",
            "y",
            "id",
            "type",
            "height",
        }
        
        class properties:
            height = schemas.Int64Schema
            id = schemas.UUIDSchema
            
            
            class options(
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
                ) -> 'options':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SLIDER_GAUGE(cls):
                    return cls("slider, gauge")
            width = schemas.Int64Schema
            x = schemas.Int64Schema
            y = schemas.Int64Schema
            has_permission_incompatibility = schemas.BoolSchema
            has_type_incompatibility = schemas.BoolSchema
            has_unlinked_variable = schemas.BoolSchema
            height_mobile = schemas.Int64Schema
            name = schemas.StrSchema
        
            @staticmethod
            def variables() -> typing.Type['ArduinoLinkedvariableCollection']:
                return ArduinoLinkedvariableCollection
            width_mobile = schemas.Int64Schema
            x_mobile = schemas.Int64Schema
            y_mobile = schemas.Int64Schema
            __annotations__ = {
                "height": height,
                "id": id,
                "options": options,
                "type": type,
                "width": width,
                "x": x,
                "y": y,
                "has_permission_incompatibility": has_permission_incompatibility,
                "has_type_incompatibility": has_type_incompatibility,
                "has_unlinked_variable": has_unlinked_variable,
                "height_mobile": height_mobile,
                "name": name,
                "variables": variables,
                "width_mobile": width_mobile,
                "x_mobile": x_mobile,
                "y_mobile": y_mobile,
            }
    
    options: MetaOapg.properties.options
    width: MetaOapg.properties.width
    x: MetaOapg.properties.x
    y: MetaOapg.properties.y
    id: MetaOapg.properties.id
    type: MetaOapg.properties.type
    height: MetaOapg.properties.height
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> MetaOapg.properties.options: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["x"]) -> MetaOapg.properties.x: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["y"]) -> MetaOapg.properties.y: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_permission_incompatibility"]) -> MetaOapg.properties.has_permission_incompatibility: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_type_incompatibility"]) -> MetaOapg.properties.has_type_incompatibility: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_unlinked_variable"]) -> MetaOapg.properties.has_unlinked_variable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["height_mobile"]) -> MetaOapg.properties.height_mobile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variables"]) -> 'ArduinoLinkedvariableCollection': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["width_mobile"]) -> MetaOapg.properties.width_mobile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["x_mobile"]) -> MetaOapg.properties.x_mobile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["y_mobile"]) -> MetaOapg.properties.y_mobile: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["height", "id", "options", "type", "width", "x", "y", "has_permission_incompatibility", "has_type_incompatibility", "has_unlinked_variable", "height_mobile", "name", "variables", "width_mobile", "x_mobile", "y_mobile", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> MetaOapg.properties.options: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["x"]) -> MetaOapg.properties.x: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["y"]) -> MetaOapg.properties.y: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_permission_incompatibility"]) -> typing.Union[MetaOapg.properties.has_permission_incompatibility, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_type_incompatibility"]) -> typing.Union[MetaOapg.properties.has_type_incompatibility, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_unlinked_variable"]) -> typing.Union[MetaOapg.properties.has_unlinked_variable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["height_mobile"]) -> typing.Union[MetaOapg.properties.height_mobile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variables"]) -> typing.Union['ArduinoLinkedvariableCollection', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["width_mobile"]) -> typing.Union[MetaOapg.properties.width_mobile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["x_mobile"]) -> typing.Union[MetaOapg.properties.x_mobile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["y_mobile"]) -> typing.Union[MetaOapg.properties.y_mobile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["height", "id", "options", "type", "width", "x", "y", "has_permission_incompatibility", "has_type_incompatibility", "has_unlinked_variable", "height_mobile", "name", "variables", "width_mobile", "x_mobile", "y_mobile", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        options: typing.Union[MetaOapg.properties.options, dict, frozendict.frozendict, ],
        width: typing.Union[MetaOapg.properties.width, decimal.Decimal, int, ],
        x: typing.Union[MetaOapg.properties.x, decimal.Decimal, int, ],
        y: typing.Union[MetaOapg.properties.y, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        height: typing.Union[MetaOapg.properties.height, decimal.Decimal, int, ],
        has_permission_incompatibility: typing.Union[MetaOapg.properties.has_permission_incompatibility, bool, schemas.Unset] = schemas.unset,
        has_type_incompatibility: typing.Union[MetaOapg.properties.has_type_incompatibility, bool, schemas.Unset] = schemas.unset,
        has_unlinked_variable: typing.Union[MetaOapg.properties.has_unlinked_variable, bool, schemas.Unset] = schemas.unset,
        height_mobile: typing.Union[MetaOapg.properties.height_mobile, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        variables: typing.Union['ArduinoLinkedvariableCollection', schemas.Unset] = schemas.unset,
        width_mobile: typing.Union[MetaOapg.properties.width_mobile, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        x_mobile: typing.Union[MetaOapg.properties.x_mobile, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        y_mobile: typing.Union[MetaOapg.properties.y_mobile, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ArduinoWidgetv2':
        return super().__new__(
            cls,
            *_args,
            options=options,
            width=width,
            x=x,
            y=y,
            id=id,
            type=type,
            height=height,
            has_permission_incompatibility=has_permission_incompatibility,
            has_type_incompatibility=has_type_incompatibility,
            has_unlinked_variable=has_unlinked_variable,
            height_mobile=height_mobile,
            name=name,
            variables=variables,
            width_mobile=width_mobile,
            x_mobile=x_mobile,
            y_mobile=y_mobile,
            _configuration=_configuration,
            **kwargs,
        )

from iot_api_client.model.arduino_linkedvariable_collection import ArduinoLinkedvariableCollection
