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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from iot_api_client.models.arduino_action_template import ArduinoActionTemplate
from iot_api_client.models.arduino_linked_device_template import ArduinoLinkedDeviceTemplate
from iot_api_client.models.arduino_linked_property_template import ArduinoLinkedPropertyTemplate
from typing import Optional, Set
from typing_extensions import Self

class ArduinoTriggerTemplate(BaseModel):
    """
    ArduinoTrigger_template media type (default view)
    """ # noqa: E501
    actions: Optional[List[ArduinoActionTemplate]] = Field(default=None, description="A list of actions associated with the trigger")
    active: Optional[StrictBool] = Field(default=None, description="Is true if the trigger is enabled")
    criteria: Optional[StrictStr] = Field(default=None, description="The criteria of the trigger, could be INCLUDE or EXCLUDE")
    description: Optional[StrictStr] = Field(default=None, description="The description of the trigger")
    grace_period_offline: Optional[StrictInt] = Field(default=None, description="The amount of seconds the trigger will wait before considering a matching device as offline")
    grace_period_online: Optional[StrictInt] = Field(default=None, description="The amount of seconds the trigger will wait before considering a matching device as online")
    id: StrictStr = Field(description="The id of the trigger")
    linked_devices: Optional[List[ArduinoLinkedDeviceTemplate]] = Field(default=None, description="A list of devices the trigger is associated to")
    linked_property: Optional[ArduinoLinkedPropertyTemplate] = None
    name: StrictStr = Field(description="The name of the trigger")
    organization_id: Optional[StrictStr] = Field(default=None, description="Id of the organization the trigger belongs to")
    __properties: ClassVar[List[str]] = ["actions", "active", "criteria", "description", "grace_period_offline", "grace_period_online", "id", "linked_devices", "linked_property", "name", "organization_id"]

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
        """Create an instance of ArduinoTriggerTemplate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item_actions in self.actions:
                if _item_actions:
                    _items.append(_item_actions.to_dict())
            _dict['actions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in linked_devices (list)
        _items = []
        if self.linked_devices:
            for _item_linked_devices in self.linked_devices:
                if _item_linked_devices:
                    _items.append(_item_linked_devices.to_dict())
            _dict['linked_devices'] = _items
        # override the default output from pydantic by calling `to_dict()` of linked_property
        if self.linked_property:
            _dict['linked_property'] = self.linked_property.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ArduinoTriggerTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actions": [ArduinoActionTemplate.from_dict(_item) for _item in obj["actions"]] if obj.get("actions") is not None else None,
            "active": obj.get("active"),
            "criteria": obj.get("criteria"),
            "description": obj.get("description"),
            "grace_period_offline": obj.get("grace_period_offline"),
            "grace_period_online": obj.get("grace_period_online"),
            "id": obj.get("id"),
            "linked_devices": [ArduinoLinkedDeviceTemplate.from_dict(_item) for _item in obj["linked_devices"]] if obj.get("linked_devices") is not None else None,
            "linked_property": ArduinoLinkedPropertyTemplate.from_dict(obj["linked_property"]) if obj.get("linked_property") is not None else None,
            "name": obj.get("name"),
            "organization_id": obj.get("organization_id")
        })
        return _obj


