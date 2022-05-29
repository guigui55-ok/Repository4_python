"""
外部pathからlogging_utilを使用する
"""
import import_init
import common_utility.log_util.logger_init
from common_utility.log_util.logger_init import initialize_logger
from common_utility.log_util.logger_init import initialize_logger_with_args
from common_utility.log_util.logger_init import intialize_logger_util

def main():
    import pathlib,os
    dir = str(pathlib.Path(__file__).parent.joinpath('log'))
    if not os.path.exists(dir):
        os.mkdir(dir)
    elif not os.path.isdir(dir):
        os.remove(dir)
        os.mkdir(dir)
    log_path = str(pathlib.Path(__file__).parent.joinpath('log','app.log'))
    loggeru = initialize_logger(log_path)
    loggeru.info('info main')
    loggeru.debug('debug main')
    loggeru.warning('warning main')
    loggeru.error('error main')
    loggeru.critical('critical main')


if __name__ == '__main__':
    main()