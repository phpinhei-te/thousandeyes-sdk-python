# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

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

class NetworkWirelessProfile(BaseModel):
    """
    NetworkWirelessProfile
    """ # noqa: E501
    ssid: Optional[StrictStr] = Field(default=None, description="Wireless network SSID.")
    bssid: Optional[StrictStr] = Field(default=None, description="Wireless network BSSID.")
    channel: Optional[StrictInt] = Field(default=None, description="Wireless network channel.")
    phy_mode: Optional[StrictStr] = Field(default=None, description="Wireless network PHY mode.", alias="phyMode")
    rssi: Optional[StrictInt] = Field(default=None, description="Wireless network RSSI.")
    noise: Optional[StrictInt] = Field(default=None, description="Wireless network noise.")
    quality: Optional[StrictInt] = Field(default=None, description="Wireless network quality.")
    tx_rate: Optional[StrictInt] = Field(default=None, description="Wireless network transmitted rate.", alias="txRate")
    vendor: Optional[StrictStr] = Field(default=None, description="Wireless network device vendor.")
    __properties: ClassVar[List[str]] = ["ssid", "bssid", "channel", "phyMode", "rssi", "noise", "quality", "txRate", "vendor"]

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
        """Create an instance of NetworkWirelessProfile from a JSON string"""
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
            "ssid",
            "bssid",
            "channel",
            "phy_mode",
            "rssi",
            "noise",
            "quality",
            "tx_rate",
            "vendor",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetworkWirelessProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ssid": obj.get("ssid"),
            "bssid": obj.get("bssid"),
            "channel": obj.get("channel"),
            "phyMode": obj.get("phyMode"),
            "rssi": obj.get("rssi"),
            "noise": obj.get("noise"),
            "quality": obj.get("quality"),
            "txRate": obj.get("txRate"),
            "vendor": obj.get("vendor")
        })
        return _obj


