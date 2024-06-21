


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class UncertaintyEllipse(BaseModel):
   
    semi_major: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Indicates value of uncertainty.", alias="semiMajor")
    semi_minor: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Indicates value of uncertainty.", alias="semiMinor")
    orientation_major: Annotated[int, Field(le=180, strict=True, ge=0)] = Field(description="Indicates value of orientation angle.", alias="orientationMajor")
    __properties: ClassVar[List[str]] = ["semiMajor", "semiMinor", "orientationMajor"]
