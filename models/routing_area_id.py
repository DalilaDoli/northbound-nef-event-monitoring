

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

from models.plmn_id1 import PlmnId1

class RoutingAreaId(BaseModel):
  
    plmn_id: PlmnId1 = Field(alias="plmnId")
    lac: Annotated[str, Field(strict=True)] = Field(description="Location Area Code")
    rac: Annotated[str, Field(strict=True)] = Field(description="Routing Area Code")
    __properties: ClassVar[List[str]] = ["plmnId", "lac", "rac"]
