
from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated

from typing import Optional, Set
from typing_extensions import Self

from models.cell_global_id import CellGlobalId
from models.location_area_id import LocationAreaId
from models.routing_area_id import RoutingAreaId
from models.service_area_id import ServiceAreaId

class GeraLocation(BaseModel):

    location_number: Optional[StrictStr] = Field(default=None, description="Location number within the PLMN. See 3GPP TS 23.003, clause 4.5.", alias="locationNumber")
    cgi: Optional[CellGlobalId] = None
    rai: Optional[RoutingAreaId] = None
    sai: Optional[ServiceAreaId] = None
    lai: Optional[LocationAreaId] = None
    vlr_number: Optional[StrictStr] = Field(default=None, description="VLR number. See 3GPP TS 23.003 clause 5.1.", alias="vlrNumber")
    msc_number: Optional[StrictStr] = Field(default=None, description="MSC number. See 3GPP TS 23.003 clause 5.1.", alias="mscNumber")
    age_of_location_information: Optional[Annotated[int, Field(le=32767, strict=True, ge=0)]] = Field(default=None, description="The value represents the elapsed time in minutes since the last network contact of the mobile station. Value \"0\" indicates that the location information was obtained after a successful paging procedure for  Active Location Retrieval when the UE is in idle mode or after a successful location reporting procedure the UE is in connected mode. Any other value than \"0\" indicates that the location information is the last known one. See 3GPP TS 29.002 clause 17.7.8. ", alias="ageOfLocationInformation")
    ue_location_timestamp: Optional[datetime] = Field(default=None, description="string with format 'date-time' as defined in OpenAPI.", alias="ueLocationTimestamp")
    geographical_information: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Refer to geographical Information.See 3GPP TS 23.032 clause 7.3.2. Only the description of an ellipsoid point with uncertainty circle is allowed to be used. ", alias="geographicalInformation")
    geodetic_information: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Refers to Calling Geodetic Location.See ITU-T Recommendation Q.763 (1999) clause 3.88.2.  Only the description of an ellipsoid point with uncertainty circle is allowed to be used. ", alias="geodeticInformation")
    __properties: ClassVar[List[str]] = []
