
from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

from models.related_ue_type import RelatedUEType

class RelatedUE(BaseModel):
  
    applicationlayer_id: StrictStr = Field(description="String identifying an UE with application layer ID. The format of the application  layer ID parameter is same as the Application layer ID defined in clause 11.3.4 of  3GPP TS 24.554. ", alias="applicationlayerId")
    related_ue_type: RelatedUEType = Field(alias="relatedUEType")
    __properties: ClassVar[List[str]] = ["applicationlayerId", "relatedUEType"]
