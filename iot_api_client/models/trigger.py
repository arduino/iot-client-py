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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from iot_api_client.models.create_action import CreateAction
from iot_api_client.models.device_status_source import DeviceStatusSource
from typing import Optional, Set
from typing_extensions import Self

class Trigger(BaseModel):
    """
    Trigger
    """ # noqa: E501
    actions: Optional[List[CreateAction]] = Field(default=None, description="A list of actions to be associated with the trigger")
    active: Optional[StrictBool] = Field(default=None, description="Is true if the trigger is enabled")
    description: Optional[StrictStr] = Field(default=None, description="The description of the trigger")
    device_status_source: Optional[DeviceStatusSource] = None
    id: Optional[StrictStr] = Field(default=None, description="The id of the trigger")
    name: Optional[StrictStr] = Field(default=None, description="The name of the trigger")
    property_id: Optional[StrictStr] = Field(default=None, description="Id of the property the trigger is associated to (mutually exclusive with 'device_status_source')")
    soft_deleted: Optional[StrictBool] = Field(default=False, description="If false, restore the thing from the soft deletion")
    __properties: ClassVar[List[str]] = ["actions", "active", "description", "device_status_source", "id", "name", "property_id", "soft_deleted"]

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
        """Create an instance of Trigger from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of device_status_source
        if self.device_status_source:
            _dict['device_status_source'] = self.device_status_source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Trigger from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actions": [CreateAction.from_dict(_item) for _item in obj["actions"]] if obj.get("actions") is not None else None,
            "active": obj.get("active"),
            "description": obj.get("description"),
            "device_status_source": DeviceStatusSource.from_dict(obj["device_status_source"]) if obj.get("device_status_source") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "property_id": obj.get("property_id"),
            "soft_deleted": obj.get("soft_deleted") if obj.get("soft_deleted") is not None else False
        })
        return _obj


