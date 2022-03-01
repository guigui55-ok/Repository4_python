
"""logger_test_common.py - 
logging.Logger クラス を使用するサンプル
ログのレベルによって、ログ出力を重複せずに、出力する内容を変更する
"""
import logging_util

def logger_util_sample2():
    # ログのレベルによって、ログ出力を重複せずに、出力する内容を変更する
    # config.json を使用するパターン
    config_file_path = './log_config.json'
    import os,pathlib
    config_file_path = str(pathlib.Path(__file__).parent.joinpath('log_config.json'))
    if not os.path.exists(config_file_path):
        print('config_file_path is not exists. return. //path= '+config_file_path)
        return
    loggeru = logging_util.LoggerUtility(
        __name__,
        config_file_path,
    )
    
    log_file_name = './logger_util_log.log'
    format = '%(asctime)s - %(message)s'
    # config.json を使用しないパターン
    # loggeru = logging_util.logger_util(
    #     __name__,
    #     log_file_name,
    #     logging_util.const.LEVEL_NOTSET,
    #     format,
    #     logging_util.const.FILE_HANDLER |
    #     logging_util.const.STREAM_HANDLER
    # )
    
    # error,critical は別の書式を設定したいので別に logger を作成する
    format = '%(asctime)s %(filename)s:%(lineno)d[%(process)d][%(thread)d][%(levelname)s] %(module)s.%(name)s : %(message)s'
    loggeru.initialize_logger_info_for_exception(
        __name__ + 'exp',
        log_file_name,
        logging_util.LoggerConstInt.LEVEL_ERROR,
        format,
        logging_util.LoggerConstInt.FILE_HANDLER |
        logging_util.LoggerConstInt.STREAM_HANDLER
    )

    loggeru.info('info main')
    loggeru.debug('debug main')
    loggeru.warning('warning main')
    loggeru.error('error main')
    loggeru.critical('critical main')

logger_util_sample2()