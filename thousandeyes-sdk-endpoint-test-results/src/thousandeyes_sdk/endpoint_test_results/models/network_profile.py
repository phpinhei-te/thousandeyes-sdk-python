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
from thousandeyes_sdk.endpoint_test_results.models.ethernet_profile import EthernetProfile
from thousandeyes_sdk.endpoint_test_results.models.interface_hardware_type import InterfaceHardwareType
from thousandeyes_sdk.endpoint_test_results.models.network_interface import NetworkInterface
from thousandeyes_sdk.endpoint_test_results.models.network_proxy_profile import NetworkProxyProfile
from thousandeyes_sdk.endpoint_test_results.models.network_wireless_profile import NetworkWirelessProfile
from typing import Optional, Set
from typing_extensions import Self

class NetworkProfile(BaseModel):
    """
    NetworkProfile
    """ # noqa: E501
    ip_address: Optional[StrictStr] = Field(default=None, description="Network IP address.", alias="ipAddress")
    subnet_mask: Optional[StrictStr] = Field(default=None, description="Network subnet mask - only for IPv4.", alias="subnetMask")
    public_ip_address: Optional[StrictStr] = Field(default=None, description="Network public IP address.", alias="publicIpAddress")
    local_prefix: Optional[StrictStr] = Field(default=None, description="Network local prefix.", alias="localPrefix")
    public_ip_range: Optional[StrictStr] = Field(default=None, description="Network public IP range.", alias="publicIpRange")
    dns_servers: Optional[List[StrictStr]] = Field(default=None, description="Network DNS servers.", alias="dnsServers")
    hardware_type: Optional[InterfaceHardwareType] = Field(default=None, alias="hardwareType")
    interface_name: Optional[StrictStr] = Field(default=None, description="Network interface name.", alias="interfaceName")
    error: Optional[StrictStr] = Field(default=None, description="Only present when there is an error")
    gateway: Optional[StrictStr] = Field(default=None, description="Network gateway address.")
    wireless_profile: Optional[NetworkWirelessProfile] = Field(default=None, alias="wirelessProfile")
    proxy_profile: Optional[NetworkProxyProfile] = Field(default=None, alias="proxyProfile")
    ethernet_profile: Optional[EthernetProfile] = Field(default=None, alias="ethernetProfile")
    previous_interface: Optional[NetworkInterface] = Field(default=None, alias="previousInterface")
    __properties: ClassVar[List[str]] = ["ipAddress", "subnetMask", "publicIpAddress", "localPrefix", "publicIpRange", "dnsServers", "hardwareType", "interfaceName", "error", "gateway", "wirelessProfile", "proxyProfile", "ethernetProfile", "previousInterface"]

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
        """Create an instance of NetworkProfile from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "ip_address",
            "subnet_mask",
            "public_ip_address",
            "local_prefix",
            "public_ip_range",
            "dns_servers",
            "interface_name",
            "error",
            "gateway",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of wireless_profile
        if self.wireless_profile:
            _dict['wirelessProfile'] = self.wireless_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of proxy_profile
        if self.proxy_profile:
            _dict['proxyProfile'] = self.proxy_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ethernet_profile
        if self.ethernet_profile:
            _dict['ethernetProfile'] = self.ethernet_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of previous_interface
        if self.previous_interface:
            _dict['previousInterface'] = self.previous_interface.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetworkProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ipAddress": obj.get("ipAddress"),
            "subnetMask": obj.get("subnetMask"),
            "publicIpAddress": obj.get("publicIpAddress"),
            "localPrefix": obj.get("localPrefix"),
            "publicIpRange": obj.get("publicIpRange"),
            "dnsServers": obj.get("dnsServers"),
            "hardwareType": obj.get("hardwareType"),
            "interfaceName": obj.get("interfaceName"),
            "error": obj.get("error"),
            "gateway": obj.get("gateway"),
            "wirelessProfile": NetworkWirelessProfile.from_dict(obj["wirelessProfile"]) if obj.get("wirelessProfile") is not None else None,
            "proxyProfile": NetworkProxyProfile.from_dict(obj["proxyProfile"]) if obj.get("proxyProfile") is not None else None,
            "ethernetProfile": EthernetProfile.from_dict(obj["ethernetProfile"]) if obj.get("ethernetProfile") is not None else None,
            "previousInterface": NetworkInterface.from_dict(obj["previousInterface"]) if obj.get("previousInterface") is not None else None
        })
        return _obj


