from typing import Annotated, ClassVar, List, Optional
from pydantic import BaseModel, Field, StrictStr

from models.ipv6_prefix import Ipv6Prefix
from models.snssai import Snssai


class PduSessionInformation(BaseModel):
  
    snssai: Snssai
    dnn: StrictStr = Field(description="String representing a Data Network as defined in clause 9A of 3GPP TS 23.003;  it shall contain either a DNN Network Identifier, or a full DNN with both the Network  Identifier and Operator Identifier, as specified in 3GPP TS 23.003 clause 9.1.1 and 9.1.2. It shall be coded as string in which the labels are separated by dots  (e.g. \"Label1.Label2.Label3\"). ")
    ue_ipv4: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="String identifying a IPv4 address formatted in the 'dotted decimal' notation as defined in RFC 1166. ", alias="ueIpv4")
    ue_ipv6: Optional[Ipv6Prefix] = Field(default=None, alias="ueIpv6")
    ip_domain: Optional[StrictStr] = Field(default=None, alias="ipDomain")
    ue_mac: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="String identifying a MAC address formatted in the hexadecimal notation according to clause 1.1 and clause 2.1 of RFC 7042. ", alias="ueMac")
    __properties: ClassVar[List[str]] = []
