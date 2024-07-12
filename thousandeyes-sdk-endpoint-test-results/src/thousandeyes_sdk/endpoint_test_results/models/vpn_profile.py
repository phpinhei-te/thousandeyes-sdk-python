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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.endpoint_test_results.models.vpn_type import VpnType
from typing import Optional, Set
from typing_extensions import Self

class VpnProfile(BaseModel):
    """
    VpnProfile
    """ # noqa: E501
    vpn_client_addresses: Optional[List[StrictStr]] = Field(default=None, description="A list of private IP addresses assigned to the device by the VPN server.", alias="vpnClientAddresses")
    vpn_client_network_range: Optional[List[StrictStr]] = Field(default=None, description="A list of private networks assigned to the device by the VPN server.", alias="vpnClientNetworkRange")
    vpn_gateway_address: Optional[StrictStr] = Field(default=None, description="IP address of the VPN gateway.", alias="vpnGatewayAddress")
    vpn_type: Optional[VpnType] = Field(default=None, alias="vpnType")
    __properties: ClassVar[List[str]] = ["vpnClientAddresses", "vpnClientNetworkRange", "vpnGatewayAddress", "vpnType"]

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
        """Create an instance of VpnProfile from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "vpn_client_addresses",
            "vpn_client_network_range",
            "vpn_gateway_address",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VpnProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "vpnClientAddresses": obj.get("vpnClientAddresses"),
            "vpnClientNetworkRange": obj.get("vpnClientNetworkRange"),
            "vpnGatewayAddress": obj.get("vpnGatewayAddress"),
            "vpnType": obj.get("vpnType")
        })
        return _obj


