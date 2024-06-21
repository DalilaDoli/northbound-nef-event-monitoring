
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
from models.uncertainty_ellipse import UncertaintyEllipse

class PointAltitudeUncertainty(GADShape):
 
    point: GeographicalCoordinates
    altitude: Union[Annotated[float, Field(le=32767, strict=True, ge=-32767)], Annotated[int, Field(le=32767, strict=True, ge=-32767)]] = Field(description="Indicates value of altitude.")
    uncertainty_ellipse: UncertaintyEllipse = Field(alias="uncertaintyEllipse")
    uncertainty_altitude: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Indicates value of uncertainty.", alias="uncertaintyAltitude")
    confidence: Annotated[int, Field(le=100, strict=True, ge=0)] = Field(description="Indicates value of confidence.")
    __properties: ClassVar[List[str]] = ["shape", "point", "altitude", "uncertaintyEllipse", "uncertaintyAltitude", "confidence"]
