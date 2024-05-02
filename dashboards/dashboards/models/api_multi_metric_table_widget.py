# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dashboards.models.api_aggregate_property import ApiAggregateProperty
from dashboards.models.api_duration import ApiDuration
from dashboards.models.api_multi_metric_column import ApiMultiMetricColumn
from dashboards.models.api_widget_measure import ApiWidgetMeasure
from dashboards.models.dashboard_metric import DashboardMetric
from dashboards.models.dashboard_metric_direction import DashboardMetricDirection
from dashboards.models.legacy_widget_sort_direction import LegacyWidgetSortDirection
from dashboards.models.legacy_widget_sort_property import LegacyWidgetSortProperty
from dashboards.models.metric_group import MetricGroup
from dashboards.models.multi_metrics_table_datasource import MultiMetricsTableDatasource
from dashboards.models.self_links_links import SelfLinksLinks
from dashboards.models.visual_mode import VisualMode
from typing import Optional, Set
from typing_extensions import Self

class ApiMultiMetricTableWidget(BaseModel):
    """
    A Multi-Metric table widget with columns, each representing a different metric, offering a comprehensive view rather than restricting to a single metric.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Identifier of the widget.")
    title: Optional[StrictStr] = Field(default=None, description="Title of the widget")
    visual_mode: Optional[VisualMode] = Field(default=None, alias="visualMode")
    embed_url: Optional[StrictStr] = Field(default=None, description="When `isEmbedded` is set to `true`, an `embedUrl` is provided.", alias="embedUrl")
    is_embedded: Optional[StrictBool] = Field(default=None, description="Set to `true` if widget is marked as embedded; otherwise, set to `false`.", alias="isEmbedded")
    metric_group: Optional[MetricGroup] = Field(default=None, alias="metricGroup")
    direction: Optional[DashboardMetricDirection] = None
    metric: Optional[DashboardMetric] = None
    filters: Optional[Dict[str, List[Any]]] = Field(default=None, description="(Optional) Specifies the filters applied to the widget. When present, the `filters` property displays. Each filter object has two properties: `filterProperty` and `filterValue`. The `filterProperty` can be values like `AGENT`, `ENDPOINT_MACHINE_ID`, `TEST`, `MONITOR`, etc.  The `filterValue` represents an identifier array of the selected property.")
    measure: Optional[ApiWidgetMeasure] = None
    fixed_timespan: Optional[ApiDuration] = Field(default=None, alias="fixedTimespan")
    api_link: Optional[StrictStr] = Field(default=None, alias="apiLink")
    should_exclude_alert_suppression_windows: Optional[StrictBool] = Field(default=None, description="Excludes alert suppression window data if set to `true`.", alias="shouldExcludeAlertSuppressionWindows")
    links: Optional[SelfLinksLinks] = Field(default=None, alias="_links")
    type: Annotated[str, Field(strict=True)] = Field(description="Multi Metric Table widget type.")
    compare_to_previous_value: Optional[StrictBool] = Field(default=None, description="Enables comparison of the current metric value with the previous value.", alias="compareToPreviousValue")
    row_group_by: Optional[ApiAggregateProperty] = Field(default=None, alias="rowGroupBy")
    sort_by: Optional[LegacyWidgetSortProperty] = Field(default=None, alias="sortBy")
    sort_direction: Optional[LegacyWidgetSortDirection] = Field(default=None, alias="sortDirection")
    limit: Optional[StrictInt] = Field(default=None, description="Limit configured in the widget.")
    multi_metric_columns: Optional[List[ApiMultiMetricColumn]] = Field(default=None, alias="multiMetricColumns")
    data_source: Optional[MultiMetricsTableDatasource] = Field(default=None, alias="dataSource")
    __properties: ClassVar[List[str]] = ["id", "title", "visualMode", "embedUrl", "isEmbedded", "metricGroup", "direction", "metric", "filters", "measure", "fixedTimespan", "apiLink", "shouldExcludeAlertSuppressionWindows", "_links", "type", "compareToPreviousValue", "rowGroupBy", "sortBy", "sortDirection", "limit", "multiMetricColumns", "dataSource"]

    @field_validator('type')
    def type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^Multi Metric Table$", value):
            raise ValueError(r"must validate the regular expression /^Multi Metric Table$/")
        return value

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
        """Create an instance of ApiMultiMetricTableWidget from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "id",
            "embed_url",
            "api_link",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of measure
        if self.measure:
            _dict['measure'] = self.measure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fixed_timespan
        if self.fixed_timespan:
            _dict['fixedTimespan'] = self.fixed_timespan.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in multi_metric_columns (list)
        _items = []
        if self.multi_metric_columns:
            for _item in self.multi_metric_columns:
                if _item:
                    _items.append(_item.to_dict())
            _dict['multiMetricColumns'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiMultiMetricTableWidget from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "visualMode": obj.get("visualMode"),
            "embedUrl": obj.get("embedUrl"),
            "isEmbedded": obj.get("isEmbedded"),
            "metricGroup": obj.get("metricGroup"),
            "direction": obj.get("direction"),
            "metric": obj.get("metric"),
            "filters": obj.get("filters"),
            "measure": ApiWidgetMeasure.from_dict(obj["measure"]) if obj.get("measure") is not None else None,
            "fixedTimespan": ApiDuration.from_dict(obj["fixedTimespan"]) if obj.get("fixedTimespan") is not None else None,
            "apiLink": obj.get("apiLink"),
            "shouldExcludeAlertSuppressionWindows": obj.get("shouldExcludeAlertSuppressionWindows"),
            "_links": SelfLinksLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "type": obj.get("type"),
            "compareToPreviousValue": obj.get("compareToPreviousValue"),
            "rowGroupBy": obj.get("rowGroupBy"),
            "sortBy": obj.get("sortBy"),
            "sortDirection": obj.get("sortDirection"),
            "limit": obj.get("limit"),
            "multiMetricColumns": [ApiMultiMetricColumn.from_dict(_item) for _item in obj["multiMetricColumns"]] if obj.get("multiMetricColumns") is not None else None,
            "dataSource": obj.get("dataSource")
        })
        return _obj


