try:
    # common_utilityをsys.pathに追加済み
    from common_utility.log_util.logging_util import LoggerUtility
except:
    import traceback
    traceback.print_exc()

logger:LoggerUtility = None

flag:bool = False

def set_logger_in_cv2_image(arg_logger:LoggerUtility):
    # globals['logger'] = arg_logger
    logger = arg_logger

def log_info(value:str):
    if logger != None:
        logger.info(value)
    else:
        print(value)
def log_error(e:Exception):
    if logger != None:
        log_error(e)
    else:
        print(str(e))
    import traceback
    traceback.print_exc()