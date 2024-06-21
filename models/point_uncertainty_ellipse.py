

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
from models.uncertainty_ellipse import UncertaintyEllipse

class PointUncertaintyEllipse(GADShape):

    point: GeographicalCoordinates
    uncertainty_ellipse: UncertaintyEllipse = Field(alias="uncertaintyEllipse")
    confidence: Annotated[int, Field(le=100, strict=True, ge=0)] = Field(description="Indicates value of confidence.")
    __properties: ClassVar[List[str]] = ["shape", "point", "uncertaintyEllipse", "confidence"]
