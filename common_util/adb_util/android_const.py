
from enum import Enum
from enum import IntEnum

class const_int(Enum):
    OPERATION_CV2_IMAGE = 101
    OPERATION_APPIUM_ELEMENT = 102
    WAIT_AFTER_REBOOT = 120
    CONTROL_SWIPE = 201
    CONTROL_TAP = 202
    CONTROL_DRAG = 203
    CONTROL_DOUBLE_TAP = 204
    CONTROl_TRIPLE_TAP = 205
    CONTROl_RELEASE = 206
    RESULT_OK = 1
    RESULT_SUCCESS = 1
    RESULT_NG = 0
    RESULT_FAILED = 0
    RESULT_ERROR = -1
    RESULT_UNEXPECTED_ERROR = -2

class const(Enum):
    ANDROID_CONST = 'android_const'
    SCREEN_CAPTURE_FILE_NAME = 'screenshot.png'
    SCREEN_RECORD_FILE_NAME = 'screenrecord.mp4'
    SD_ROOT_DIR = '/sdcard/'
    SAVE_PATH_ROOT_DIR = './'
    DEFAULT_THRESHOLD = '0.8'
    NOT_IMPLEMENTED = 'Not Implemented'

class const_screen_image_file_names(Enum):
    POWER_OFF = 'power_off.png'
    LOCK = 'lock.png'
    LOCK_INCLUDED = 'lock_'
    HOME_MAIN = 'home_main.png'
    HOME_INCLUDED = 'home_'

class const_state(IntEnum):
    UNKNOWN = 101,
    OFF = 102,
    HOME = 103