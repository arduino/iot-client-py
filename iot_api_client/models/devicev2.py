# coding: utf-8

"""
    Arduino IoT Cloud API

    Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Devicev2(BaseModel):
    """
    DeviceV2 describes a device.
    """ # noqa: E501
    connection_type: Optional[StrictStr] = Field(default=None, description="The type of the connections selected by the user when multiple connections are available")
    fqbn: Optional[StrictStr] = Field(default=None, description="The fully qualified board name")
    name: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="The friendly name of the device")
    serial: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="The serial uuid of the device")
    type: Optional[StrictStr] = Field(default=None, description="The type of the device")
    user_id: Optional[StrictStr] = Field(default=None, description="The user_id associated to the device. If absent it will be inferred from the authentication header")
    wifi_fw_version: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="The version of the NINA/WIFI101 firmware running on the device")
    __properties: ClassVar[List[str]] = ["connection_type", "fqbn", "name", "serial", "type", "user_id", "wifi_fw_version"]

    @field_validator('connection_type')
    def connection_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['wifi', 'eth', 'wifiandsecret', 'gsm', 'nb', 'lora', 'catm1', 'cellular']):
            raise ValueError("must be one of enum values ('wifi', 'eth', 'wifiandsecret', 'gsm', 'nb', 'lora', 'catm1', 'cellular')")
        return value

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[a-zA-Z0-9_.@-]+", value):
            raise ValueError(r"must validate the regular expression /[a-zA-Z0-9_.@-]+/")
        return value

    @field_validator('serial')
    def serial_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[a-zA-Z0-9_.@-]+", value):
            raise ValueError(r"must validate the regular expression /[a-zA-Z0-9_.@-]+/")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['mkrwifi1010', 'mkr1000', 'nano_33_iot', 'mkrgsm1400', 'mkrnb1500', 'login_and_secretkey_wifi', 'envie_m7', 'nanorp2040connect', 'nicla_vision', 'phone', 'portenta_x8', 'opta', 'giga', 'generic_device_secretkey', 'portenta_c33', 'unor4wifi', 'nano_nora']):
            raise ValueError("must be one of enum values ('mkrwifi1010', 'mkr1000', 'nano_33_iot', 'mkrgsm1400', 'mkrnb1500', 'login_and_secretkey_wifi', 'envie_m7', 'nanorp2040connect', 'nicla_vision', 'phone', 'portenta_x8', 'opta', 'giga', 'generic_device_secretkey', 'portenta_c33', 'unor4wifi', 'nano_nora')")
        return value

    @field_validator('wifi_fw_version')
    def wifi_fw_version_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Devicev2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Devicev2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "connection_type": obj.get("connection_type"),
            "fqbn": obj.get("fqbn"),
            "name": obj.get("name"),
            "serial": obj.get("serial"),
            "type": obj.get("type"),
            "user_id": obj.get("user_id"),
            "wifi_fw_version": obj.get("wifi_fw_version")
        })
        return _obj


