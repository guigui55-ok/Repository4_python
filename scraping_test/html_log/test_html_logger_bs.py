
import pathlib,sys
path = str(pathlib.Path(__file__).parent.parent)
sys.path.append(path)
import import_init
import traceback
try:
    from html_logger_bs import HtmlLoggerBs as HtmlLogger
    from common_utility.log_util.logging_util import LoggerUtility
except Exception as e:
    traceback.print_exc()
    raise Exception(e)


def html_log_test():
    import pathlib,os
    log_dir = str(pathlib.Path(__file__).parent.joinpath('test_log_bs'))
    css_path = os.path.join(log_dir, 'log.css')
    # css_path = 'log.css'
    if not os.path.exists(log_dir): os.mkdir(log_dir)
    log_path = os.path.join(log_dir,'testlog.log')
    css_path = str(pathlib.Path(__file__).parent.joinpath('sample_files','log.css'))
    logger = HtmlLogger('test_html_logger',log_dir)
    # basic_html_path = str(pathlib.Path(__file__).parent.joinpath('sample_files','basic_log.html'))
    # logger.html_writer.create_html(logger.html_writer.html_path, '')
    logger.reset_log_file()
    logger.add_main_title('メインタイトル')
    logger.add_section_title('セクションタイトル')
    logger.add_procedure('手順')
    logger.info('test info')
    logger.info('画像')
    logger.info('float:left')
    logger.info('テキストチェック')
    logger.info('テキストのみ')
    logger.add_section_title('セクションタイトル2')
    logger.info('内容2')
    logger.set_css_path(css_path)
    logger.finish_to_create_html()
    # is check tag
    #add tag
    #add tag in tag
        # get tag (class tag id (selector))
    #add log last tag
    #analyze,not analyze
    #add log last line

    # image float left
    # 展開、閉じる
    # vue.js 
    print('path = {}'.format(log_dir))
    return

if __name__ == '__main__':
    html_log_test()
