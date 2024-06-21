
from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional

from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

from models.horizontal_velocity import HorizontalVelocity
from models.horizontal_velocity_with_uncertainty import HorizontalVelocityWithUncertainty
from models.horizontal_with_vertical_velocity import HorizontalWithVerticalVelocity
from models.horizontal_with_vertical_velocity_and_uncertainty import HorizontalWithVerticalVelocityAndUncertainty

VELOCITYESTIMATE_ONE_OF_SCHEMAS = ["HorizontalVelocity", "HorizontalVelocityWithUncertainty", "HorizontalWithVerticalVelocity", "HorizontalWithVerticalVelocityAndUncertainty"]

class VelocityEstimate(BaseModel):
    """
    Velocity estimate.
    """
    # data type: HorizontalVelocity
    oneof_schema_1_validator: Optional[HorizontalVelocity] = None
    # data type: HorizontalWithVerticalVelocity
    oneof_schema_2_validator: Optional[HorizontalWithVerticalVelocity] = None
    # data type: HorizontalVelocityWithUncertainty
    oneof_schema_3_validator: Optional[HorizontalVelocityWithUncertainty] = None
    # data type: HorizontalWithVerticalVelocityAndUncertainty
    oneof_schema_4_validator: Optional[HorizontalWithVerticalVelocityAndUncertainty] = None
    actual_instance: Optional[Union[HorizontalVelocity, HorizontalVelocityWithUncertainty, HorizontalWithVerticalVelocity, HorizontalWithVerticalVelocityAndUncertainty]] = None
    one_of_schemas: Set[str] = { "HorizontalVelocity", "HorizontalVelocityWithUncertainty", "HorizontalWithVerticalVelocity", "HorizontalWithVerticalVelocityAndUncertainty" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = VelocityEstimate.model_construct()
        error_messages = []
        match = 0
        # validate data type: HorizontalVelocity
        if not isinstance(v, HorizontalVelocity):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HorizontalVelocity`")
        else:
            match += 1
        # validate data type: HorizontalWithVerticalVelocity
        if not isinstance(v, HorizontalWithVerticalVelocity):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HorizontalWithVerticalVelocity`")
        else:
            match += 1
        # validate data type: HorizontalVelocityWithUncertainty
        if not isinstance(v, HorizontalVelocityWithUncertainty):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HorizontalVelocityWithUncertainty`")
        else:
            match += 1
        # validate data type: HorizontalWithVerticalVelocityAndUncertainty
        if not isinstance(v, HorizontalWithVerticalVelocityAndUncertainty):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HorizontalWithVerticalVelocityAndUncertainty`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in VelocityEstimate with oneOf schemas: HorizontalVelocity, HorizontalVelocityWithUncertainty, HorizontalWithVerticalVelocity, HorizontalWithVerticalVelocityAndUncertainty. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in VelocityEstimate with oneOf schemas: HorizontalVelocity, HorizontalVelocityWithUncertainty, HorizontalWithVerticalVelocity, HorizontalWithVerticalVelocityAndUncertainty. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into HorizontalVelocity
        try:
            instance.actual_instance = HorizontalVelocity.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into HorizontalWithVerticalVelocity
        try:
            instance.actual_instance = HorizontalWithVerticalVelocity.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into HorizontalVelocityWithUncertainty
        try:
            instance.actual_instance = HorizontalVelocityWithUncertainty.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into HorizontalWithVerticalVelocityAndUncertainty
        try:
            instance.actual_instance = HorizontalWithVerticalVelocityAndUncertainty.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into VelocityEstimate with oneOf schemas: HorizontalVelocity, HorizontalVelocityWithUncertainty, HorizontalWithVerticalVelocity, HorizontalWithVerticalVelocityAndUncertainty. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into VelocityEstimate with oneOf schemas: HorizontalVelocity, HorizontalVelocityWithUncertainty, HorizontalWithVerticalVelocity, HorizontalWithVerticalVelocityAndUncertainty. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], HorizontalVelocity, HorizontalVelocityWithUncertainty, HorizontalWithVerticalVelocity, HorizontalWithVerticalVelocityAndUncertainty]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


