

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

from models.eutra_location import EutraLocation
from models.gera_location import GeraLocation
from models.n3ga_location import N3gaLocation
from models.nr_location import NrLocation
from models.utra_location import UtraLocation

class UserLocation(BaseModel):
    """
    At least one of eutraLocation, nrLocation and n3gaLocation shall be present. Several of them may be present. 
    """ # noqa: E501
    eutra_location: Optional[EutraLocation] = Field(default=None, alias="eutraLocation")
    nr_location: Optional[NrLocation] = Field(default=None, alias="nrLocation")
    n3ga_location: Optional[N3gaLocation] = Field(default=None, alias="n3gaLocation")
    utra_location: Optional[UtraLocation] = Field(default=None, alias="utraLocation")
    gera_location: Optional[GeraLocation] = Field(default=None, alias="geraLocation")
    __properties: ClassVar[List[str]] = ["eutraLocation", "nrLocation", "n3gaLocation", "utraLocation", "geraLocation"]
