from typing import Annotated, ClassVar, List, Optional, Union
from pydantic import BaseModel, Field, StrictBool

from models.lcs_qos_class import LcsQosClass
from models.minor_location_qo_s import MinorLocationQoS
from models.response_time import ResponseTime


class LocationQoS(BaseModel):
   
    h_accuracy: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Indicates value of accuracy.", alias="hAccuracy")
    v_accuracy: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Indicates value of accuracy.", alias="vAccuracy")
    vertical_requested: Optional[StrictBool] = Field(default=None, alias="verticalRequested")
    response_time: Optional[ResponseTime] = Field(default=None, alias="responseTime")
    minor_loc_qoses: Optional[Annotated[List[MinorLocationQoS], Field(min_length=1, max_length=2)]] = Field(default=None, alias="minorLocQoses")
    lcs_qos_class: Optional[LcsQosClass] = Field(default=None, alias="lcsQosClass")
    __properties: ClassVar[List[str]] = ["hAccuracy", "vAccuracy", "verticalRequested", "responseTime", "minorLocQoses", "lcsQosClass"]