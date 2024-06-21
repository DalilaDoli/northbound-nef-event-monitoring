from enum import Enum

class PatchOperation(str, Enum):
    ADD = "add"
    REPLACE = "replace"