

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import ConfigDict
from typing import Any, ClassVar, Dict, List

from typing import Optional, Set
from typing_extensions import Self

from models.gad_shape import GADShape
from models.geographical_coordinates import GeographicalCoordinates

class Point(GADShape):
  
    point: GeographicalCoordinates
    __properties: ClassVar[List[str]] = ["shape", "point"]

 