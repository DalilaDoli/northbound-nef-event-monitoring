

from datetime import datetime
from typing import ClassVar, List
from pydantic import BaseModel, Field


class TimeWindow(BaseModel):
  
    start_time: datetime = Field(description="string with format \"date-time\" as defined in OpenAPI.", alias="startTime")
    stop_time: datetime = Field(description="string with format \"date-time\" as defined in OpenAPI.", alias="stopTime")
    __properties: ClassVar[List[str]] = ["startTime", "stopTime"]
