
from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated

from typing import Optional, Set
from typing_extensions import Self

from models.accuracy_fulfilment_indicator import AccuracyFulfilmentIndicator
from models.civic_address import CivicAddress
from models.geographic_area import GeographicArea
from models.ldr_type import LdrType
from models.minor_location_qo_s import MinorLocationQoS
from models.positioning_method import PositioningMethod
from models.range_direction import RangeDirection
from models.threedrelative_location import ThreedrelativeLocation
from models.twodrelative_location import TwodrelativeLocation
from models.up_cum_evt_rep import UpCumEvtRep
from models.user_location import UserLocation
from models.velocity_estimate import VelocityEstimate

class LocationInfo(BaseModel):

    age_of_location_info: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Unsigned integer identifying a period of time in units of minutes.", alias="ageOfLocationInfo")
    cell_id: Optional[StrictStr] = Field(default=None, description="Indicates the Cell Global Identification of the user which identifies the cell the UE is registered. ", alias="cellId")
    enode_bid: Optional[StrictStr] = Field(default=None, description="Indicates the eNodeB in which the UE is currently located.", alias="enodeBId")
    routing_area_id: Optional[StrictStr] = Field(default=None, description="Identifies the Routing Area Identity of the user where the UE is located.", alias="routingAreaId")
    tracking_area_id: Optional[StrictStr] = Field(default=None, description="Identifies the Tracking Area Identity of the user where the UE is located.", alias="trackingAreaId")
    plmn_id: Optional[StrictStr] = Field(default=None, description="Identifies the PLMN Identity of the user where the UE is located.", alias="plmnId")
    twan_id: Optional[StrictStr] = Field(default=None, description="Identifies the TWAN Identity of the user where the UE is located.", alias="twanId")
    user_location: Optional[UserLocation] = Field(default=None, alias="userLocation")
    geographic_area: Optional[GeographicArea] = Field(default=None, alias="geographicArea")
    civic_address: Optional[CivicAddress] = Field(default=None, alias="civicAddress")
    position_method: Optional[PositioningMethod] = Field(default=None, alias="positionMethod")
    qos_fulfil_ind: Optional[AccuracyFulfilmentIndicator] = Field(default=None, alias="qosFulfilInd")
    ue_velocity: Optional[VelocityEstimate] = Field(default=None, alias="ueVelocity")
    ldr_type: Optional[LdrType] = Field(default=None, alias="ldrType")
    achieved_qos: Optional[MinorLocationQoS] = Field(default=None, alias="achievedQos")
    related_applicationlayer_id: Optional[StrictStr] = Field(default=None, alias="relatedApplicationlayerId")
    range_direction: Optional[RangeDirection] = Field(default=None, alias="rangeDirection")
    twodrelative_location: Optional[TwodrelativeLocation] = Field(default=None, alias="twodrelativeLocation")
    threedrelative_location: Optional[ThreedrelativeLocation] = Field(default=None, alias="threedrelativeLocation")
    relative_velocity: Optional[VelocityEstimate] = Field(default=None, alias="relativeVelocity")
    up_cum_evt_rep: Optional[UpCumEvtRep] = Field(default=None, alias="upCumEvtRep")
    __properties: ClassVar[List[str]] = ["ageOfLocationInfo", "cellId", "enodeBId", "routingAreaId", "trackingAreaId", "plmnId", "twanId", "userLocation", "geographicArea", "civicAddress", "positionMethod", "qosFulfilInd", "ueVelocity", "ldrType", "achievedQos", "relatedApplicationlayerId", "rangeDirection", "twodrelativeLocation", "threedrelativeLocation", "relativeVelocity", "upCumEvtRep"]
