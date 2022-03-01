from enum import IntEnum
from enum import Enum

class ConstCv2Monochro(IntEnum):
    BLACK = 0
    WHITE = 255
    GRAY = 127

class ConstCv2Color(Enum):
    BLUE = [0,0,255]
    WHITE = [255,255,255]