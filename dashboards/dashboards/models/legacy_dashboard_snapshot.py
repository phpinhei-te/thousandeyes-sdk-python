# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class LegacyDashboardSnapshot(BaseModel):
    """
    LegacyDashboardSnapshot
    """ # noqa: E501
    account_id: Optional[StrictInt] = Field(default=None, description="Identifier of the account group that the snapshot belongs to.", alias="accountId")
    created_date: Optional[StrictStr] = Field(default=None, description="UTC date when dashboard snapshot was created.", alias="createdDate")
    expiration_date: Optional[StrictStr] = Field(default=None, description="Expiration date of the snapshot. If unspecified, the snapshot expires 1 year from its creation date. The expiration date must be set within 5 years from the current date.", alias="expirationDate")
    permalink: Optional[StrictStr] = Field(default=None, description="Hyperlink to dashboard snapshot in ThousandEyes Application")
    api_links: Optional[List[Dict[str, Any]]] = Field(default=None, description="A links array containing the self link.", alias="apiLinks")
    __properties: ClassVar[List[str]] = ["accountId", "createdDate", "expirationDate", "permalink", "apiLinks"]

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
        """Create an instance of LegacyDashboardSnapshot from a JSON string"""
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
        """Create an instance of LegacyDashboardSnapshot from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountId": obj.get("accountId"),
            "createdDate": obj.get("createdDate"),
            "expirationDate": obj.get("expirationDate"),
            "permalink": obj.get("permalink"),
            "apiLinks": obj.get("apiLinks")
        })
        return _obj


