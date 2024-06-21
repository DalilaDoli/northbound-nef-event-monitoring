


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated

from typing import Optional, Set
from typing_extensions import Self

from models.applied_parameter_configuration import AppliedParameterConfiguration
from models.config_result import ConfigResult
from models.monitoring_event_report import MonitoringEventReport

class MonitoringNotification(BaseModel):
    
    subscription: StrictStr = Field(description="string formatted according to IETF RFC 3986 identifying a referenced resource.")
    config_results: Optional[Annotated[List[Optional[ConfigResult]], Field(min_length=1)]] = Field(default=None, description="Each element identifies a notification of grouping configuration result.", alias="configResults")
    monitoring_event_reports: Optional[Annotated[List[MonitoringEventReport], Field(min_length=1)]] = Field(default=None, description="Monitoring event reports.", alias="monitoringEventReports")
    added_external_ids: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Identifies the added external Identifier(s) within the active group via the \"externalGroupId\" attribute within the MonitoringEventSubscription data type. ", alias="addedExternalIds")
    added_msisdns: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Identifies the added MSISDN(s) within the active group via the \"externalGroupId\" attribute within the MonitoringEventSubscription data type. ", alias="addedMsisdns")
    cancel_external_ids: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Identifies the cancelled external Identifier(s) within the active group via the \"externalGroupId\" attribute within the MonitoringEventSubscription data type. ", alias="cancelExternalIds")
    cancel_msisdns: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Identifies the cancelled MSISDN(s) within the active group via the \"externalGroupId\" attribute within the MonitoringEventSubscription data type. ", alias="cancelMsisdns")
    cancel_ind: Optional[StrictBool] = Field(default=None, description="Indicates whether to request to cancel the corresponding monitoring subscription. Set to false or omitted otherwise. ", alias="cancelInd")
    applied_param: Optional[AppliedParameterConfiguration] = Field(default=None, alias="appliedParam")
    __properties: ClassVar[List[str]] = ["subscription", "configResults", "monitoringEventReports", "addedExternalIds", "addedMsisdns", "cancelExternalIds", "cancelMsisdns", "cancelInd", "appliedParam"]
