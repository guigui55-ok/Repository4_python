"""
外部pathからlogging_utilを使用する
"""
import sys,os
from pathlib import Path
import_path = str(Path('__file__').resolve().parent.parent)+'\\logger_util'
print('import_path:'+import_path)
import_path = os.path.join('..', 'logger_util')
print('import_path:'+import_path)
sys.path.append(import_path)
import logging_util

def initialize_logger() -> logging_util.logger_util:
    log_file_name = './app.log'
    config_file_path = ''
    basic_format = '%(asctime)s - %(message)s'
    exception_format = '%(asctime)s %(filename)s:%(lineno)d[%(process)d][%(thread)d][%(levelname)s] %(module)s.%(name)s : %(message)s'
    loggeru = logging_util.intialize_logger_util(
        log_file_name,
        config_file_path,
        basic_format,
        exception_format
    )
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