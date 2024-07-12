# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.endpoint_test_results.models.network_ping import NetworkPing
from thousandeyes_sdk.endpoint_test_results.models.network_topology_type import NetworkTopologyType
from thousandeyes_sdk.endpoint_test_results.models.system_metrics import SystemMetrics
from thousandeyes_sdk.endpoint_test_results.models.tcp_connect import TcpConnect
from typing import Optional, Set
from typing_extensions import Self

class LocalNetworkTopologyResultBase(BaseModel):
    """
    LocalNetworkTopologyResultBase
    """ # noqa: E501
    agent_id: Optional[StrictStr] = Field(default=None, description="Unique ID of endpoint agent, from `/endpoint/agents` endpoint.", alias="agentId")
    var_date: Optional[datetime] = Field(default=None, description="UTC date when endpoint network topology took place (ISO date-time format).", alias="date")
    network_topology_id: Optional[StrictStr] = Field(default=None, description="Network topology ID. Each network topology occurrence has a unique ID.", alias="networkTopologyId")
    round_id: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round.", alias="roundId")
    target: Optional[StrictStr] = Field(default=None, description="IP of the target the network topology was performed against. This is typically a default gateway, proxy or VPN endpoint.")
    target_port: Optional[StrictInt] = Field(default=None, description="Port of the target the network topology was performed against.", alias="targetPort")
    type: Optional[NetworkTopologyType] = None
    icmp_ping: Optional[NetworkPing] = Field(default=None, alias="icmpPing")
    is_icmp_blocked: Optional[StrictBool] = Field(default=None, description="Set to `true` if network target is blocking ICMP echo (ping) queries.", alias="isIcmpBlocked")
    tcp_connect: Optional[TcpConnect] = Field(default=None, alias="tcpConnect")
    system_metrics: Optional[SystemMetrics] = Field(default=None, alias="systemMetrics")
    __properties: ClassVar[List[str]] = ["agentId", "date", "networkTopologyId", "roundId", "target", "targetPort", "type", "icmpPing", "isIcmpBlocked", "tcpConnect", "systemMetrics"]

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
        """Create an instance of LocalNetworkTopologyResultBase from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "agent_id",
            "var_date",
            "network_topology_id",
            "round_id",
            "target",
            "target_port",
            "is_icmp_blocked",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of icmp_ping
        if self.icmp_ping:
            _dict['icmpPing'] = self.icmp_ping.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tcp_connect
        if self.tcp_connect:
            _dict['tcpConnect'] = self.tcp_connect.to_dict()
        # override the default output from pydantic by calling `to_dict()` of system_metrics
        if self.system_metrics:
            _dict['systemMetrics'] = self.system_metrics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LocalNetworkTopologyResultBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agentId": obj.get("agentId"),
            "date": obj.get("date"),
            "networkTopologyId": obj.get("networkTopologyId"),
            "roundId": obj.get("roundId"),
            "target": obj.get("target"),
            "targetPort": obj.get("targetPort"),
            "type": obj.get("type"),
            "icmpPing": NetworkPing.from_dict(obj["icmpPing"]) if obj.get("icmpPing") is not None else None,
            "isIcmpBlocked": obj.get("isIcmpBlocked"),
            "tcpConnect": TcpConnect.from_dict(obj["tcpConnect"]) if obj.get("tcpConnect") is not None else None,
            "systemMetrics": SystemMetrics.from_dict(obj["systemMetrics"]) if obj.get("systemMetrics") is not None else None
        })
        return _obj


