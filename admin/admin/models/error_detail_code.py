# coding: utf-8

"""
    Administrative API

    ## Overview Manage users, accounts, and account groups in the ThousandEyes platform using the Administrative API. This API provides the following endpoints that define the operations to manage your organization:     * `/account-groups`: Account groups are used to divide an organization into different sections. These endpoints can be used to create, retrieve, update and delete account groups.   * `/users`: Create, retrieve, update and delete users within an organization.    * `/roles`: Create, retrieve and update roles for the current user.    * `/permissions`: Retrieve all assignable permissions. Used in the context of modifying roles.    * `/audit-user-events`: Retrieve all activity log events.    For more information about the administrative models, see [Account Management](https://docs.thousandeyes.com/product-documentation/user-management).

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ErrorDetailCode(str, Enum):
    """
    Code for the agent error.
    """

    """
    allowed enum values
    """
    AGENT_MINUS_VERSION_MINUS_OUTDATED = 'agent-version-outdated'
    BROWSERBOT_MINUS_VERSION_MINUS_OUTDATED = 'browserbot-version-outdated'
    APPLIANCE_MINUS_VERSION_MINUS_OUTDATED = 'appliance-version-outdated'
    CLOCK_MINUS_OFFSET = 'clock-offset'
    OS_MINUS_END_MINUS_OF_MINUS_INSTALLATION_MINUS_SUPPORT = 'os-end-of-installation-support'
    OS_MINUS_END_MINUS_OF_MINUS_SUPPORT = 'os-end-of-support'
    OS_MINUS_END_MINUS_OF_MINUS_LIFE = 'os-end-of-life'
    NAT_MINUS_TRAVERSAL_MINUS_ERROR = 'nat-traversal-error'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ErrorDetailCode from a JSON string"""
        return cls(json.loads(json_str))


