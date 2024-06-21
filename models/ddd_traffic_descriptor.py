from typing import Annotated, ClassVar, List, Optional
from pydantic import BaseModel, Field


class DddTrafficDescriptor(BaseModel):

    ipv4_addr: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="String identifying a IPv4 address formatted in the 'dotted decimal' notation as defined in RFC 1166. ", alias="ipv4Addr")
    ipv6_addr: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="ipv6Addr")
    port_number: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.", alias="portNumber")
    mac_addr: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042. ", alias="macAddr")
    __properties: ClassVar[List[str]] = ["ipv4Addr", "ipv6Addr", "portNumber", "macAddr"]
