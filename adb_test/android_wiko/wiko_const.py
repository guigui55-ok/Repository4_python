from enum import Enum

image_root_dir = './screen_wiko'

class const:
    SCREEN_CAPTURE_FILE_NAME = 'screenshot.png'

class const_screen_image_file_names:
    POWER_OFF = 'power_off.png'
    LOCK = 'lock.png'

class ConstWikoMain(Enum):
    SCREEN_CAPTURE_FILE_NAME = 'screenshot.png'

class ConstantsWiko():
    main : ConstWikoMain
    image : const_screen_image_file_names

