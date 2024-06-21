

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

from models.sac_info import SACInfo

class SACEventStatus(BaseModel):
   
    reached_num_ues: Optional[SACInfo] = Field(default=None, alias="reachedNumUes")
    reached_num_pdu_sess: Optional[SACInfo] = Field(default=None, alias="reachedNumPduSess")
    __properties: ClassVar[List[str]] = ["reachedNumUes", "reachedNumPduSess"]
