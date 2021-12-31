import os
logger = None

def rename_with_add_str(arg_path:str,add_str : str ='_') -> str:
    try:
        ret = os.path.dirname(arg_path)
        ret += '\\' + os.path.basename(arg_path)
        ret += add_str
        ext = os.path.splitext(arg_path)
        ret = ret + ext[1]
        logger.info('make path : '+ ret)
        return ret + ext[1]
    except Exception as e:
        logger.error(e)
        return arg_path