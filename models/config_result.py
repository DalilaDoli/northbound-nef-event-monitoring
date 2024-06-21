

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

from models.result_reason import ResultReason

class ConfigResult(BaseModel):
 
    external_ids: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Each element indicates an external identifier of the UE.", alias="externalIds")
    msisdns: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Each element identifies the MS internal PSTN/ISDN number allocated for the UE. ")
    result_reason: ResultReason = Field(alias="resultReason")
    __properties: ClassVar[List[str]] = []
