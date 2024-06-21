from typing import Annotated, ClassVar, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt


class SACInfo(BaseModel):

    numeric_val_num_ues: Optional[StrictInt] = Field(default=None, alias="numericValNumUes")
    numeric_val_num_pdu_sess: Optional[StrictInt] = Field(default=None, alias="numericValNumPduSess")
    perc_value_num_ues: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = Field(default=None, alias="percValueNumUes")
    perc_value_num_pdu_sess: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = Field(default=None, alias="percValueNumPduSess")
    ues_with_pdu_session_ind: Optional[StrictBool] = Field(default=False, alias="uesWithPduSessionInd")
    __properties: ClassVar[List[str]] = ["numericValNumUes", "numericValNumPduSess", "percValueNumUes", "percValueNumPduSess", "uesWithPduSessionInd"]
