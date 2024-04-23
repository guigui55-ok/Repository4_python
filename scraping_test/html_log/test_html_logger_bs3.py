
import pathlib
from pathlib import Path
import os
# import sys_args_test
import sys
path = str(pathlib.Path(__file__).parent) #240419 HtmlLoggerBs
sys.path.append(path)
path = str(pathlib.Path(__file__).parent.parent) # import init
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
    """
    html_logger.HtmlLogger を使用して、htmlファイルを作成する。
     ログ出力には書式がセットされた、専用のメソッドを使用する

    Memo:
        240419 修正
         インポート文修正。ログのパスを修正（gitignoreとなるように）
          （html_editor を Repository4_python に移動したため？）
    """
    
    import datetime
    date_str = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    log_dir = Path(__file__).parent.joinpath('__log_bs3_' + date_str)
    log_dir.mkdir(exist_ok=True)
    css_path = os.path.join(log_dir, 'log.css')
    read_css_dir = Path(__file__).parent.joinpath('sample_files/log_sample2')
    src_css_path = read_css_dir.joinpath(Path(css_path).name)

    log_dir = str(pathlib.Path(__file__).parent.joinpath('test_log_bs3'))
    # css_path = 'log.css'
    if not os.path.exists(log_dir): os.mkdir(log_dir)
    # log_path = os.path.join(log_dir,'testlog.log')
    # css_path = str(pathlib.Path(__file__).parent.joinpath('sample_files','log.css'))
    css_paths = []
    css_path = os.path.join(read_css_dir, 'log.css')
    css_paths.append(css_path)
    css_path = os.path.join(read_css_dir, 'accordion.css')
    css_paths.append(css_path)
    css_path = os.path.join(read_css_dir, 'index.css')
    css_paths.append(css_path)
    #/
    read_css_dir_b = Path(__file__).parent.joinpath('sample_files/log_sample1')
    css_path = os.path.join(read_css_dir_b, 'log_b.css')
    css_paths.append(css_path)


    logger = HtmlLogger('test_html_logger',log_dir)
    # basic_html_path = str(pathlib.Path(__file__).parent.joinpath('sample_files','basic_log.html'))
    # logger.html_writer.create_html(logger.html_writer.html_path, '')
    #/
    from test_html_logger2 import _init_css_format_values_custom
    logger._init_css_format_values()
    log_format_dict_custom = _init_css_format_values_custom()
    logger.log_format_dict.update(log_format_dict_custom)
    #/
    logger.reset_log_file()
    # logger.html_writer.remover_html_source_outer_main_contents
    logger.create_log()
    # logger.html_writer.add_outline_body_with_div(logger.html_writer.html_path)
    # logger.set_css_path
    logger.add_main_title('メインタイトル2')
    logger.add_section_title('セクションタイトル')
    logger.add_procedure('手順')
    logger.info('test info')
    logger.info('画像')
    logger.info('float:left')
    logger.info('テキストチェック')
    logger.info('テキストのみ')
    logger.add_section_title('セクションタイトル2')
    logger.info('内容2')
    logger.set_css_path(css_paths)
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

    
def html_log_test2():
    import pathlib,os
    log_dir = str(pathlib.Path(__file__).parent.joinpath('test_log_bs3'))
    if not os.path.exists(log_dir): os.mkdir(log_dir)
    log_path = os.path.join(log_dir,'testlog.log')
    read_dir_path = pathlib.Path(__file__)
    # css_path = str(pathlib.Path(__file__).parent.joinpath('sample_files','log.css'))
    css_paths = []
    css_path = os.path.join(log_dir, 'log.css')
    css_paths.append(css_path)
    css_path = os.path.join(log_dir, 'accordion.css')
    css_paths.append(css_path)
    css_path = os.path.join(log_dir, 'index.css')
    css_paths.append(css_path)

    logger = HtmlLogger('test_html_logger',log_dir)
    # # basic_html_path = str(pathlib.Path(__file__).parent.joinpath('sample_files','basic_log.html'))
    # # logger.html_writer.create_html(logger.html_writer.html_path, '')
    # logger.reset_log_file()
    # logger.add_main_title('メインタイトル2')
    # logger.add_section_title('セクションタイトル')
    # logger.add_procedure('手順')
    # logger.info('test info')
    # logger.info('画像')
    # logger.info('float:left')
    # logger.info('テキストチェック')
    # logger.info('テキストのみ')
    # logger.add_section_title('セクションタイトル2')
    # logger.info('内容2')
    # logger.set_css_path(css_path)
    # logger.finish_to_create_html()
    # # is check tag
    # #add tag
    # #add tag in tag
    #     # get tag (class tag id (selector))
    # #add log last tag
    # #analyze,not analyze
    # #add log last line

    # # image float left
    # # 展開、閉じる
    # # vue.js 
    print('path = {}'.format(log_dir))
    return

if __name__ == '__main__':
    html_log_test()
    # html_log_test2()
