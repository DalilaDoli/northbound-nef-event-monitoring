from typing import Annotated, ClassVar, List, Optional
from pydantic import BaseModel, Field, StrictStr

from models.civic_address import CivicAddress
from models.geographic_area import GeographicArea


class LocationArea(BaseModel):
   
    cell_ids: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Indicates a list of Cell Global Identities of the user which identifies the cell the UE is registered. ", alias="cellIds")
    enode_b_ids: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Indicates a list of eNodeB identities in which the UE is currently located.", alias="enodeBIds")
    routing_area_ids: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Identifies a list of Routing Area Identities of the user where the UE is located. ", alias="routingAreaIds")
    tracking_area_ids: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="Identifies a list of Tracking Area Identities of the user where the UE is located. ", alias="trackingAreaIds")
    geographic_areas: Optional[Annotated[List[GeographicArea], Field(min_length=1)]] = Field(default=None, description="Identifies a list of geographic area of the user where the UE is located.", alias="geographicAreas")
    civic_addresses: Optional[Annotated[List[CivicAddress], Field(min_length=1)]] = Field(default=None, description="Identifies a list of civic addresses of the user where the UE is located.", alias="civicAddresses")
    __properties: ClassVar[List[str]] = ["cellIds", "enodeBIds", "routingAreaIds", "trackingAreaIds", "geographicAreas", "civicAddresses"]
