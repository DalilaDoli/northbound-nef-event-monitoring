from datetime import datetime
from typing import Annotated, ClassVar, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

from models.MonitoringType import MonitoringType
from models.api_capability_info import ApiCapabilityInfo
from models.assication_type import AssociationType
from models.ddd_traffic_descriptor import DddTrafficDescriptor
from models.dl_data_delivery_status import DlDataDeliveryStatus
from models.failure_cause import FailureCause
from models.group_memb_list_changes import GroupMembListChanges
from models.idle_status_info import IdleStatusInfo
from models.location_failure_cause import LocationFailureCause
from models.location_info import LocationInfo
from models.pdn_connection_information import PdnConnectionInformation
from models.pdu_session_information import PduSessionInformation
from models.plmn_id import PlmnId
from models.reachability_type import ReachabilityType
from models.sac_event_status import SACEventStatus
from models.ue_per_location_report import UePerLocationReport


class MonitoringEventReport(BaseModel):
    imei_change: Optional[AssociationType] = Field(default=None, alias="imeiChange")
    external_id: Optional[StrictStr] = Field(default=None, description="String containing a local identifier followed by '@' and a domain identifier.")
    app_id: Optional[StrictStr] = Field(default=None, description="String providing an application identifier.", alias="appId")
    pdu_sess_info: Optional[PduSessionInformation] = Field(default=None, alias="pduSessInfo")
    idle_status_info: Optional[IdleStatusInfo] = Field(default=None, alias="idleStatusInfo")
    location_info: Optional[LocationInfo] = Field(default=None, alias="locationInfo")
    loc_failure_cause: Optional[LocationFailureCause] = Field(default=None, alias="locFailureCause")
    loss_of_connect_reason: Optional[StrictInt] = Field(default=None, description="If 'monitoringType' is 'LOSS_OF_CONNECTIVITY', this parameter shall be included if available to identify the reason why.")
    unavail_per_dur: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Unsigned integer identifying a period of time in units of seconds.", alias="unavailPerDur")
    max_ue_availability_time: Optional[datetime] = Field(default=None, description="String with format 'date-time' as defined in OpenAPI.", alias="maxUEAvailabilityTime")
    msisdn: Optional[StrictStr] = Field(default=None, description="String formatted according to clause 3.3 of 3GPP TS 23.003 that describes an MSISDN.")
    monitoringType: MonitoringType
    ue_per_location_report: Optional[UePerLocationReport] = Field(default=None, alias="uePerLocationReport")
    plmn_id: Optional[PlmnId] = Field(default=None, alias="plmnId")
    reachability_type: Optional[ReachabilityType] = Field(default=None, alias="reachabilityType")
    roaming_status: Optional[StrictBool] = Field(default=None, description="If 'monitoringType' is 'ROAMING_STATUS', this parameter shall be set to 'true' if the new serving PLMN is different from the HPLMN.")
    failure_cause: Optional[FailureCause] = Field(default=None, alias="failureCause")
    event_time: Optional[datetime] = Field(default=None, description="String with format 'date-time' as defined in OpenAPI.", alias="eventTime")
    pdn_conn_info_list: Optional[Annotated[List[PdnConnectionInformation], Field(min_length=1)]] = Field(default=None, alias="pdnConnInfoList")
    ddd_status: Optional[DlDataDeliveryStatus] = Field(default=None, alias="dddStatus")
    ddd_traf_descriptor: Optional[DddTrafficDescriptor] = Field(default=None, alias="dddTrafDescriptor")
    max_wait_time: Optional[datetime] = Field(default=None, description="String with format 'date-time' as defined in OpenAPI.", alias="maxWaitTime")
    api_caps: Optional[Annotated[List[ApiCapabilityInfo], Field(min_length=0)]] = Field(default=None, alias="apiCaps")
    n_s_status_info: Optional[SACEventStatus] = Field(default=None, alias="nSStatusInfo")
    af_service_id: Optional[StrictStr] = Field(default=None, alias="afServiceId")
    serv_level_dev_id: Optional[StrictStr] = Field(default=None, description="If 'monitoringType' is 'AREA_OF_INTEREST', this parameter may be included to identify the UAV.", alias="servLevelDevId")
    uav_pres_ind: Optional[StrictBool] = Field(default=None, description="If 'monitoringType' is 'AREA_OF_INTEREST', this parameter shall be set to true if the specified UAV is in the monitoring area.")
    group_memb_list_changes: Optional[GroupMembListChanges] = Field(default=None, alias="groupMembListChanges")
    __properties: ClassVar[List[str]] = [
        "imeiChange", "externalId", "appId", "pduSessInfo", "idleStatusInfo", "locationInfo", "locFailureCause",
        "lossOfConnectReason", "unavailPerDur", "maxUEAvailabilityTime", "msisdn", "monitoringType", "uePerLocationReport",
        "plmnId", "reachabilityType", "roamingStatus", "failureCause", "eventTime", "pdnConnInfoList", "dddStatus",
        "dddTrafDescriptor", "maxWaitTime", "apiCaps", "nSStatusInfo", "afServiceId", "servLevelDevId", "uavPresInd",
        "groupMembListChanges"
    ]

