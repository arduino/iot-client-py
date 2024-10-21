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
from typing import Any, ClassVar, Dict, List
from iot_api_client.models.arduino_devicev2propertyvalue import ArduinoDevicev2propertyvalue
from iot_api_client.models.arduino_devicev2propertyvalues_last_evaluated_key import ArduinoDevicev2propertyvaluesLastEvaluatedKey
from typing import Optional, Set
from typing_extensions import Self

class ArduinoDevicev2propertyvalues(BaseModel):
    """
    ArduinoDevicev2propertyvalues media type (default view)
    """ # noqa: E501
    id: StrictStr
    last_evaluated_key: ArduinoDevicev2propertyvaluesLastEvaluatedKey
    name: StrictStr
    values: List[ArduinoDevicev2propertyvalue] = Field(description="ArduinoDevicev2propertyvalueCollection is the media type for an array of ArduinoDevicev2propertyvalue (default view)")
    __properties: ClassVar[List[str]] = ["id", "last_evaluated_key", "name", "values"]

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
        """Create an instance of ArduinoDevicev2propertyvalues from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of last_evaluated_key
        if self.last_evaluated_key:
            _dict['last_evaluated_key'] = self.last_evaluated_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in values (list)
        _items = []
        if self.values:
            for _item_values in self.values:
                if _item_values:
                    _items.append(_item_values.to_dict())
            _dict['values'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ArduinoDevicev2propertyvalues from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "last_evaluated_key": ArduinoDevicev2propertyvaluesLastEvaluatedKey.from_dict(obj["last_evaluated_key"]) if obj.get("last_evaluated_key") is not None else None,
            "name": obj.get("name"),
            "values": [ArduinoDevicev2propertyvalue.from_dict(_item) for _item in obj["values"]] if obj.get("values") is not None else None
        })
        return _obj


