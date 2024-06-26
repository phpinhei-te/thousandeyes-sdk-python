# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.8
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class LegacyApiDashboard(BaseModel):
    """
    LegacyApiDashboard
    """ # noqa: E501
    account_id: Optional[StrictInt] = Field(default=None, description="Identifier for the account group associated with a dashboard.", alias="accountId")
    created_by: Optional[StrictInt] = Field(default=None, description="Identifier for the user that created a dashboard.", alias="createdBy")
    modified_by: Optional[StrictInt] = Field(default=None, description="Identifier for the user that last modified a dashboard.", alias="modifiedBy")
    modified_date: Optional[StrictStr] = Field(default=None, description="UTC date/time when a dashboard was last modified.", alias="modifiedDate")
    global_override: Optional[StrictBool] = Field(default=None, description="When set to `true`, the defaultTimespan is used and overrides the widget's timespan. If set to `false`, the the widget's timespan is used.", alias="globalOverride")
    migrated_report: Optional[StrictBool] = Field(default=None, description="True if this dashboard was previously a report.", alias="migratedReport")
    api_link: Optional[List[Dict[str, Any]]] = Field(default=None, description="A links array containing the self and the snapshots links.", alias="apiLink")
    __properties: ClassVar[List[str]] = ["accountId", "createdBy", "modifiedBy", "modifiedDate", "globalOverride", "migratedReport", "apiLink"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return self.model_dump_json(by_alias=True, exclude_unset=True, exclude_none=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of LegacyApiDashboard from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "account_id",
            "created_by",
            "modified_by",
            "modified_date",
            "migrated_report",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LegacyApiDashboard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountId": obj.get("accountId"),
            "createdBy": obj.get("createdBy"),
            "modifiedBy": obj.get("modifiedBy"),
            "modifiedDate": obj.get("modifiedDate"),
            "globalOverride": obj.get("globalOverride"),
            "migratedReport": obj.get("migratedReport"),
            "apiLink": obj.get("apiLink")
        })
        return _obj


