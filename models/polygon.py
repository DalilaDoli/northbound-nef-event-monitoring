

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated

from typing import Optional, Set
from typing_extensions import Self

from models.gad_shape import GADShape
from models.geographical_coordinates import GeographicalCoordinates

class Polygon(GADShape):
  
    point_list: Annotated[List[GeographicalCoordinates], Field(min_length=3, max_length=15)] = Field(description="List of points.", alias="pointList")
    __properties: ClassVar[List[str]] = ["shape", "pointList"]

   