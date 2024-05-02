# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Trigger(str, Enum):
    """
    Trigger
    """

    """
    allowed enum values
    """
    AUTO = 'auto'
    USER = 'user'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Trigger from a JSON string"""
        return cls(json.loads(json_str))


