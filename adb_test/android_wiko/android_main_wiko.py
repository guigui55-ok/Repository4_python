
import android_home
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