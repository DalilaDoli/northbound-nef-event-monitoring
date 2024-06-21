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

class PointUncertaintyCircle(GADShape):
 
    point: GeographicalCoordinates
    uncertainty: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Indicates value of uncertainty.")
    __properties: ClassVar[List[str]] = ["shape", "point", "uncertainty"]
