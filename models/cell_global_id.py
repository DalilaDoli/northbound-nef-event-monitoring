

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

class CellGlobalId(BaseModel):
   
    plmn_id: PlmnId1 = Field(alias="plmnId")
    lac: Annotated[str, Field(strict=True)]
    cell_id: Annotated[str, Field(strict=True)] = Field(alias="cellId")
    __properties: ClassVar[List[str]] = ["plmnId", "lac", "cellId"]
