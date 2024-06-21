from datetime import datetime
from typing import Annotated, ClassVar, List, Optional, Union
from pydantic import BaseModel, Field


class IdleStatusInfo(BaseModel):
    
    active_time: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Unsigned integer identifying a period of time in units of seconds.", alias="activeTime")
    edrx_cycle_length: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, alias="edrxCycleLength")
    suggested_number_of_dl_packets: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Identifies the number of packets shall be buffered in the serving gateway. It shall be present if the idle status indication is requested by the SCS/AS with \"idleStatusIndication\" in the \"monitoringEventSubscription\" sets to \"true\". ", alias="suggestedNumberOfDlPackets")
    idle_status_timestamp: Optional[datetime] = Field(default=None, description="string with format \"date-time\" as defined in OpenAPI.", alias="idleStatusTimestamp")
    periodic_au_timer: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Unsigned integer identifying a period of time in units of seconds.", alias="periodicAUTimer")
    __properties: ClassVar[List[str]] = ["activeTime", "edrxCycleLength", "suggestedNumberOfDlPackets", "idleStatusTimestamp", "periodicAUTimer"]
