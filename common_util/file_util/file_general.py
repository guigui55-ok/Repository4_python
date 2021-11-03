


def get_file_list(logger, dir_path:str,include_file_name:str = ''):
    ret_list = list(range(0))
    try:
        import os
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

