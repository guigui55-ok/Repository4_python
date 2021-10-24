
import logging_util

def logger_util_sample1():
    # ログのレベルによって、ログ出力を重複せずに、出力する内容を変更する
    log_file_name = './logger_util_log.log'
    config_file_path = ''
    format = '%(asctime)s - %(message)s'
    loggeru = logging_util.logger_util(
        __name__,
        config_file_path,
        log_file_name,        
        logging_util.const.LEVEL_NOTSET,
        format,
        logging_util.const.FILE_HANDLER |
        logging_util.const.STREAM_HANDLER
    )
    
    format = '%(asctime)s %(filename)s:%(lineno)d[%(process)d][%(thread)d][%(levelname)s] %(module)s.%(name)s : %(message)s'
    loggeru.initialize_logger_info_for_exception(
        __name__ + 'exp',
        log_file_name,
        logging_util.const.LEVEL_ERROR,
        format,
        logging_util.const.FILE_HANDLER |
        logging_util.const.STREAM_HANDLER
    )

    loggeru.info('info main')
    loggeru.debug('debug main')
    loggeru.warning('warning main')
    loggeru.error('error main')
    loggeru.critical('critical main')

logger_util_sample1()

# -----------------------------------------------------
import logging

def setup_logger(name:str,logfile:str='app.log') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even DEBUG messages
    fh = logging.FileHandler(logfile)
    fh.setLevel(logging.DEBUG)
    fh_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s')
    fh.setFormatter(fh_formatter)

    # create console handler with a INFO log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
    ch.setFormatter(ch_formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

