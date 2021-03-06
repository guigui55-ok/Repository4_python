
from enum import Enum
from enum import IntEnum

if __name__ == '__main__' or __name__ == 'android_const':
    from adb_key_const import ConstKeycode
    from adb_key_const import ConstCommand
else:
    # 外部から参照時は、common_util を sys.path へ追加しておくこと
    from common_util.adb_util.adb_key_const import ConstKeycode
    from common_util.adb_util.adb_key_const import ConstCommand
class Const(Enum):
    ANDROID_CONST = 'android_const'
    SCREEN_CAPTURE_FILE_NAME = 'screenshot.png'
    SCREEN_RECORD_FILE_NAME = 'screenrecord.mp4'
    SD_ROOT_DIR = '/sdcard/'
    ANDOID_STORAGE_ROOT = '/storage/'
    SAVE_PATH_ROOT_DIR = './'
    DEFAULT_THRESHOLD = '0.8'
    NOT_IMPLEMENTED = 'Not Implemented'
    OPERATION_CV2_IMAGE = 101
    OPERATION_APPIUM_ELEMENT = 102
    LOCK_OFF_DEFAULT_SWIPE_UP_VALUE = [300,1000,300,200,200]
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
    CONTROL_MODE_DEFAULT = 301
    CONTROL_MODE_IMG_CV2 = 302
    CONTROL_MODE_MOV_CV2 = 303
    CONTROL_MODE_OCR = 304
    CONTROL_MODE_ADB = 305
    TYPE_STRING = 401
    TYPE_BOOL = 402
    SWIPE_UP_FAST_DURATION = 250
    SWIPE_FAST_DURATION = 250
    SWIPE_NORMAL_SPEED = 1000
    ORDER_ASCENDING = 0
    ORDER_DEASCENDING = 1

class ConstScreenImageFileNames(Enum):
    POWER_OFF = 'power_off.png'
    LOCK = 'lock.png'
    LOCK_INCLUDED = 'lock_'
    HOME_MAIN = 'home_main.png'
    HOME_INCLUDED = 'home_'

class ConstState(IntEnum):
    UNKNOWN = 101,
    OFF = 102,
    HOME = 103

class Constants():
    main:Const = Const
    image_file:ConstScreenImageFileNames = ConstScreenImageFileNames
    state:ConstState = ConstState
    key:ConstKeycode = ConstKeycode
    command:ConstCommand = ConstCommand
