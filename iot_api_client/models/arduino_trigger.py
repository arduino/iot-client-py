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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from iot_api_client.models.arduino_action import ArduinoAction
from iot_api_client.models.device_status_source import DeviceStatusSource
from typing import Optional, Set
from typing_extensions import Self

class ArduinoTrigger(BaseModel):
    """
    ArduinoTrigger media type (default view)
    """ # noqa: E501
    actions: Optional[List[ArduinoAction]] = Field(default=None, description="A list of actions associated with the trigger")
    active: Optional[StrictBool] = Field(default=None, description="Is true if the trigger is enabled")
    created_at: Optional[datetime] = Field(default=None, description="Creation date of the trigger")
    created_by: Optional[StrictStr] = Field(default=None, description="Id of the user who last updated the trigger")
    deleted_at: Optional[datetime] = Field(default=None, description="Deletion date of the trigger")
    description: Optional[StrictStr] = Field(default=None, description="The description of the trigger")
    device_status_source: Optional[DeviceStatusSource] = None
    id: Optional[StrictStr] = Field(default=None, description="The id of the trigger")
    name: StrictStr = Field(description="The name of the trigger")
    organization_id: Optional[StrictStr] = Field(default=None, description="Id of the organization the trigger belongs to")
    property_id: Optional[StrictStr] = Field(default=None, description="Id of the property the trigger is associated to (mutually exclusive with 'device_status_source')")
    updated_at: Optional[datetime] = Field(default=None, description="Update date of the trigger")
    __properties: ClassVar[List[str]] = ["actions", "active", "created_at", "created_by", "deleted_at", "description", "device_status_source", "id", "name", "organization_id", "property_id", "updated_at"]

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
        """Create an instance of ArduinoTrigger from a JSON string"""
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
        """Create an instance of ArduinoTrigger from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actions": [ArduinoAction.from_dict(_item) for _item in obj["actions"]] if obj.get("actions") is not None else None,
            "active": obj.get("active"),
            "created_at": obj.get("created_at"),
            "created_by": obj.get("created_by"),
            "deleted_at": obj.get("deleted_at"),
            "description": obj.get("description"),
            "device_status_source": DeviceStatusSource.from_dict(obj["device_status_source"]) if obj.get("device_status_source") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "organization_id": obj.get("organization_id"),
            "property_id": obj.get("property_id"),
            "updated_at": obj.get("updated_at")
        })
        return _obj

