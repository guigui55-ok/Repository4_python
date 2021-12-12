

if __name__ == '__main__':
    import pathlib,os,sys
    parent = str(pathlib.Path(__file__).parent.parent.parent)
    path = os.path.join(parent,'adb_test')
    sys.path.append(path)
    path = os.path.join(parent)
    sys.path.append(path)
    import android_home
else:
    import pathlib,os
    path = str(pathlib.Path(__file__).parent.parent)
    path = os.path.join(path,'adb_test')
    import android_wiko.android_home
from common_util.adb_util.android_common import AndroidCommon
from common_util.adb_util.android_const import Constants
logger = None

def set_logger(arg_logger):
    logger = arg_logger
    android_home.logger = logger

def is_screen_match(
    screen_name:str,now_screen_file_path:str
):
    try:
        pass
    except Exception as e:
        logger.exp.error(e)

def get_screen_now():
    pass


class Wiko(AndroidCommon):
    def __init__(self, logger, image_dir, mode=Constants.main.CONTROL_MODE_ADB) -> None:
        super().__init__(logger, image_dir, mode=mode)
    