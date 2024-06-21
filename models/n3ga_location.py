
from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBytes, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated

from typing import Optional, Set
from typing_extensions import Self

from models.hfc_node_id import HfcNodeId
from models.line_type import LineType
from models.tai import Tai
from models.tnap_id import TnapId
from models.transport_protocol import TransportProtocol
from models.twap_id import TwapId

class N3gaLocation(BaseModel):

    n3gpp_tai: Optional[Tai] = Field(default=None, alias="n3gppTai")
    n3_iwf_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="This IE shall contain the N3IWF identifier received over NGAP and shall be encoded as a  string of hexadecimal characters. Each character in the string shall take a value of \"0\"  to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most significant  character representing the 4 most significant bits of the N3IWF ID shall appear first in  the string, and the character representing the 4 least significant bit of the N3IWF ID  shall appear last in the string.  ", alias="n3IwfId")
    ue_ipv4_addr: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="String identifying a IPv4 address formatted in the 'dotted decimal' notation as defined in RFC 1166. ", alias="ueIpv4Addr")
    ue_ipv6_addr: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="ueIpv6Addr")
    port_number: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.", alias="portNumber")
    protocol: Optional[TransportProtocol] = None
    tnap_id: Optional[TnapId] = Field(default=None, alias="tnapId")
    twap_id: Optional[TwapId] = Field(default=None, alias="twapId")
    hfc_node_id: Optional[HfcNodeId] = Field(default=None, alias="hfcNodeId")
    gli: Optional[Union[StrictBytes, StrictStr]] = Field(default=None, description="string with format 'bytes' as defined in OpenAPI")
    w5gban_line_type: Optional[LineType] = Field(default=None, alias="w5gbanLineType")
    gci: Optional[StrictStr] = Field(default=None, description="Global Cable Identifier uniquely identifying the connection between the 5G-CRG or FN-CRG to the 5GS. See clause 28.15.4 of 3GPP TS 23.003. This shall be encoded as a string per clause 28.15.4 of 3GPP TS 23.003, and compliant with the syntax specified  in clause 2.2  of IETF RFC 7542 for the username part of a NAI. The GCI value is specified in CableLabs WR-TR-5WWC-ARCH. ")
    __properties: ClassVar[List[str]] = ["n3gppTai", "n3IwfId", "ueIpv4Addr", "ueIpv6Addr", "portNumber", "protocol", "tnapId", "twapId", "hfcNodeId", "gli", "w5gbanLineType", "gci"]
