# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from test_results.models.agent import Agent
from typing import Optional, Set
from typing_extensions import Self

class FtpServerTestResult(BaseModel):
    """
    FtpServerTestResult
    """ # noqa: E501
    var_date: Optional[datetime] = Field(default=None, description="Data point date UTC (ISO date-time format).", alias="date")
    round_id: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round", alias="roundId")
    links: Optional[Dict[str, Any]] = Field(default=None, alias="_links")
    start_time: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round", alias="startTime")
    end_time: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the end time of the round", alias="endTime")
    agent: Optional[Agent] = None
    server_ip: Optional[StrictStr] = Field(default=None, description="IP address of destination server", alias="serverIp")
    response_code: Optional[StrictInt] = Field(default=None, description="FTP response code", alias="responseCode")
    dns_time: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Time required to resolve DNS  in milliseconds", alias="dnsTime")
    connect_time: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Time required to establish a TCP connection to the server in milliseconds", alias="connectTime")
    negotiation_time: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Time negotiate the connection and authenticate with the destination server in milliseconds", alias="negotiationTime")
    wait_time: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Time elapsed between completion of request and first byte of response in milliseconds", alias="waitTime")
    response_time: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Sum of DNS, connect, negotiation and wait times in milliseconds", alias="responseTime")
    transfer_time: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Elapsed time between first and last byte of the transfer in milliseconds", alias="transferTime")
    wire_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Size of content in bytes", alias="wireSize")
    total_time: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Sum of response + transfer time in milliseconds", alias="totalTime")
    error_type: Optional[StrictStr] = Field(default=None, description="Type of error encountered; corresponds to phase of connection", alias="errorType")
    error_details: Optional[StrictStr] = Field(default=None, description="Error details, if an error were encountered", alias="errorDetails")
    throughput: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="WireSize divided by receiveTime in byter per second")
    __properties: ClassVar[List[str]] = ["date", "roundId", "_links", "startTime", "endTime", "agent", "serverIp", "responseCode", "dnsTime", "connectTime", "negotiationTime", "waitTime", "responseTime", "transferTime", "wireSize", "totalTime", "errorType", "errorDetails", "throughput"]

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
        """Create an instance of FtpServerTestResult from a JSON string"""
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
            "var_date",
            "round_id",
            "start_time",
            "end_time",
            "server_ip",
            "response_code",
            "dns_time",
            "connect_time",
            "negotiation_time",
            "wait_time",
            "response_time",
            "transfer_time",
            "wire_size",
            "total_time",
            "error_type",
            "error_details",
            "throughput",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of agent
        if self.agent:
            _dict['agent'] = self.agent.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FtpServerTestResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "roundId": obj.get("roundId"),
            "_links": obj.get("_links"),
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime"),
            "agent": Agent.from_dict(obj["agent"]) if obj.get("agent") is not None else None,
            "serverIp": obj.get("serverIp"),
            "responseCode": obj.get("responseCode"),
            "dnsTime": obj.get("dnsTime"),
            "connectTime": obj.get("connectTime"),
            "negotiationTime": obj.get("negotiationTime"),
            "waitTime": obj.get("waitTime"),
            "responseTime": obj.get("responseTime"),
            "transferTime": obj.get("transferTime"),
            "wireSize": obj.get("wireSize"),
            "totalTime": obj.get("totalTime"),
            "errorType": obj.get("errorType"),
            "errorDetails": obj.get("errorDetails"),
            "throughput": obj.get("throughput")
        })
        return _obj


