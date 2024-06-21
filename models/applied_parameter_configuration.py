
from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class AppliedParameterConfiguration(BaseModel):
    
    external_ids: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Each element uniquely identifies a user.", alias="externalIds")
    msisdns: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Each element identifies the MS internal PSTN/ISDN number allocated for a UE.")
    maximum_latency: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Unsigned integer identifying a period of time in units of seconds.", alias="maximumLatency")
    maximum_response_time: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Unsigned integer identifying a period of time in units of seconds.", alias="maximumResponseTime")
    maximum_detection_time: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Unsigned integer identifying a period of time in units of seconds.", alias="maximumDetectionTime")
    __properties: ClassVar[List[str]] = ["externalIds", "msisdns", "maximumLatency", "maximumResponseTime", "maximumDetectionTime"]

  