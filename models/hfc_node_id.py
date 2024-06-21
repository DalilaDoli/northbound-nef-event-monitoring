
from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class HfcNodeId(BaseModel):
 
    hfc_nid: Annotated[str, Field(strict=True, max_length=6)] = Field(description="This IE represents the identifier of the HFC node Id as specified in CableLabs WR-TR-5WWC-ARCH. It is provisioned by the wireline operator as part of wireline operations and may contain up to six characters. ", alias="hfcNId")
    __properties: ClassVar[List[str]] = ["hfcNId"]
