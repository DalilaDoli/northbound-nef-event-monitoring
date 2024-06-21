from typing import TYPE_CHECKING, Optional, Set, Union

from pydantic import BaseModel

from models.ellipsoid_arc import EllipsoidArc
from models.point import Point
from models.point_altitude import PointAltitude
from models.point_altitude_uncertainty import PointAltitudeUncertainty
from models.point_uncertainty_circle import PointUncertaintyCircle
from models.point_uncertainty_ellipse import PointUncertaintyEllipse
from models.polygon import Polygon
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict



GEOGRAPHICAREA_ANY_OF_SCHEMAS = ["EllipsoidArc", "Point", "PointAltitude", "PointAltitudeUncertainty", "PointUncertaintyCircle", "PointUncertaintyEllipse", "Polygon"]

class GeographicArea(BaseModel):
   

    # data type: Point
    anyof_schema_1_validator: Optional[Point] = None
    # data type: PointUncertaintyCircle
    anyof_schema_2_validator: Optional[PointUncertaintyCircle] = None
    # data type: PointUncertaintyEllipse
    anyof_schema_3_validator: Optional[PointUncertaintyEllipse] = None
    # data type: Polygon
    anyof_schema_4_validator: Optional[Polygon] = None
    # data type: PointAltitude
    anyof_schema_5_validator: Optional[PointAltitude] = None
    # data type: PointAltitudeUncertainty
    anyof_schema_6_validator: Optional[PointAltitudeUncertainty] = None
    # data type: EllipsoidArc
    anyof_schema_7_validator: Optional[EllipsoidArc] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[EllipsoidArc, Point, PointAltitude, PointAltitudeUncertainty, PointUncertaintyCircle, PointUncertaintyEllipse, Polygon]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "EllipsoidArc", "Point", "PointAltitude", "PointAltitudeUncertainty", "PointUncertaintyCircle", "PointUncertaintyEllipse", "Polygon" }
