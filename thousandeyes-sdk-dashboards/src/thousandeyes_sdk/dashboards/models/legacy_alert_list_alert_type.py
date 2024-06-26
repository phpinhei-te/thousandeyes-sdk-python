# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.8
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class LegacyAlertListAlertType(str, Enum):
    """
    Name of the alert type
    """

    """
    allowed enum values
    """
    NETWORK_MINUS__END_MINUS_TO_MINUS_END_LEFT_PARENTHESIS_SERVER_RIGHT_PARENTHESIS = 'Network - End-to-End (Server)'
    NETWORK_MINUS__END_MINUS_TO_MINUS_END_LEFT_PARENTHESIS_AGENT_RIGHT_PARENTHESIS = 'Network - End-to-End (Agent)'
    NETWORK_MINUS__PATH_TRACE = 'Network - Path Trace'
    DNS_SERVER = 'DNS Server'
    DNS_TRACE = 'DNS Trace'
    DNSSEC = 'DNSSEC'
    DNS_PLUS__DOMAIN = 'DNS+ Domain'
    DNS_PLUS__SERVER = 'DNS+ Server'
    WEB_MINUS__HTTP_SERVER = 'Web - HTTP Server'
    WEB_MINUS__PAGE_LOAD = 'Web - Page Load'
    WEB_MINUS__TRANSACTION_LEFT_PARENTHESIS_CLASSIC_RIGHT_PARENTHESIS = 'Web - Transaction (Classic)'
    WEB_MINUS__TRANSACTION = 'Web - Transaction'
    WEB_MINUS__FTP_SERVER = 'Web - FTP Server'
    VOICE_MINUS__SIP_SERVER = 'Voice - SIP Server'
    VOICE_MINUS__RTP_STREAM = 'Voice - RTP Stream'
    DEVICE = 'Device'
    DEVICE_INTERFACE = 'Device Interface'
    ENDPOINT_MINUS__END_MINUS_TO_MINUS_END_LEFT_PARENTHESIS_SERVER_RIGHT_PARENTHESIS = 'Endpoint - End-to-End (Server)'
    ENDPOINT_WEB_MINUS__HTTP_SERVER = 'EndpointWeb - HTTP Server'
    ENDPOINT_MINUS__PATH_TRACE = 'Endpoint - Path Trace'
    BROWSER_SESSIONS_MINUS__AGENT = 'Browser Sessions - Agent'
    BROWSER_SESSIONS_MINUS__APPLICATION = 'Browser Sessions - Application'
    ROUTING_MINUS__BGP = 'Routing - BGP'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LegacyAlertListAlertType from a JSON string"""
        return cls(json.loads(json_str))


