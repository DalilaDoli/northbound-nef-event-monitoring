from enum import Enum

class LcsQosClass(str, Enum):
    BEST_EFFORT = "BEST_EFFORT"
    ASSURED = "ASSURED"
    MULTIPLE_QOS = "MULTIPLE_QOS"