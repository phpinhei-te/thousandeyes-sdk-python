# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.   For more information about Endpoint Agents, see [Endpoint Agents](https://docs.thousandeyes.com/product-documentation/global-vantage-points/endpoint-agents).

    The version of the OpenAPI document: 7.0.8
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Platform(str, Enum):
    """
    OS platform types
    """

    """
    allowed enum values
    """
    WINDOWS = 'windows'
    LINUX = 'linux'
    MAC = 'mac'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Platform from a JSON string"""
        return cls(json.loads(json_str))


