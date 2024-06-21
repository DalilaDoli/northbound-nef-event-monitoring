from enum import Enum

class PdnType(str, Enum):
    IPV4 = "IPV4"
    IPV6 = "IPV6"
    IPV4V6 = "IPV4V6"
    NON_IP = "NON_IP"
    ETHERNET = "ETHERNET"