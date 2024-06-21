

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBytes, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class TwapId(BaseModel):

    ss_id: StrictStr = Field(description="This IE shall contain the SSID of the access point to which the UE is attached, that is received over NGAP, see IEEE Std 802.11-2012.  ", alias="ssId")
    bss_id: Optional[StrictStr] = Field(default=None, description="When present, it shall contain the BSSID of the access point to which the UE is attached, for trusted WLAN access, see IEEE Std 802.11-2012.  ", alias="bssId")
    civic_address: Optional[Union[StrictBytes, StrictStr]] = Field(default=None, description="string with format 'bytes' as defined in OpenAPI", alias="civicAddress")
    __properties: ClassVar[List[str]] = ["ssId", "bssId", "civicAddress"]

  