from pydantic import BaseModel, Field, StrictStr, StrictBool, StrictInt
from typing import Optional, List, Dict, Union


class Snssai(BaseModel):
    sst: Optional[StrictStr]
    sd: Optional[StrictStr]


class PduSessInfo(BaseModel):
    snssai: Optional[Snssai]
    dnn: Optional[StrictStr]
    ueIpv4: Optional[StrictStr]
    ueIpv6: Optional[StrictStr]
    ipDomain: Optional[StrictStr]
    ueMac: Optional[List[Optional[StrictStr]]]


class IdleStatusInfo(BaseModel):
    activeTime: Optional[StrictInt]
    edrxCycleLength: Optional[float]
    suggestedNumberOfDlPackets: Optional[StrictInt]
    idleStatusTimestamp: Optional[StrictStr]
    periodicAUTimer: Optional[StrictInt]


class UserLocation(BaseModel):
    latitude: Optional[float]
    longitude: Optional[float]
    altitude: Optional[float]


class GeographicArea(BaseModel):
    latitude: Optional[float]
    longitude: Optional[float]
    radius: Optional[float]


class CivicAddress(BaseModel):
    country: Optional[StrictStr]
    state: Optional[StrictStr]
    city: Optional[StrictStr]
    street: Optional[StrictStr]
    houseNumber: Optional[StrictStr]
    postalCode: Optional[StrictStr]


class LocationInfo(BaseModel):
    ageOfLocationInfo: Optional[StrictInt]
    cellId: Optional[StrictStr]
    enodeBId: Optional[StrictStr]
    routingAreaId: Optional[StrictStr]
    trackingAreaId: Optional[StrictStr]
    plmnId: Optional[StrictStr]
    twanId: Optional[StrictStr]
    userLocation: Optional[UserLocation]
    geographicArea: Optional[GeographicArea]
    civicAddress: Optional[CivicAddress]
    positionMethod: Optional[StrictStr]
    qosFulfilInd: Optional[StrictStr]
    ueVelocity: Optional[Dict[str, Optional[float]]]
    ldrType: Optional[StrictStr]
    achievedQos: Optional[StrictStr]
    relAppLayerId: Optional[StrictStr]
    rangeDirection: Optional[StrictStr]
    twoDRelLoc: Optional[Dict[str, Optional[float]]]
    threeDRelLoc: Optional[Dict[str, Optional[float]]]
    relVelocity: Optional[Dict[str, Optional[float]]]
    upCumEvtRep: Optional[Dict[str, Optional[Union[StrictStr, StrictInt]]]]


class MonitoringEventReport(BaseModel):
    imeiChange: Optional[str] = None
    externalId: Optional[str] = None
    appId: Optional[str] = None
    pduSessInfo: Optional[Dict] = None
    idleStatusInfo: Optional[Dict] = None
    locationInfo: Optional[Dict] = None
    locFailureCause: Optional[str] = None
    lossOfConnectReason: Optional[Union[int, str]] = None
    unavailPerDur: Optional[int] = None
    maxUEAvailabilityTime: Optional[str] = None
    msisdn: Optional[str] = None
    monitoringType: Optional[str] = None
    uePerLocationReport: Optional[Dict] = None
    plmnId: Optional[str] = None
    reachabilityType: Optional[str] = None
    roamingStatus: Optional[bool] = None
    failureCause: Optional[Dict] = None
    eventTime: Optional[Union[str, int]] = None
    pdnConnInfoList: Optional[List[Dict]] = None
    dddStatus: Optional[str] = None
    dddTrafDescriptor: Optional[str] = None
    maxWaitTime: Optional[str] = None
    apiCaps: Optional[List[Dict]] = None
    nSStatusInfo: Optional[str] = None
    afServiceId: Optional[str] = None
    servLevelDevId: Optional[str] = None
    uavPresInd: Optional[bool] = None
    groupMembListChanges: Optional[Dict] = None
    ueIpAddr: Optional[str] = None
    ueMacAddr: Optional[str] = None
    revocationNotifUri: Optional[str] = None
    reqRangSlRes: Optional[List[Dict]] = None
    relatedUEs: Optional[Dict] = None

class MonitoringNotification(BaseModel):
    subscription: Optional[StrictStr] = Field(description="string formatted according to IETF RFC 3986 identifying a referenced resource.")
    configResults: Optional[List[Dict[str, Optional[List[Optional[StrictStr]]]]]] = Field(default=None, description="Each element identifies a notification of grouping configuration result.")
    monitoringEventReports: Optional[List[MonitoringEventReport]] = Field(default=None, description="Monitoring event reports.")
    addedExternalIds: Optional[List[StrictStr]] = Field(default=None, description="Identifies the added external Identifier(s) within the active group.")
    addedMsisdns: Optional[List[StrictStr]] = Field(default=None, description="Identifies the added MSISDN(s) within the active group.")
    cancelExternalIds: Optional[List[StrictStr]] = Field(default=None, description="Identifies the cancelled external Identifier(s) within the active group.")
    cancelMsisdns: Optional[List[StrictStr]] = Field(default=None, description="Identifies the cancelled MSISDN(s) within the active group.")
    cancelInd: Optional[StrictBool] = Field(default=None, description="Indicates whether to request to cancel the corresponding monitoring subscription. Set to false or omitted otherwise.")
    appliedParam: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None)

