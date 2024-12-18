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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from iot_api_client.models.arduino_dashboardowner import ArduinoDashboardowner
from iot_api_client.models.arduino_dashboardshare import ArduinoDashboardshare
from iot_api_client.models.arduino_widgetv2 import ArduinoWidgetv2
from typing import Optional, Set
from typing_extensions import Self

class ArduinoDashboardv2(BaseModel):
    """
    Dashboard is a collection of widgets (default view)
    """ # noqa: E501
    cover_image: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(default=None, description="The cover image of the dashboard")
    created_by: Optional[ArduinoDashboardowner] = None
    id: StrictStr = Field(description="The friendly name of the dashboard")
    name: StrictStr = Field(description="The friendly name of the dashboard")
    organization_id: Optional[StrictStr] = Field(default=None, description="Id of the organization the dashboard belongs to")
    shared_by: Optional[ArduinoDashboardshare] = None
    shared_with: Optional[List[ArduinoDashboardshare]] = Field(default=None, description="ArduinoDashboardshareCollection is the media type for an array of ArduinoDashboardshare (default view)")
    updated_at: datetime = Field(description="Last update date")
    widgets: Optional[List[ArduinoWidgetv2]] = Field(default=None, description="ArduinoWidgetv2Collection is the media type for an array of ArduinoWidgetv2 (default view)")
    __properties: ClassVar[List[str]] = ["cover_image", "created_by", "id", "name", "organization_id", "shared_by", "shared_with", "updated_at", "widgets"]

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
        """Create an instance of ArduinoDashboardv2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shared_by
        if self.shared_by:
            _dict['shared_by'] = self.shared_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in shared_with (list)
        _items = []
        if self.shared_with:
            for _item_shared_with in self.shared_with:
                if _item_shared_with:
                    _items.append(_item_shared_with.to_dict())
            _dict['shared_with'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in widgets (list)
        _items = []
        if self.widgets:
            for _item_widgets in self.widgets:
                if _item_widgets:
                    _items.append(_item_widgets.to_dict())
            _dict['widgets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ArduinoDashboardv2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cover_image": obj.get("cover_image"),
            "created_by": ArduinoDashboardowner.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "organization_id": obj.get("organization_id"),
            "shared_by": ArduinoDashboardshare.from_dict(obj["shared_by"]) if obj.get("shared_by") is not None else None,
            "shared_with": [ArduinoDashboardshare.from_dict(_item) for _item in obj["shared_with"]] if obj.get("shared_with") is not None else None,
            "updated_at": obj.get("updated_at"),
            "widgets": [ArduinoWidgetv2.from_dict(_item) for _item in obj["widgets"]] if obj.get("widgets") is not None else None
        })
        return _obj


