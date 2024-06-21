

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class UePerLocationReport(BaseModel):
   
    ue_count: Annotated[int, Field(strict=True, ge=0)] = Field(description="Identifies the number of UEs.", alias="ueCount")
    external_ids: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Each element uniquely identifies a user.", alias="externalIds")
    msisdns: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Each element identifies the MS internal PSTN/ISDN number allocated for a UE.")
    serv_level_dev_ids: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Each element uniquely identifies a UAV.", alias="servLevelDevIds")
    __properties: ClassVar[List[str]] = ["ueCount", "externalIds", "msisdns", "servLevelDevIds"]
