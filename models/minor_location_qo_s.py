from typing import Annotated, ClassVar, List, Optional, Union
from pydantic import BaseModel, Field


class MinorLocationQoS(BaseModel):
 
    h_accuracy: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Indicates value of accuracy.", alias="hAccuracy")
    v_accuracy: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Indicates value of accuracy.", alias="vAccuracy")
    __properties: ClassVar[List[str]] = ["hAccuracy", "vAccuracy"]