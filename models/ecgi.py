from typing import Annotated, ClassVar, List, Optional
from pydantic import BaseModel, Field

from models.plmn_id1 import PlmnId1


class Ecgi(BaseModel):
  
    plmn_id: PlmnId1 = Field(alias="plmnId")
    eutra_cell_id: Annotated[str, Field(strict=True)] = Field(description="28-bit string identifying an E-UTRA Cell Id as specified in clause 9.3.1.9 of  3GPP TS 38.413, in hexadecimal representation. Each character in the string shall take a  value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent 4 bits. The most  significant character representing the 4 most significant bits of the Cell Id shall appear  first in the string, and the character representing the 4 least significant bit of the  Cell Id shall appear last in the string.  ", alias="eutraCellId")
    nid: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="This represents the Network Identifier, which together with a PLMN ID is used to identify an SNPN (see 3GPP TS 23.003 and 3GPP TS 23.501 clause 5.30.2.1).  ")
    __properties: ClassVar[List[str]] = ["plmnId", "eutraCellId", "nid"]
