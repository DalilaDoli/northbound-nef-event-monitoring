


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from importlib import import_module
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING

from models.supported_gad_shapes import SupportedGADShapes


class GADShape(BaseModel):
 
    shape: SupportedGADShapes
    __properties: ClassVar[List[str]] = ["shape"]

  