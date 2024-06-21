
from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated

from typing import Optional, Set
from typing_extensions import Self

from models.ecgi import Ecgi
from models.global_ran_node_id import GlobalRanNodeId
from models.tai import Tai

class EutraLocation(BaseModel):

    tai: Tai
    ignore_tai: Optional[StrictBool] = Field(default=False, alias="ignoreTai")
    ecgi: Ecgi
    ignore_ecgi: Optional[StrictBool] = Field(default=False, description="This flag when present shall indicate that the Ecgi shall be ignored When present, it shall be set as follows: - true: ecgi shall be ignored. - false (default): ecgi shall not be ignored. ", alias="ignoreEcgi")
    age_of_location_information: Optional[Annotated[int, Field(le=32767, strict=True, ge=0)]] = Field(default=None, description="The value represents the elapsed time in minutes since the last network contact of the mobile station.  Value \"0\" indicates that the location information was obtained after a successful paging procedure for Active Location Retrieval when the UE is in idle mode or after a successful NG-RAN location reporting procedure with the eNB when the UE is in connected mode.  Any other value than \"0\" indicates that the location information is the last known one.  See 3GPP TS 29.002 clause 17.7.8. ", alias="ageOfLocationInformation")
    ue_location_timestamp: Optional[datetime] = Field(default=None, description="string with format 'date-time' as defined in OpenAPI.", alias="ueLocationTimestamp")
    geographical_information: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Refer to geographical Information. See 3GPP TS 23.032 clause 7.3.2. Only the description of an ellipsoid point with uncertainty circle is allowed to be used. ", alias="geographicalInformation")
    geodetic_information: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Refers to Calling Geodetic Location. See ITU-T Recommendation Q.763 (1999) [24] clause 3.88.2. Only the description of an ellipsoid point with uncertainty circle is allowed to be used. ", alias="geodeticInformation")
    global_ngenb_id: Optional[GlobalRanNodeId] = Field(default=None, alias="globalNgenbId")
    global_enb_id: Optional[GlobalRanNodeId] = Field(default=None, alias="globalENbId")
    __properties: ClassVar[List[str]] = ["tai", "ignoreTai", "ecgi", "ignoreEcgi", "ageOfLocationInformation", "ueLocationTimestamp", "geographicalInformation", "geodeticInformation", "globalNgenbId", "globalENbId"]
