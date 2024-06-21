

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PlmnIdNid(BaseModel):

    mcc: Annotated[str, Field(strict=True)] = Field(description="Mobile Country Code part of the PLMN, comprising 3 digits, as defined in clause 9.3.3.5 of 3GPP TS 38.413.  ")
    mnc: Annotated[str, Field(strict=True)] = Field(description="Mobile Network Code part of the PLMN, comprising 2 or 3 digits, as defined in clause 9.3.3.5 of 3GPP TS 38.413.")
    nid: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="This represents the Network Identifier, which together with a PLMN ID is used to identify an SNPN (see 3GPP TS 23.003 and 3GPP TS 23.501 clause 5.30.2.1).  ")
    __properties: ClassVar[List[str]] = ["mcc", "mnc", "nid"]
