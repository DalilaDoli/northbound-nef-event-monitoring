from typing import Annotated, ClassVar, List, Optional
from pydantic import BaseModel, Field

from models.civic_address import CivicAddress
from models.geographic_area import GeographicArea
from models.network_area_info import NetworkAreaInfo


class LocationArea5G(BaseModel):

    geographic_areas: Optional[Annotated[List[GeographicArea], Field(min_length=0)]] = Field(default=None, description="Identifies a list of geographic area of the user where the UE is located.", alias="geographicAreas")
    civic_addresses: Optional[Annotated[List[CivicAddress], Field(min_length=0)]] = Field(default=None, description="Identifies a list of civic addresses of the user where the UE is located.", alias="civicAddresses")
    nw_area_info: Optional[NetworkAreaInfo] = Field(default=None, alias="nwAreaInfo")
    __properties: ClassVar[List[str]] = ["geographicAreas", "civicAddresses", "nwAreaInfo"]
