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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from iot_api_client.models.arduino_devicev2_simple_properties import ArduinoDevicev2SimpleProperties
from iot_api_client.models.arduino_devicev2_webhook import ArduinoDevicev2Webhook
from iot_api_client.models.arduino_thing import ArduinoThing
from typing import Optional, Set
from typing_extensions import Self

class ArduinoDevicev2(BaseModel):
    """
    ArduinoDevicev2 media type (default view)
    """ # noqa: E501
    connection_type: Optional[StrictStr] = Field(default=None, description="The type of the connections selected by the user when multiple connections are available")
    created_at: Optional[datetime] = Field(default=None, description="Creation date of the device")
    device_status: Optional[StrictStr] = Field(default=None, description="The connection status of the device")
    events: Optional[List[ArduinoDevicev2SimpleProperties]] = Field(default=None, description="ArduinoDevicev2SimplePropertiesCollection is the media type for an array of ArduinoDevicev2SimpleProperties (default view)")
    fqbn: Optional[StrictStr] = Field(default=None, description="The fully qualified board name")
    href: StrictStr = Field(description="The api reference of this device")
    id: StrictStr = Field(description="The arn of the device")
    label: StrictStr = Field(description="The label of the device")
    last_activity_at: Optional[datetime] = Field(default=None, description="Last activity date")
    latest_wifi_fw_version: Optional[StrictStr] = Field(default=None, description="The latest version of the NINA/WIFI101 firmware available for this device")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="The metadata of the device")
    name: StrictStr = Field(description="The friendly name of the device")
    no_sketch: Optional[StrictBool] = Field(default=None, description="True if the device type can not have an associated sketch")
    organization_id: Optional[StrictStr] = Field(default=None, description="Id of the organization the device belongs to")
    ota_available: Optional[StrictBool] = Field(default=None, description="True if the device type is ready to receive OTA updated")
    ota_compatible: Optional[StrictBool] = Field(default=None, description="True if the device type is OTA compatible")
    required_wifi_fw_version: Optional[StrictStr] = Field(default=None, description="The required version of the NINA/WIFI101 firmware needed by IoT Cloud")
    serial: StrictStr = Field(description="The serial uuid of the device")
    tags: Optional[Dict[str, Any]] = Field(default=None, description="Tags belonging to the device")
    thing: Optional[ArduinoThing] = None
    type: StrictStr = Field(description="The type of the device")
    user_id: StrictStr = Field(description="The id of the user")
    webhooks: Optional[List[ArduinoDevicev2Webhook]] = Field(default=None, description="ArduinoDevicev2WebhookCollection is the media type for an array of ArduinoDevicev2Webhook (default view)")
    wifi_fw_version: Optional[StrictStr] = Field(default=None, description="The version of the NINA/WIFI101 firmware running on the device")
    __properties: ClassVar[List[str]] = ["connection_type", "created_at", "device_status", "events", "fqbn", "href", "id", "label", "last_activity_at", "latest_wifi_fw_version", "metadata", "name", "no_sketch", "organization_id", "ota_available", "ota_compatible", "required_wifi_fw_version", "serial", "tags", "thing", "type", "user_id", "webhooks", "wifi_fw_version"]

    @field_validator('connection_type')
    def connection_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['wifi', 'eth', 'wifiandsecret', 'gsm', 'nb', 'lora', 'catm1', 'cellular']):
            raise ValueError("must be one of enum values ('wifi', 'eth', 'wifiandsecret', 'gsm', 'nb', 'lora', 'catm1', 'cellular')")
        return value

    @field_validator('device_status')
    def device_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ONLINE', 'OFFLINE', 'UNKNOWN']):
            raise ValueError("must be one of enum values ('ONLINE', 'OFFLINE', 'UNKNOWN')")
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
        """Create an instance of ArduinoDevicev2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in events (list)
        _items = []
        if self.events:
            for _item_events in self.events:
                if _item_events:
                    _items.append(_item_events.to_dict())
            _dict['events'] = _items
        # override the default output from pydantic by calling `to_dict()` of thing
        if self.thing:
            _dict['thing'] = self.thing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in webhooks (list)
        _items = []
        if self.webhooks:
            for _item_webhooks in self.webhooks:
                if _item_webhooks:
                    _items.append(_item_webhooks.to_dict())
            _dict['webhooks'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ArduinoDevicev2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "connection_type": obj.get("connection_type"),
            "created_at": obj.get("created_at"),
            "device_status": obj.get("device_status"),
            "events": [ArduinoDevicev2SimpleProperties.from_dict(_item) for _item in obj["events"]] if obj.get("events") is not None else None,
            "fqbn": obj.get("fqbn"),
            "href": obj.get("href"),
            "id": obj.get("id"),
            "label": obj.get("label"),
            "last_activity_at": obj.get("last_activity_at"),
            "latest_wifi_fw_version": obj.get("latest_wifi_fw_version"),
            "metadata": obj.get("metadata"),
            "name": obj.get("name"),
            "no_sketch": obj.get("no_sketch"),
            "organization_id": obj.get("organization_id"),
            "ota_available": obj.get("ota_available"),
            "ota_compatible": obj.get("ota_compatible"),
            "required_wifi_fw_version": obj.get("required_wifi_fw_version"),
            "serial": obj.get("serial"),
            "tags": obj.get("tags"),
            "thing": ArduinoThing.from_dict(obj["thing"]) if obj.get("thing") is not None else None,
            "type": obj.get("type"),
            "user_id": obj.get("user_id"),
            "webhooks": [ArduinoDevicev2Webhook.from_dict(_item) for _item in obj["webhooks"]] if obj.get("webhooks") is not None else None,
            "wifi_fw_version": obj.get("wifi_fw_version")
        })
        return _obj


