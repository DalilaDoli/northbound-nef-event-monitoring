
from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class UpCumEvtRep(BaseModel):
   
    up_loc_rep_stat: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.", alias="upLocRepStat")
    __properties: ClassVar[List[str]] = ["upLocRepStat"]
