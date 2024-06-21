from typing import ClassVar, List
from pydantic import BaseModel, Field, StrictBool


class UavPolicy(BaseModel):
   
    uav_move_ind: StrictBool = Field(alias="uavMoveInd")
    revoke_ind: StrictBool = Field(alias="revokeInd")
    __properties: ClassVar[List[str]] = ["uavMoveInd", "revokeInd"]