
from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

TRANSPORTPROTOCOL_ANY_OF_SCHEMAS = ["str"]

class TransportProtocol(BaseModel):
    """
    Possible values are: - UDP: User Datagram Protocol. - TCP: Transmission Control Protocol.  
    """

    # data type: str
    anyof_schema_1_validator: Optional[StrictStr] = None
    # data type: str
    anyof_schema_2_validator: Optional[StrictStr] = Field(default=None, description="This string provides forward-compatibility with future extensions to the enumeration but is not used to encode content defined in the present version of this API.  ")
    if TYPE_CHECKING:
        actual_instance: Optional[Union[str]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "str" }
