
import os

def get_file_list(logger, dir_path:str,include_file_name:str = ''):
    ret_list = list(range(0))
    try:       
        if os.path.isdir(dir_path):
            condition = ''
            if include_file_name != '':
                condition = '\\*' + condition + '*'
            import glob
            files = glob.glob(dir_path + condition)
            for file in files:
                ret_list.append(file)
        else:
            logger.exp.error('path is not directory. path=' + dir_path)
        return ret_list
    except Exception as e:
        logger.exp.error(e)
        return ret_list

def create_dir_if_nothing(logger,dir : str)->str:
    try:
        if os.path.exists(dir) and os.path.isdir(dir):
            return dir
        else:
            os.mkdir(dir)
            logger.info('create_dir_if_nothing : mkdir , dir = ' + dir)
        return dir
    except Exception as e:
        logger.exp.error(e)
        return ''

def read_line_file(logger,file_path):
    try:
        lines = []
        with open(file_path) as f:
            lines = f.readlines()
        return lines
    except Exception as e:
        logger.exp.error(e)
        return []