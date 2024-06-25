# coding: utf-8

"""
    Labels API

    ### Overview This is API for the Labels API (formerly called groups).

    The version of the OpenAPI document: 7.0.8
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class LabelType(str, Enum):
    """
    Either `test`, `agent`, `endpoint-test`, `endpoint-agent` or `dashboard`, indicates the type of label.
    """

    """
    allowed enum values
    """
    AGENT = 'agent'
    TEST = 'test'
    ENDPOINT_MINUS_AGENT = 'endpoint-agent'
    ENDPOINT_MINUS_TEST = 'endpoint-test'
    DASHBOARD = 'dashboard'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LabelType from a JSON string"""
        return cls(json.loads(json_str))


