

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ThreedrelativeLocation(BaseModel):
   
    semi_minor: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Indicates value of uncertainty.", alias="semiMinor")
    semi_major: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Indicates value of uncertainty.", alias="semiMajor")
    vertical_uncertainty: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Indicates value of uncertainty.", alias="verticalUncertainty")
    orientation_angle: Optional[Annotated[int, Field(le=360, strict=True, ge=0)]] = Field(default=None, description="Indicates value of angle.", alias="orientationAngle")
    __properties: ClassVar[List[str]] = ["semiMinor", "semiMajor", "verticalUncertainty", "orientationAngle"]
