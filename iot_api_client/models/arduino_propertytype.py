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
from typing import Optional, Set
from typing_extensions import Self

class ArduinoPropertytype(BaseModel):
    """
    ArduinoPropertytype media type (default view)
    """ # noqa: E501
    assistants: Optional[List[StrictStr]] = Field(default=None, description="The voice assistants available for this type")
    declaration: StrictStr = Field(description="The c++ type we are using for this variable type")
    deprecated: StrictBool = Field(description="Tell if this type is deprecated")
    example: Optional[StrictStr] = Field(default=None, description="Example of use")
    name: StrictStr = Field(description="The friendly name of the property type")
    rw: StrictBool = Field(description="Tell if the type allow a R/W permission")
    superseded_by: Optional[StrictStr] = Field(default=None, description="The type of property to use if it's deprecated", alias="supersededBy")
    tags: Optional[List[StrictStr]] = Field(default=None, description="The tags related to the type")
    type: StrictStr = Field(description="The api reference of this type")
    units: Optional[List[StrictStr]] = Field(default=None, description="The measure units available for this type")
    __properties: ClassVar[List[str]] = ["assistants", "declaration", "deprecated", "example", "name", "rw", "supersededBy", "tags", "type", "units"]

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
        """Create an instance of ArduinoPropertytype from a JSON string"""
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
        """Create an instance of ArduinoPropertytype from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assistants": obj.get("assistants"),
            "declaration": obj.get("declaration"),
            "deprecated": obj.get("deprecated"),
            "example": obj.get("example"),
            "name": obj.get("name"),
            "rw": obj.get("rw"),
            "supersededBy": obj.get("supersededBy"),
            "tags": obj.get("tags"),
            "type": obj.get("type"),
            "units": obj.get("units")
        })
        return _obj

