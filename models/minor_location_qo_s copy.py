

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class MinorLocationQoS(BaseModel):
   
    h_accuracy: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Indicates value of accuracy.", alias="hAccuracy")
    v_accuracy: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Indicates value of accuracy.", alias="vAccuracy")
    __properties: ClassVar[List[str]] = ["hAccuracy", "vAccuracy"]
