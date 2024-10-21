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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class Dashboardshare(BaseModel):
    """
    Dashboardshare
    """
    user_id: Optional[StrictStr] = Field(None, description="The userID of the user you want to share the dashboard with")
    username: Optional[StrictStr] = Field(None, description="The username of the user you want to share the dashboard with")
    __properties = ["user_id", "username"]

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
    def from_json(cls, json_str: str) -> Dashboardshare:
        """Create an instance of Dashboardshare from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Dashboardshare:
        """Create an instance of Dashboardshare from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Dashboardshare.parse_obj(obj)

        _obj = Dashboardshare.parse_obj({
            "user_id": obj.get("user_id"),
            "username": obj.get("username")
        })
        return _obj


