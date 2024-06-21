from typing import Annotated, ClassVar, List, Optional
from pydantic import BaseModel, Field


class UpLocRepAddrAfRm(BaseModel):
    """
    Represents the user plane addressing information.
    """ # noqa: E501
    ipv4_addrs: Optional[Annotated[List[Annotated[str, Field(strict=True)]], Field(min_length=1)]] = Field(default=None, alias="ipv4Addrs")
    ipv6_addrs: Optional[Annotated[List[Annotated[str, Field(strict=True)]], Field(min_length=1)]] = Field(default=None, alias="ipv6Addrs")
    fqdn: Optional[Annotated[str, Field(min_length=4, strict=True, max_length=253)]] = Field(default=None, description="Fully Qualified Domain Name")
    __properties: ClassVar[List[str]] = []