
from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class VerticalDirection(str, Enum):
    """
    Indicates direction of vertical speed.
    """

    """
    allowed enum values
    """
    UPWARD = 'UPWARD'
    DOWNWARD = 'DOWNWARD'



