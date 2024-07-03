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


class Devicev2(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    DeviceV2 describes a device.
    """


    class MetaOapg:
        
        class properties:
            
            
            class connection_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "wifi": "WIFI",
                        "eth": "ETH",
                        "wifiandsecret": "WIFIANDSECRET",
                        "gsm": "GSM",
                        "nb": "NB",
                        "lora": "LORA",
                        "catm1": "CATM1",
                        "cellular": "CELLULAR",
                    }
                
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
            fqbn = schemas.StrSchema
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
                    regex=[{
                        'pattern': r'[a-zA-Z0-9_.@-]+',  # noqa: E501
                    }]
            
            
            class serial(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
                    regex=[{
                        'pattern': r'[a-zA-Z0-9_.@-]+',  # noqa: E501
                    }]
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "mkrwifi1010": "MKRWIFI1010",
                        "mkr1000": "MKR1000",
                        "nano_33_iot": "NANO_33_IOT",
                        "mkrgsm1400": "MKRGSM1400",
                        "mkrwan1310": "MKRWAN1310",
                        "mkrwan1300": "MKRWAN1300",
                        "mkrnb1500": "MKRNB1500",
                        "lora-device": "LORADEVICE",
                        "login_and_secretkey_wifi": "LOGIN_AND_SECRETKEY_WIFI",
                        "envie_m7": "ENVIE_M7",
                        "nanorp2040connect": "NANORP2040CONNECT",
                        "nicla_vision": "NICLA_VISION",
                        "phone": "PHONE",
                        "portenta_x8": "PORTENTA_X8",
                        "opta": "OPTA",
                        "giga": "GIGA",
                        "generic_device_secretkey": "GENERIC_DEVICE_SECRETKEY",
                        "portenta_c33": "PORTENTA_C33",
                        "unor4wifi": "UNOR4WIFI",
                        "nano_nora": "NANO_NORA",
                    }
                
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
                def PHONE(cls):
                    return cls("phone")
                
                @schemas.classproperty
                def PORTENTA_X8(cls):
                    return cls("portenta_x8")
                
                @schemas.classproperty
                def OPTA(cls):
                    return cls("opta")
                
                @schemas.classproperty
                def GIGA(cls):
                    return cls("giga")
                
                @schemas.classproperty
                def GENERIC_DEVICE_SECRETKEY(cls):
                    return cls("generic_device_secretkey")
                
                @schemas.classproperty
                def PORTENTA_C33(cls):
                    return cls("portenta_c33")
                
                @schemas.classproperty
                def UNOR4WIFI(cls):
                    return cls("unor4wifi")
                
                @schemas.classproperty
                def NANO_NORA(cls):
                    return cls("nano_nora")
            user_id = schemas.UUIDSchema
            
            
            class wifi_fw_version(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 10
                    regex=[{
                        'pattern': r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$',  # noqa: E501
                    }]
            __annotations__ = {
                "connection_type": connection_type,
                "fqbn": fqbn,
                "name": name,
                "serial": serial,
                "type": type,
                "user_id": user_id,
                "wifi_fw_version": wifi_fw_version,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connection_type"]) -> MetaOapg.properties.connection_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fqbn"]) -> MetaOapg.properties.fqbn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serial"]) -> MetaOapg.properties.serial: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wifi_fw_version"]) -> MetaOapg.properties.wifi_fw_version: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["connection_type", "fqbn", "name", "serial", "type", "user_id", "wifi_fw_version", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connection_type"]) -> typing.Union[MetaOapg.properties.connection_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fqbn"]) -> typing.Union[MetaOapg.properties.fqbn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serial"]) -> typing.Union[MetaOapg.properties.serial, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> typing.Union[MetaOapg.properties.user_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wifi_fw_version"]) -> typing.Union[MetaOapg.properties.wifi_fw_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["connection_type", "fqbn", "name", "serial", "type", "user_id", "wifi_fw_version", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        connection_type: typing.Union[MetaOapg.properties.connection_type, str, schemas.Unset] = schemas.unset,
        fqbn: typing.Union[MetaOapg.properties.fqbn, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        serial: typing.Union[MetaOapg.properties.serial, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        user_id: typing.Union[MetaOapg.properties.user_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        wifi_fw_version: typing.Union[MetaOapg.properties.wifi_fw_version, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Devicev2':
        return super().__new__(
            cls,
            *_args,
            connection_type=connection_type,
            fqbn=fqbn,
            name=name,
            serial=serial,
            type=type,
            user_id=user_id,
            wifi_fw_version=wifi_fw_version,
            _configuration=_configuration,
            **kwargs,
        )
