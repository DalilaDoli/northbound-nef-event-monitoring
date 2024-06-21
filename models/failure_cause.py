
from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class FailureCause(BaseModel):
   
    bssgp_cause: Optional[StrictInt] = Field(default=None, description="Identifies a non-transparent copy of the BSSGP cause code. Refer to 3GPP TS 29.128. ", alias="bssgpCause")
    cause_type: Optional[StrictInt] = Field(default=None, description="Identify the type of the S1AP-Cause. Refer to 3GPP TS 29.128.", alias="causeType")
    gmm_cause: Optional[StrictInt] = Field(default=None, description="Identifies a non-transparent copy of the GMM cause code. Refer to 3GPP TS 29.128. ", alias="gmmCause")
    ranap_cause: Optional[StrictInt] = Field(default=None, description="Identifies a non-transparent copy of the RANAP cause code. Refer to 3GPP TS 29.128. ", alias="ranapCause")
    ran_nas_cause: Optional[StrictStr] = Field(default=None, description="Indicates RAN and/or NAS release cause code information, TWAN release cause code information or untrusted WLAN release cause code information. Refer to 3GPP TS 29.214. ", alias="ranNasCause")
    s1_ap_cause: Optional[StrictInt] = Field(default=None, description="Identifies a non-transparent copy of the S1AP cause code. Refer to 3GPP TS 29.128. ", alias="s1ApCause")
    sm_cause: Optional[StrictInt] = Field(default=None, description="Identifies a non-transparent copy of the SM cause code. Refer to 3GPP TS 29.128. ", alias="smCause")
    __properties: ClassVar[List[str]] = ["bssgpCause", "causeType", "gmmCause", "ranapCause", "ranNasCause", "s1ApCause", "smCause"]
