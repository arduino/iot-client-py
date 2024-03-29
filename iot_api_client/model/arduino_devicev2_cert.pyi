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


class ArduinoDevicev2Cert(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    DeviceCertV2 describes a certificate associated to the device (default view)
    """


    class MetaOapg:
        required = {
            "der",
            "device_id",
            "pem",
            "compressed",
            "href",
            "id",
            "enabled",
        }
        
        class properties:
        
            @staticmethod
            def compressed() -> typing.Type['ArduinoCompressedv2']:
                return ArduinoCompressedv2
            der = schemas.StrSchema
            device_id = schemas.UUIDSchema
            enabled = schemas.BoolSchema
            href = schemas.StrSchema
            id = schemas.UUIDSchema
            
            
            class pem(
                schemas.StrSchema
            ):
                pass
            ca = schemas.StrSchema
            __annotations__ = {
                "compressed": compressed,
                "der": der,
                "device_id": device_id,
                "enabled": enabled,
                "href": href,
                "id": id,
                "pem": pem,
                "ca": ca,
            }
    
    der: MetaOapg.properties.der
    device_id: MetaOapg.properties.device_id
    pem: MetaOapg.properties.pem
    compressed: 'ArduinoCompressedv2'
    href: MetaOapg.properties.href
    id: MetaOapg.properties.id
    enabled: MetaOapg.properties.enabled
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compressed"]) -> 'ArduinoCompressedv2': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["der"]) -> MetaOapg.properties.der: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_id"]) -> MetaOapg.properties.device_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pem"]) -> MetaOapg.properties.pem: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ca"]) -> MetaOapg.properties.ca: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["compressed", "der", "device_id", "enabled", "href", "id", "pem", "ca", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compressed"]) -> 'ArduinoCompressedv2': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["der"]) -> MetaOapg.properties.der: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_id"]) -> MetaOapg.properties.device_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pem"]) -> MetaOapg.properties.pem: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ca"]) -> typing.Union[MetaOapg.properties.ca, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["compressed", "der", "device_id", "enabled", "href", "id", "pem", "ca", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        der: typing.Union[MetaOapg.properties.der, str, ],
        device_id: typing.Union[MetaOapg.properties.device_id, str, uuid.UUID, ],
        pem: typing.Union[MetaOapg.properties.pem, str, ],
        compressed: 'ArduinoCompressedv2',
        href: typing.Union[MetaOapg.properties.href, str, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        enabled: typing.Union[MetaOapg.properties.enabled, bool, ],
        ca: typing.Union[MetaOapg.properties.ca, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ArduinoDevicev2Cert':
        return super().__new__(
            cls,
            *_args,
            der=der,
            device_id=device_id,
            pem=pem,
            compressed=compressed,
            href=href,
            id=id,
            enabled=enabled,
            ca=ca,
            _configuration=_configuration,
            **kwargs,
        )

from iot_api_client.model.arduino_compressedv2 import ArduinoCompressedv2
