# 
from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class RangeDirection(BaseModel):
    
    range: Optional[Union[StrictFloat, StrictInt]] = None
    azimuth_direction: Optional[Annotated[int, Field(le=360, strict=True, ge=0)]] = Field(default=None, description="Indicates value of angle.", alias="azimuthDirection")
    elevation_direction: Optional[Annotated[int, Field(le=360, strict=True, ge=0)]] = Field(default=None, description="Indicates value of angle.", alias="elevationDirection")
    __properties: ClassVar[List[str]] = ["range", "azimuthDirection", "elevationDirection"]
