print('logger_init.py')
"""
外部pathからlogging_utilを使用する
"""
import sys,os
from pathlib import Path
import_path = str(Path('__file__').resolve().parent.parent)
# import_path = os.path.join(import_path,'common_util')
print('import_path:'+ import_path)
# import_path = os.path.join('..', 'logger_util')
# print('import_path:'+import_path)
sys.path.append(import_path)
import common_util.log_util
import common_util.log_util as logging_util
from common_util.log_util.logging_util import logger_info
from common_util.log_util.logging_util import logger_util
from common_util.log_util.logging_util import intialize_logger_util
g_is_initialize_logger:bool = False
g_loggeru : logger_info = False

log_file_name = './app.log'
config_file_path = ''
basic_format = '%(asctime)s - %(message)s'
exception_format = '%(asctime)s %(filename)s:%(lineno)d[%(process)d][%(thread)d][%(levelname)s] %(module)s.%(name)s : %(message)s'


def initialize_logger_with_args(
    arg_log_file_name:str,
    arg_config_file_path:str,
    arg_basic_format:str,
    arg_exception_format:str
):
    log_file_name = arg_log_file_name
    config_file_path = arg_config_file_path
    basic_format = arg_basic_format
    exception_format = arg_exception_format
    initialize_logger()

def initialize_logger() -> logger_util:
    # print('initialize_logger')
    global g_is_initialize_logger
    global g_loggeru
    if g_is_initialize_logger:
        return g_loggeru

    # log_file_name = './app.log'
    # config_file_path = ''
    # basic_format = '%(asctime)s - %(message)s'
    # exception_format = '%(asctime)s %(filename)s:%(lineno)d[%(process)d][%(thread)d][%(levelname)s] %(module)s.%(name)s : %(message)s'
    loggeru : logger_util = intialize_logger_util(
        log_file_name,
        config_file_path,
        basic_format,
        exception_format
    )
    from logger_util.logging_util import const
    loggeru.initialize_logger_info_for_exception(
        __name__ + 'exp',
        log_file_name,
        const.LEVEL_ERROR,
        exception_format,
        const.FILE_HANDLER |
        const.STREAM_HANDLER
    )
    g_is_initialize_logger = True
    g_loggeru = loggeru
    return loggeru

# def main():
#     loggeru = initialize_logger()
#     loggeru.info('info main')
#     loggeru.debug('debug main')
#     loggeru.warning('warning main')
#     loggeru.error('error main')
#     loggeru.critical('critical main')

# if __name__ == '__main__':
#     main()