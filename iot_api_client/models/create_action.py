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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from iot_api_client.models.email_action import EmailAction
from iot_api_client.models.push_action import PushAction
from typing import Optional, Set
from typing_extensions import Self

class CreateAction(BaseModel):
    """
    CreateAction
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="The description of the trigger")
    email: Optional[EmailAction] = None
    kind: StrictStr = Field(description="The kind of the action")
    name: StrictStr = Field(description="The name of the action")
    organization_id: Optional[StrictStr] = Field(default=None, description="Id of the organization the trigger belongs to")
    push_notification: Optional[PushAction] = None
    trigger_id: Optional[StrictStr] = Field(default=None, description="Id of the trigger the action is associated to")
    __properties: ClassVar[List[str]] = ["description", "email", "kind", "name", "organization_id", "push_notification", "trigger_id"]

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['NOTIFY-EMAIL', 'NOTIFY-PUSH']):
            raise ValueError("must be one of enum values ('NOTIFY-EMAIL', 'NOTIFY-PUSH')")
        return value

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
        """Create an instance of CreateAction from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of email
        if self.email:
            _dict['email'] = self.email.to_dict()
        # override the default output from pydantic by calling `to_dict()` of push_notification
        if self.push_notification:
            _dict['push_notification'] = self.push_notification.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateAction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "email": EmailAction.from_dict(obj["email"]) if obj.get("email") is not None else None,
            "kind": obj.get("kind"),
            "name": obj.get("name"),
            "organization_id": obj.get("organization_id"),
            "push_notification": PushAction.from_dict(obj["push_notification"]) if obj.get("push_notification") is not None else None,
            "trigger_id": obj.get("trigger_id")
        })
        return _obj


