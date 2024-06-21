
from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

from models.patch_operation import PatchOperation

class PatchItem(BaseModel):
    op: PatchOperation
    path: str = Field(..., description="contains a JSON pointer value (as defined in IETF RFC 6901) that references a location of a resource on which the patch operation shall be performed.")
    var_from: Optional[str] = Field(None, description="indicates the path of the source JSON element (according to JSON Pointer syntax) being moved or copied to the location indicated by the 'path' attribute.", alias="from")
    value: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["op", "path", "from", "value"]
    
  