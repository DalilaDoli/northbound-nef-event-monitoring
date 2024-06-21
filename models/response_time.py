from enum import Enum

class ResponseTime(str, Enum):
    LOW_DELAY = "LOW_DELAY"
    DELAY_TOLERANT = "DELAY_TOLERANT"
    NO_DELAY = "NO_DELAY"