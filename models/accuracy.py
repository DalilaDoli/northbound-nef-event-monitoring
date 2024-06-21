from enum import Enum

class Accuracy(str, Enum):
    CGI_ECGI = "CGI_ECGI"
    ENODEB = "ENODEB"
    TA_RA = "TA_RA"
    PLMN = "PLMN"
    TWAN_ID = "TWAN_ID"
    GEO_AREA = "GEO_AREA"
    CIVIC_ADDR = "CIVIC_ADDR"

