from typing import ClassVar, List, Optional
from pydantic import BaseModel, Field, StrictStr


class CivicAddress(BaseModel):

    country: Optional[StrictStr] = None
    a1: Optional[StrictStr] = Field(default=None, alias="A1")
    a2: Optional[StrictStr] = Field(default=None, alias="A2")
    a3: Optional[StrictStr] = Field(default=None, alias="A3")
    a4: Optional[StrictStr] = Field(default=None, alias="A4")
    a5: Optional[StrictStr] = Field(default=None, alias="A5")
    a6: Optional[StrictStr] = Field(default=None, alias="A6")
    prd: Optional[StrictStr] = Field(default=None, alias="PRD")
    pod: Optional[StrictStr] = Field(default=None, alias="POD")
    sts: Optional[StrictStr] = Field(default=None, alias="STS")
    hno: Optional[StrictStr] = Field(default=None, alias="HNO")
    hns: Optional[StrictStr] = Field(default=None, alias="HNS")
    lmk: Optional[StrictStr] = Field(default=None, alias="LMK")
    loc: Optional[StrictStr] = Field(default=None, alias="LOC")
    nam: Optional[StrictStr] = Field(default=None, alias="NAM")
    pc: Optional[StrictStr] = Field(default=None, alias="PC")
    bld: Optional[StrictStr] = Field(default=None, alias="BLD")
    unit: Optional[StrictStr] = Field(default=None, alias="UNIT")
    flr: Optional[StrictStr] = Field(default=None, alias="FLR")
    room: Optional[StrictStr] = Field(default=None, alias="ROOM")
    plc: Optional[StrictStr] = Field(default=None, alias="PLC")
    pcn: Optional[StrictStr] = Field(default=None, alias="PCN")
    pobox: Optional[StrictStr] = Field(default=None, alias="POBOX")
    addcode: Optional[StrictStr] = Field(default=None, alias="ADDCODE")
    seat: Optional[StrictStr] = Field(default=None, alias="SEAT")
    rd: Optional[StrictStr] = Field(default=None, alias="RD")
    rdsec: Optional[StrictStr] = Field(default=None, alias="RDSEC")
    rdbr: Optional[StrictStr] = Field(default=None, alias="RDBR")
    rdsubbr: Optional[StrictStr] = Field(default=None, alias="RDSUBBR")
    prm: Optional[StrictStr] = Field(default=None, alias="PRM")
    pom: Optional[StrictStr] = Field(default=None, alias="POM")
    usage_rules: Optional[StrictStr] = Field(default=None, alias="usageRules")
    method: Optional[StrictStr] = None
    provided_by: Optional[StrictStr] = Field(default=None, alias="providedBy")
    __properties: ClassVar[List[str]] = ["country", "A1", "A2", "A3", "A4", "A5", "A6", "PRD", "POD", "STS", "HNO", "HNS", "LMK", "LOC", "NAM", "PC", "BLD", "UNIT", "FLR", "ROOM", "PLC", "PCN", "POBOX", "ADDCODE", "SEAT", "RD", "RDSEC", "RDBR", "RDSUBBR", "PRM", "POM", "usageRules", "method", "providedBy"]
