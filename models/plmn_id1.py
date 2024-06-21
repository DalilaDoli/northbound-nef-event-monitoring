from typing import Annotated, ClassVar, List
from pydantic import BaseModel, Field


class PlmnId1(BaseModel):

    mcc: Annotated[str, Field(strict=True)] = Field(description="Mobile Country Code part of the PLMN, comprising 3 digits, as defined in clause 9.3.3.5 of 3GPP TS 38.413.  ")
    mnc: Annotated[str, Field(strict=True)] = Field(description="Mobile Network Code part of the PLMN, comprising 2 or 3 digits, as defined in clause 9.3.3.5 of 3GPP TS 38.413.")
    __properties: ClassVar[List[str]] = ["mcc", "mnc"]
