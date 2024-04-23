
import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent)
sys.path.append(path)

import import_init
import traceback
try:
    from html_logger import HtmlLogger
    from common_utility.log_util.logging_util import LoggerUtility
except Exception as e:
    traceback.print_exc()
    raise e



######################################################################
### _init_css_format_values BEGIN
def _init_css_format_values_custom(tag_dict:dict=None):
    """
    log.htmlで使用するcssスタイルを設定する custom
     loggerのものを書き換える用

    Args:
        {lof_format_name : HtmlElement}

    Memo:
        目的別のログ出力のメソッド（add_log_main_title, add_log_procedure など）
            のフォーマットを設定する。
            （log_format_name[dictのkey]は HtmlLogConst.LOG_FORMAT_~ で指定する）
        タグやCSS（クラス名やプロパティ）を変えたいときはこれを変更する。

    Related Methods:
        add_main_title
            add_section_title
        add_log
            add_log_image
        add_procedure
            add_confirmation
    """
    log_format_dict = {}
    from html_logger import HtmlLogger, HtmlLogConst, HtmlElement, HtmlTagName
    tag_text = ''
    name = 'add_main_title'
    key = HtmlLogConst.LOG_FORMAT_MAIN_TITLE
    value = 'main_title'
    # value = 'title_bar'
    el = HtmlElement(
        tag_text, HtmlTagName.P,
        {HtmlLogConst.ATTR_CLASS: value})
    log_format_dict.update({key:el})
    #/
    key = HtmlLogConst.LOG_FORMAT_SECTION_TITLE
    el = HtmlElement(
        tag_text, HtmlTagName.P,
        {HtmlLogConst.ATTR_CLASS: 'section_title'})
    log_format_dict.update({key:el})
    #/
    # add log normal
    key = HtmlLogConst.LOG_FORMAT_NORMAL
    el = HtmlElement(
        tag_text, HtmlTagName.P,
        {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_LOG})
    log_format_dict.update({key:el})
    #/
    key = HtmlLogConst.LOG_FORMAT_IMAGE_BOX
    box_el = HtmlElement(
        '',HtmlTagName.DIV,
        {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_LOG_IMAGE_BOX})
    log_format_dict.update({key:box_el})
    #/
    key = HtmlLogConst.LOG_FORMAT_IMAGE_DESC
    image_description:str='log-image'
    span_el = HtmlElement(
        image_description,HtmlTagName.SPAN,
        {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_LOG_IMAGE_DESC})
    log_format_dict.update({key:span_el})
    #/
    key = HtmlLogConst.LOG_FORMAT_PROCEDURE
    el = HtmlElement(
        tag_text, HtmlTagName.P,
        {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_PROCEDURE})
    log_format_dict.update({key:el})
    #/
    key = HtmlLogConst.LOG_FORMAT_CONFIRMATION
    el = HtmlElement(
        tag_text, HtmlTagName.P,
        {HtmlLogConst.ATTR_CLASS:HtmlLogConst.CLASS_NAME_CONFIRMATION})
    log_format_dict.update({key:el})
    return log_format_dict
### _init_css_format_values END
######################################################################


from pathlib import Path
import os
def html_log_test():
    """
    html_logger.HtmlLogger を使用して、htmlファイルを作成する。
     ログ出力には書式がセットされた、専用のメソッドを使用する

    Memo:
        240419 修正
         インポート文修正。ログのパスを修正（gitignoreとなるように）
    """
    import datetime
    date_str = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    log_dir = Path(__file__).parent.joinpath('__log' + date_str)
    log_dir.mkdir(exist_ok=True)
    css_path = os.path.join(log_dir, 'log.css')
    read_css_dir = Path(__file__).parent.joinpath('sample_files/log_sample1')
    src_css_path = read_css_dir.joinpath(Path(css_path).name)
    # import shutil
    # shutil.copy(src_path, css_path)
    #/
    # log_path = os.path.join(log_dir,'testlog.log')
    logger = HtmlLogger('test_html_logger',log_dir)
    # dist_css_path = Path(logger.logger_dir_path).joinpath(Path(css_path).name)
    # logger.set_css_path(dist_css_path)
    #/
    # import shutil
    # shutil.copy(src_css_path, dist_css_path)
    #/
    logger._init_css_format_values()
    log_format_dict_custom = _init_css_format_values_custom()
    logger.log_format_dict.update(log_format_dict_custom)
    #/
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
    logger.set_css_path(src_css_path)
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
