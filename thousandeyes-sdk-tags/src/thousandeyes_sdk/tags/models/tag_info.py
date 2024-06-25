# coding: utf-8

"""
    Tags API

    The ThousandEyes Tags API provides a tagging system with key/value pairs. It allows you to tag assets within the ThousandEyes platform (such as agents, tests, or alert rules) with meaningful metadata. For example: `branch:sfo`, `branch:nyc`, and `team:netops`.  This feature provides:  * Support for automation. * Powerful and flexible reports/dashboards. * Support for third-party integrations.  Things to note with the ThousandEyes Tags API:  * Tags are backwards-compatible with existing labels. * Tags are separated by Tests (CEA), Agents (CEA), Endpoint Agents, Scheduled Endpoint Tests, and Reports. A single tag can only apply to one type of target object, so each tag must specify the target type of object via a `type` field. * Tags are defined in a single table so that they can be represented using a single model - `Tag`. 

    The version of the OpenAPI document: 7.0.8
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.tags.models.access_type import AccessType
from thousandeyes_sdk.tags.models.assignment import Assignment
from thousandeyes_sdk.tags.models.object_type import ObjectType
from typing import Optional, Set
from typing_extensions import Self

class TagInfo(BaseModel):
    """
    TagInfo
    """ # noqa: E501
    assignments: Optional[List[Assignment]] = None
    access_type: Optional[AccessType] = Field(default=None, alias="accessType")
    aid: Optional[StrictInt] = Field(default=None, description="The account group ID")
    color: Optional[StrictStr] = Field(default=None, description="Tag color")
    create_date: Optional[StrictStr] = Field(default=None, description="Tag creation date", alias="createDate")
    icon: Optional[StrictStr] = None
    id: Optional[StrictStr] = Field(default=None, description="The tag ID")
    key: Optional[StrictStr] = Field(default=None, description="The tags's key")
    legacy_id: Optional[StrictStr] = Field(default=None, alias="legacyId")
    object_type: Optional[ObjectType] = Field(default=None, alias="objectType")
    value: Optional[StrictStr] = Field(default=None, description="The tag's value")
    __properties: ClassVar[List[str]] = ["assignments", "accessType", "aid", "color", "createDate", "icon", "id", "key", "legacyId", "objectType", "value"]

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
        """Create an instance of TagInfo from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "assignments",
            "aid",
            "create_date",
            "icon",
            "id",
            "legacy_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in assignments (list)
        _items = []
        if self.assignments:
            for _item in self.assignments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['assignments'] = _items
        # set to None if icon (nullable) is None
        # and model_fields_set contains the field
        if self.icon is None and "icon" in self.model_fields_set:
            _dict['icon'] = None

        # set to None if legacy_id (nullable) is None
        # and model_fields_set contains the field
        if self.legacy_id is None and "legacy_id" in self.model_fields_set:
            _dict['legacyId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TagInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assignments": [Assignment.from_dict(_item) for _item in obj["assignments"]] if obj.get("assignments") is not None else None,
            "accessType": obj.get("accessType"),
            "aid": obj.get("aid"),
            "color": obj.get("color"),
            "createDate": obj.get("createDate"),
            "icon": obj.get("icon"),
            "id": obj.get("id"),
            "key": obj.get("key"),
            "legacyId": obj.get("legacyId"),
            "objectType": obj.get("objectType"),
            "value": obj.get("value")
        })
        return _obj


