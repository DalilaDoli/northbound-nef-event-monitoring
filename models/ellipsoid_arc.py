
from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

from models.gad_shape import GADShape
from models.geographical_coordinates import GeographicalCoordinates

class EllipsoidArc(GADShape):
  
    point: GeographicalCoordinates
    inner_radius: Annotated[int, Field(le=327675, strict=True, ge=0)] = Field(description="Indicates value of the inner radius.", alias="innerRadius")
    uncertainty_radius: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Indicates value of uncertainty.", alias="uncertaintyRadius")
    offset_angle: Annotated[int, Field(le=360, strict=True, ge=0)] = Field(description="Indicates value of angle.", alias="offsetAngle")
    included_angle: Annotated[int, Field(le=360, strict=True, ge=0)] = Field(description="Indicates value of angle.", alias="includedAngle")
    confidence: Annotated[int, Field(le=100, strict=True, ge=0)] = Field(description="Indicates value of confidence.")
    __properties: ClassVar[List[str]] = ["shape", "point", "innerRadius", "uncertaintyRadius", "offsetAngle", "includedAngle", "confidence"]
