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


from typing import List
from pydantic import BaseModel, Field, StrictInt, conlist
from iot_api_client.models.batch_query_request_media_v1 import BatchQueryRequestMediaV1

class BatchQueryRequestsMediaV1(BaseModel):
    """
    BatchQueryRequestsMediaV1
    """
    requests: conlist(BatchQueryRequestMediaV1) = Field(..., description="Requests")
    resp_version: StrictInt = Field(..., description="Response version")
    __properties = ["requests", "resp_version"]

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
    def from_json(cls, json_str: str) -> BatchQueryRequestsMediaV1:
        """Create an instance of BatchQueryRequestsMediaV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in requests (list)
        _items = []
        if self.requests:
            for _item in self.requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['requests'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BatchQueryRequestsMediaV1:
        """Create an instance of BatchQueryRequestsMediaV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BatchQueryRequestsMediaV1.parse_obj(obj)

        _obj = BatchQueryRequestsMediaV1.parse_obj({
            "requests": [BatchQueryRequestMediaV1.from_dict(_item) for _item in obj.get("requests")] if obj.get("requests") is not None else None,
            "resp_version": obj.get("resp_version")
        })
        return _obj


