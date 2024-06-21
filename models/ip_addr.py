

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated

from typing import Optional, Set
from typing_extensions import Self

from models.ipv6_prefix import Ipv6Prefix

class IpAddr(BaseModel):
    """
    Contains an IP adresse.
    """ # noqa: E501
    ipv4_addr: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="String identifying a IPv4 address formatted in the 'dotted decimal' notation as defined in RFC 1166. ", alias="ipv4Addr")
    ipv6_addr: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="ipv6Addr")
    ipv6_prefix: Optional[Ipv6Prefix] = Field(default=None, alias="ipv6Prefix")
    __properties: ClassVar[List[str]] = []
