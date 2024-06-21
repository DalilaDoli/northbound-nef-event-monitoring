

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class PlmnId(BaseModel):
   
    mcc: StrictStr = Field(description="String encoding a Mobile Country Code part of the PLMN, comprising 3 digits, as defined in 3GPP TS 38.413. ")
    mnc: StrictStr = Field(description="String encoding a Mobile Network Code part of the PLMN, comprising 2 or 3 digits, as defined in 3GPP TS 38.413. ")
    __properties: ClassVar[List[str]] = ["mcc", "mnc"]
