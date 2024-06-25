# coding: utf-8

"""
    Administrative API

    Manage users, accounts, and account groups in the ThousandEyes platform using the Administrative API. This API provides the following endpoints that define the operations to manage your organization:     * `/account-groups`: Account groups are used to divide an organization into different sections. These endpoints can be used to create, retrieve, update and delete account groups.   * `/users`: Create, retrieve, update and delete users within an organization.    * `/roles`: Create, retrieve and update roles for the current user.    * `/permissions`: Retrieve all assignable permissions. Used in the context of modifying roles.    * `/audit-user-events`: Retrieve all activity log events.    For more information about the administrative models, see [Account Management](https://docs.thousandeyes.com/product-documentation/user-management).

    The version of the OpenAPI document: 7.0.8
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class EnterpriseAgentIpv6Policy(str, Enum):
    """
    IP version policy, (Enterprise Agents and Enterprise Clusters only)
    """

    """
    allowed enum values
    """
    FORCE_MINUS_IPV4 = 'force-ipv4'
    PREFER_MINUS_IPV6 = 'prefer-ipv6'
    FORCE_MINUS_IPV6 = 'force-ipv6'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EnterpriseAgentIpv6Policy from a JSON string"""
        return cls(json.loads(json_str))


