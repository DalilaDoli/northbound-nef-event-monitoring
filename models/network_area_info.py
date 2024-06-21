from typing import Annotated, ClassVar, List, Optional
from pydantic import BaseModel, Field

from models.ecgi import Ecgi
from models.global_ran_node_id import GlobalRanNodeId
from models.ncgi import Ncgi
from models.tai import Tai


class NetworkAreaInfo(BaseModel):
 
    ecgis: Optional[Annotated[List[Ecgi], Field(min_length=1)]] = Field(default=None, description="Contains a list of E-UTRA cell identities.")
    ncgis: Optional[Annotated[List[Ncgi], Field(min_length=1)]] = Field(default=None, description="Contains a list of NR cell identities.")
    g_ran_node_ids: Optional[Annotated[List[Optional[GlobalRanNodeId]], Field(min_length=1)]] = Field(default=None, description="Contains a list of NG RAN nodes.", alias="gRanNodeIds")
    tais: Optional[Annotated[List[Tai], Field(min_length=1)]] = Field(default=None, description="Contains a list of tracking area identities.")
    __properties: ClassVar[List[str]] = ["ecgis", "ncgis", "gRanNodeIds", "tais"]
