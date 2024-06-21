
from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class HorizontalVelocity(BaseModel):

    h_speed: Union[Annotated[float, Field(le=2047, strict=True, ge=0)], Annotated[int, Field(le=2047, strict=True, ge=0)]] = Field(description="Indicates value of horizontal speed.", alias="hSpeed")
    bearing: Annotated[int, Field(le=360, strict=True, ge=0)] = Field(description="Indicates value of angle.")
    __properties: ClassVar[List[str]] = ["hSpeed", "bearing"]
