

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

from models.plmn_id_nid import PlmnIdNid

class NtnTaiInfo(BaseModel):
 
    plmn_id: PlmnIdNid = Field(alias="plmnId")
    tac_list: Annotated[List[Annotated[str, Field(strict=True)]], Field(min_length=1)] = Field(alias="tacList")
    derived_tac: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="2 or 3-octet string identifying a tracking area code as specified in clause 9.3.3.10  of 3GPP TS 38.413, in hexadecimal representation. Each character in the string shall  take a value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most significant character representing the 4 most significant bits of the TAC shall  appear first in the string, and the character representing the 4 least significant bit  of the TAC shall appear last in the string.  ", alias="derivedTac")
    __properties: ClassVar[List[str]] = ["plmnId", "tacList", "derivedTac"]
