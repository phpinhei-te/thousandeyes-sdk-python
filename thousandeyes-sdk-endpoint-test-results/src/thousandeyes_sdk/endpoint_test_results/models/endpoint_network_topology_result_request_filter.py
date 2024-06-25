# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.8
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.endpoint_test_results.models.interface_hardware_type import InterfaceHardwareType
from thousandeyes_sdk.endpoint_test_results.models.network_topology_type import NetworkTopologyType
from thousandeyes_sdk.endpoint_test_results.models.platform import Platform
from typing import Optional, Set
from typing_extensions import Self

class EndpointNetworkTopologyResultRequestFilter(BaseModel):
    """
    EndpointNetworkTopologyResultRequestFilter
    """ # noqa: E501
    location: Optional[List[StrictStr]] = Field(default=None, description="Location of the endpoint agent.")
    connection: Optional[List[InterfaceHardwareType]] = None
    platform: Optional[List[Platform]] = None
    gateway: Optional[List[StrictStr]] = Field(default=None, description="Endpoint agent default gateway IP address.")
    proxy_target: Optional[List[StrictStr]] = Field(default=None, description="Endpoint agent proxy IP address.", alias="proxyTarget")
    vpn_target: Optional[List[StrictStr]] = Field(default=None, description="Endpoint agent VPN endpoint IP address.", alias="vpnTarget")
    agent_id: Optional[List[StrictStr]] = Field(default=None, description="Endpoint agent ID.", alias="agentId")
    network_id: Optional[List[StrictStr]] = Field(default=None, description="Network ID.", alias="networkId")
    ssid: Optional[List[StrictStr]] = Field(default=None, description="WiFi SSID.")
    bssid: Optional[List[StrictStr]] = Field(default=None, description="WiFi BSSID.")
    type: Optional[List[NetworkTopologyType]] = Field(default=None, description="Web site base domain visited during the session.")
    __properties: ClassVar[List[str]] = ["location", "connection", "platform", "gateway", "proxyTarget", "vpnTarget", "agentId", "networkId", "ssid", "bssid", "type"]

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
        """Create an instance of EndpointNetworkTopologyResultRequestFilter from a JSON string"""
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
        """Create an instance of EndpointNetworkTopologyResultRequestFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "location": obj.get("location"),
            "connection": obj.get("connection"),
            "platform": obj.get("platform"),
            "gateway": obj.get("gateway"),
            "proxyTarget": obj.get("proxyTarget"),
            "vpnTarget": obj.get("vpnTarget"),
            "agentId": obj.get("agentId"),
            "networkId": obj.get("networkId"),
            "ssid": obj.get("ssid"),
            "bssid": obj.get("bssid"),
            "type": obj.get("type")
        })
        return _obj


