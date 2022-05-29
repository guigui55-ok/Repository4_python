print('### ' + str(__file__))
"""
外部pathからlogging_utilを使用する
"""
import sys,os,pathlib
import_path = str(pathlib.Path(__file__).resolve().parent.parent)
print('    import_path:'+ import_path)
sys.path.append(import_path)
import common_utility.log_util
import common_utility.log_util as logging_util
from common_utility.log_util.logging_util import MyLogger
from common_utility.log_util.logging_util import LoggerUtility
from common_utility.log_util.logging_util import intialize_logger_util
g_is_initialize_logger:bool = False
g_loggeru : MyLogger = False

# log_file_name = '.log/app.log'
log_file_name = './app.log'
config_file_path = ''
basic_format = '%(asctime)s - %(message)s'
exception_format = '%(asctime)s %(filename)s:%(lineno)d[%(process)d][%(thread)d][%(levelname)s] %(module)s.%(name)s : %(message)s'


def initialize_logger_with_args(
    log_file_path:str,
    arg_config_file_path:str,
    arg_basic_format:str,
    arg_exception_format:str
):
    log_file_path = log_file_path
    config_file_path = arg_config_file_path
    basic_format = arg_basic_format
    exception_format = arg_exception_format
    initialize_logger(log_file_path)

def initialize_logger(
    log_file_path = './app.log') -> LoggerUtility:
    # print('initialize_logger')
    global g_is_initialize_logger
    global g_loggeru
    if g_is_initialize_logger:
        return g_loggeru

    # log_file_name = './app.log'
    # config_file_path = ''
    # basic_format = '%(asctime)s - %(message)s'
    # exception_format = '%(asctime)s %(filename)s:%(lineno)d[%(process)d][%(thread)d][%(levelname)s] %(module)s.%(name)s : %(message)s'
    loggeru : LoggerUtility = intialize_logger_util(
        log_file_path,
        config_file_path,
        basic_format,
        exception_format
    )
    from common_utility.log_util.logging_util import LoggerConstInt
    loggeru.initialize_logger_info_for_exception(
        __name__ + 'exp',
        log_file_name,
        LoggerConstInt.LEVEL_ERROR,
        exception_format,
        LoggerConstInt.FILE_HANDLER |
        LoggerConstInt.STREAM_HANDLER
    )
    g_is_initialize_logger = True
    g_loggeru = loggeru
    return loggeru

def test_main():
    loggeru = initialize_logger()
    loggeru.info('info main')
    loggeru.debug('debug main')
    loggeru.warning('warning main')
    loggeru.error('error main')
    loggeru.critical('critical main')

if __name__ == '__main__':
    test_main()