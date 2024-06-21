
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

class PointAltitude(GADShape):
   
    point: GeographicalCoordinates
    altitude: Union[Annotated[float, Field(le=32767, strict=True, ge=-32767)], Annotated[int, Field(le=32767, strict=True, ge=-32767)]] = Field(description="Indicates value of altitude.")
    __properties: ClassVar[List[str]] = ["shape", "point", "altitude"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

