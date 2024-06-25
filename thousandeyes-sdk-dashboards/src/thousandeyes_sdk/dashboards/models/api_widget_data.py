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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.dashboards.models.api_report_data_component_label_map import ApiReportDataComponentLabelMap
from thousandeyes_sdk.dashboards.models.api_widgets_data_v2 import ApiWidgetsDataV2
from typing import Optional, Set
from typing_extensions import Self

class ApiWidgetData(BaseModel):
    """
    Response of a widget data request.
    """ # noqa: E501
    group_labels: Optional[List[ApiReportDataComponentLabelMap]] = Field(default=None, alias="groupLabels")
    bin_size: Optional[StrictInt] = Field(default=None, description="Duration of each bin.", alias="binSize")
    data: Optional[ApiWidgetsDataV2] = None
    start_date: Optional[datetime] = Field(default=None, description="(Optional) When passing `window` or `startDate` parameter,  the client will also receive the `startDate` field indicating the UTC start date of the data's time range being retrieved  (ISO date-time format).", alias="startDate")
    end_date: Optional[datetime] = Field(default=None, description="(Optional) When passing `window` or `endDate` parameter,  the client will also receive the `endDate` field indicating the UTC end date of the data's time range being retrieved  (ISO date-time format).", alias="endDate")
    __properties: ClassVar[List[str]] = ["groupLabels", "binSize", "data", "startDate", "endDate"]

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
        """Create an instance of ApiWidgetData from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "start_date",
            "end_date",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in group_labels (list)
        _items = []
        if self.group_labels:
            for _item in self.group_labels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['groupLabels'] = _items
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiWidgetData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "groupLabels": [ApiReportDataComponentLabelMap.from_dict(_item) for _item in obj["groupLabels"]] if obj.get("groupLabels") is not None else None,
            "binSize": obj.get("binSize"),
            "data": ApiWidgetsDataV2.from_dict(obj["data"]) if obj.get("data") is not None else None,
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate")
        })
        return _obj


