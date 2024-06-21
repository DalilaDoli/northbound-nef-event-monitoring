from enum import Enum

class PdnConnectionStatus(str, Enum):
    CREATED = "CREATED"
    RELEASED = "RELEASED"