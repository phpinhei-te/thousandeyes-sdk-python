# coding: utf-8

"""
    Endpoint Instant Scheduled Tests API

     You can create and execute a new endpoint instant scheduled test within ThousandEyes using this API. The test parameters are specified in the `POST` data.  The following applies to the Endpoint Instant Scheduled Tests API:  * To initiate the creation and execution of an instant scheduled test, the user must possess the `Edit endpoint tests` permission.  * Upon successful creation of an instant scheduled test, the API responds with an HTTP/201 CREATED status code and return the test definition. * It's important to note that the response does not include the results of the instant scheduled test. To retrieve test results, users can utilize the Endpoint Test Data endpoints. The URLs for these API test data endpoints are provided within the test definition output when an instant scheduled test is created. 

    The version of the OpenAPI document: 7.0.8
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AlertDirection(str, Enum):
    """
    Direction for applicable alert types (eg. path trace, End-to-End (Agent) etc.)
    """

    """
    allowed enum values
    """
    TO_MINUS_TARGET = 'to-target'
    FROM_MINUS_TARGET = 'from-target'
    BIDIRECTIONAL = 'bidirectional'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AlertDirection from a JSON string"""
        return cls(json.loads(json_str))


