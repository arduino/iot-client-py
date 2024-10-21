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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, conlist
from iot_api_client.models.properties_value import PropertiesValue

class PropertiesValues(BaseModel):
    """
    PropertiesValues
    """
    input: Optional[StrictBool] = Field(False, description="If true, send property values to device's input topic.")
    properties: conlist(PropertiesValue) = Field(...)
    __properties = ["input", "properties"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PropertiesValues:
        """Create an instance of PropertiesValues from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in properties (list)
        _items = []
        if self.properties:
            for _item in self.properties:
                if _item:
                    _items.append(_item.to_dict())
            _dict['properties'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PropertiesValues:
        """Create an instance of PropertiesValues from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PropertiesValues.parse_obj(obj)

        _obj = PropertiesValues.parse_obj({
            "input": obj.get("input") if obj.get("input") is not None else False,
            "properties": [PropertiesValue.from_dict(_item) for _item in obj.get("properties")] if obj.get("properties") is not None else None
        })
        return _obj


