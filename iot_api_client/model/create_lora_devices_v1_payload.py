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


class CreateLoraDevicesV1Payload(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "app",
            "user_id",
            "eui",
            "frequency_plan",
            "name",
            "type",
        }
        
        class properties:
            app = schemas.StrSchema
            
            
            class eui(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'[0-9a-z]{16}',  # noqa: E501
                    }]
            
            
            class frequency_plan(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "EU_863_870_TTN": "EU_863_870_TTN",
                        "US_902_928_FSB_2": "US_902_928_FSB_2",
                        "EU_433": "EU_433",
                        "AU_915_928_FSB_2": "AU_915_928_FSB_2",
                        "CN_470_510_FSB_11": "CN_470_510_FSB_11",
                        "AS_920_923": "AS_920_923",
                        "AS_920_923_TTN_AU": "AS_920_923_TTN_AU",
                        "AS_923_925": "AS_923_925",
                        "AS_923_925_TTN_AU": "AS_923_925_TTN_AU",
                        "KR_920_923_TTN": "KR_920_923_TTN",
                        "IN_865_867": "IN_865_867",
                    }
                
                @schemas.classproperty
                def EU_863_870_TTN(cls):
                    return cls("EU_863_870_TTN")
                
                @schemas.classproperty
                def US_902_928_FSB_2(cls):
                    return cls("US_902_928_FSB_2")
                
                @schemas.classproperty
                def EU_433(cls):
                    return cls("EU_433")
                
                @schemas.classproperty
                def AU_915_928_FSB_2(cls):
                    return cls("AU_915_928_FSB_2")
                
                @schemas.classproperty
                def CN_470_510_FSB_11(cls):
                    return cls("CN_470_510_FSB_11")
                
                @schemas.classproperty
                def AS_920_923(cls):
                    return cls("AS_920_923")
                
                @schemas.classproperty
                def AS_920_923_TTN_AU(cls):
                    return cls("AS_920_923_TTN_AU")
                
                @schemas.classproperty
                def AS_923_925(cls):
                    return cls("AS_923_925")
                
                @schemas.classproperty
                def AS_923_925_TTN_AU(cls):
                    return cls("AS_923_925_TTN_AU")
                
                @schemas.classproperty
                def KR_920_923_TTN(cls):
                    return cls("KR_920_923_TTN")
                
                @schemas.classproperty
                def IN_865_867(cls):
                    return cls("IN_865_867")
            name = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "lora-device": "LORADEVICE",
                        "mkrwan1300": "MKRWAN1300",
                        "mkrwan1310": "MKRWAN1310",
                    }
                
                @schemas.classproperty
                def LORADEVICE(cls):
                    return cls("lora-device")
                
                @schemas.classproperty
                def MKRWAN1300(cls):
                    return cls("mkrwan1300")
                
                @schemas.classproperty
                def MKRWAN1310(cls):
                    return cls("mkrwan1310")
            user_id = schemas.StrSchema
            
            
            class app_eui(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'[0-9a-z]{16}',  # noqa: E501
                    }]
            
            
            class app_key(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'[0-9a-z]{16}',  # noqa: E501
                    }]
            serial = schemas.StrSchema
            __annotations__ = {
                "app": app,
                "eui": eui,
                "frequency_plan": frequency_plan,
                "name": name,
                "type": type,
                "user_id": user_id,
                "app_eui": app_eui,
                "app_key": app_key,
                "serial": serial,
            }
    
    app: MetaOapg.properties.app
    user_id: MetaOapg.properties.user_id
    eui: MetaOapg.properties.eui
    frequency_plan: MetaOapg.properties.frequency_plan
    name: MetaOapg.properties.name
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["app"]) -> MetaOapg.properties.app: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eui"]) -> MetaOapg.properties.eui: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frequency_plan"]) -> MetaOapg.properties.frequency_plan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["app_eui"]) -> MetaOapg.properties.app_eui: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["app_key"]) -> MetaOapg.properties.app_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serial"]) -> MetaOapg.properties.serial: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["app", "eui", "frequency_plan", "name", "type", "user_id", "app_eui", "app_key", "serial", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["app"]) -> MetaOapg.properties.app: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eui"]) -> MetaOapg.properties.eui: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frequency_plan"]) -> MetaOapg.properties.frequency_plan: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["app_eui"]) -> typing.Union[MetaOapg.properties.app_eui, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["app_key"]) -> typing.Union[MetaOapg.properties.app_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serial"]) -> typing.Union[MetaOapg.properties.serial, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["app", "eui", "frequency_plan", "name", "type", "user_id", "app_eui", "app_key", "serial", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        app: typing.Union[MetaOapg.properties.app, str, ],
        user_id: typing.Union[MetaOapg.properties.user_id, str, ],
        eui: typing.Union[MetaOapg.properties.eui, str, ],
        frequency_plan: typing.Union[MetaOapg.properties.frequency_plan, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        app_eui: typing.Union[MetaOapg.properties.app_eui, str, schemas.Unset] = schemas.unset,
        app_key: typing.Union[MetaOapg.properties.app_key, str, schemas.Unset] = schemas.unset,
        serial: typing.Union[MetaOapg.properties.serial, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateLoraDevicesV1Payload':
        return super().__new__(
            cls,
            *_args,
            app=app,
            user_id=user_id,
            eui=eui,
            frequency_plan=frequency_plan,
            name=name,
            type=type,
            app_eui=app_eui,
            app_key=app_key,
            serial=serial,
            _configuration=_configuration,
            **kwargs,
        )
