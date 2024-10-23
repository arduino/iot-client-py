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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from iot_api_client.models.arduino_devicev2templatedevice import ArduinoDevicev2templatedevice
from iot_api_client.models.arduino_templateproperty import ArduinoTemplateproperty
from iot_api_client.models.tag import Tag
from typing import Optional, Set
from typing_extensions import Self

class ArduinoThingtemplate(BaseModel):
    """
    ArduinoThingtemplate media type (default view)
    """ # noqa: E501
    device_metadata: Optional[ArduinoDevicev2templatedevice] = None
    id: Optional[StrictStr] = Field(default=None, description="The friendly id of the thing")
    name: StrictStr = Field(description="The friendly name of the thing")
    organization_id: Optional[StrictStr] = Field(default=None, description="Id of the organization the thing belongs to")
    sketch_template: Optional[StrictStr] = Field(default=None, description="The ID of the template's sketch")
    tags: Optional[List[Tag]] = Field(default=None, description="Tags of the thing")
    timezone: StrictStr = Field(description="Time zone of the thing")
    variables: Optional[List[ArduinoTemplateproperty]] = Field(default=None, description="ArduinoTemplatepropertyCollection is the media type for an array of ArduinoTemplateproperty (default view)")
    webhook_uri: Optional[StrictStr] = Field(default=None, description="Webhook uri")
    __properties: ClassVar[List[str]] = ["device_metadata", "id", "name", "organization_id", "sketch_template", "tags", "timezone", "variables", "webhook_uri"]

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
        """Create an instance of ArduinoThingtemplate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of device_metadata
        if self.device_metadata:
            _dict['device_metadata'] = self.device_metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item_tags in self.tags:
                if _item_tags:
                    _items.append(_item_tags.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in variables (list)
        _items = []
        if self.variables:
            for _item_variables in self.variables:
                if _item_variables:
                    _items.append(_item_variables.to_dict())
            _dict['variables'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ArduinoThingtemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "device_metadata": ArduinoDevicev2templatedevice.from_dict(obj["device_metadata"]) if obj.get("device_metadata") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "organization_id": obj.get("organization_id"),
            "sketch_template": obj.get("sketch_template"),
            "tags": [Tag.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "timezone": obj.get("timezone"),
            "variables": [ArduinoTemplateproperty.from_dict(_item) for _item in obj["variables"]] if obj.get("variables") is not None else None,
            "webhook_uri": obj.get("webhook_uri")
        })
        return _obj

