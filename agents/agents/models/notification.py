# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from agents.models.alert_email import AlertEmail
from agents.models.alert_integration_base import AlertIntegrationBase
from typing import Optional, Set
from typing_extensions import Self

class Notification(BaseModel):
    """
    Alert notification object.
    """ # noqa: E501
    email: Optional[AlertEmail] = None
    third_party: Optional[List[AlertIntegrationBase]] = Field(default=None, alias="thirdParty")
    webhook: Optional[List[AlertIntegrationBase]] = None
    __properties: ClassVar[List[str]] = ["email", "thirdParty", "webhook"]

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
        """Create an instance of Notification from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in third_party (list)
        _items = []
        if self.third_party:
            for _item in self.third_party:
                if _item:
                    _items.append(_item.to_dict())
            _dict['thirdParty'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in webhook (list)
        _items = []
        if self.webhook:
            for _item in self.webhook:
                if _item:
                    _items.append(_item.to_dict())
            _dict['webhook'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Notification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": AlertEmail.from_dict(obj["email"]) if obj.get("email") is not None else None,
            "thirdParty": [AlertIntegrationBase.from_dict(_item) for _item in obj["thirdParty"]] if obj.get("thirdParty") is not None else None,
            "webhook": [AlertIntegrationBase.from_dict(_item) for _item in obj["webhook"]] if obj.get("webhook") is not None else None
        })
        return _obj


