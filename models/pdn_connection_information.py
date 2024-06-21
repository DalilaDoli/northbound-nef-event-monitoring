

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated

from typing import Optional, Set
from typing_extensions import Self

from models.interface_indication import InterfaceIndication
from models.pdn_connection_status import PdnConnectionStatus
from models.pdn_type import PdnType

class PdnConnectionInformation(BaseModel):
   
    status: PdnConnectionStatus
    apn: Optional[StrictStr] = Field(default=None, description="Identify the APN, it is depending on the SCEF local configuration whether or not this attribute is sent to the SCS/AS. ")
    pdn_type: PdnType = Field(alias="pdnType")
    interface_ind: Optional[InterfaceIndication] = Field(default=None, alias="interfaceInd")
    ipv4_addr: Optional[StrictStr] = Field(default=None, description="string identifying a Ipv4 address formatted in the \"dotted decimal\" notation as defined in IETF RFC 1166. ", alias="ipv4Addr")
    ipv6_addrs: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, alias="ipv6Addrs")
    mac_addrs: Optional[Annotated[List[Annotated[str, Field(strict=True)]], Field(min_length=1)]] = Field(default=None, alias="macAddrs")
    __properties: ClassVar[List[str]] = ["status", "apn", "pdnType", "interfaceInd", "ipv4Addr", "ipv6Addrs", "macAddrs"]
