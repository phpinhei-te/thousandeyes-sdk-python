# coding: utf-8

"""
    Internet Insights API

    We are happy to announce the release of the Internet Insights API set. This limited release includes endpoints that:  * Make our catalog provider and Internet outage data accessible to API users. * Provide access to advanced filtering, which is part of our next-generation API efforts to allow API users to fine-tune queries across all of our APIs in a consistent manner.  Internet Insights provide visibility into core Internet infrastructure, including ISPs, DNS providers, IaaS, CDNs , and SaaS providers. It tracks the macro-level impact of Internet events on individual users and enterprise networks connecting at the edge of the Internet. These events include Outages, Routing hijacks and leaks, DDoS attacks, And political interference, among others.  Future releases of the Internet Insights API set will further unlock access to core Internet Insights functionality, unlocking potential integrations to enrich customer process flows. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from internet_insights.models.outage_scope import OutageScope
from typing import Optional, Set
from typing_extensions import Self

class ApiOutageFilter(BaseModel):
    """
    Advanced filter query used to filter the response. Can filter on: - outageScope (all, affected tests (e.g. my tests only)). - providerName - interfaceNetwork - applicationName - startDate, endDate - window
    """ # noqa: E501
    start_date: Optional[StrictStr] = Field(default=None, description="Start of the time range. Must be paired with `endDate`.", alias="startDate")
    end_date: Optional[StrictStr] = Field(default=None, description="End of the time range. Must be paired with `startDate`.", alias="endDate")
    window: Optional[StrictStr] = Field(default=None, description="Specify a time period in the past for which to retrieve data. Alternative to specifying `startDate` and `endDate`.")
    outage_scope: Optional[OutageScope] = Field(default=None, alias="outageScope")
    provider_name: Optional[List[StrictStr]] = Field(default=None, description="The name used to identify the provider.", alias="providerName")
    application_name: Optional[List[StrictStr]] = Field(default=None, description="The name to identify the application.", alias="applicationName")
    interface_network: Optional[List[StrictStr]] = Field(default=None, description="The name of the ASN (Interface Network).", alias="interfaceNetwork")
    __properties: ClassVar[List[str]] = ["startDate", "endDate", "window", "outageScope", "providerName", "applicationName", "interfaceNetwork"]

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
        """Create an instance of ApiOutageFilter from a JSON string"""
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
        """Create an instance of ApiOutageFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "window": obj.get("window"),
            "outageScope": obj.get("outageScope"),
            "providerName": obj.get("providerName"),
            "applicationName": obj.get("applicationName"),
            "interfaceNetwork": obj.get("interfaceNetwork")
        })
        return _obj


