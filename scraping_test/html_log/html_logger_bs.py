

if __name__ == '__main__':
    from common_utility.log_util.logging_util import LoggerUtility,LogLevel,BasicLogger
else:
    from common_utility.log_util.logging_util import LoggerUtility,LogLevel,BasicLogger

# from html_editor.html_writer import HtmlWriter
# from html_editor.html_editor import HtmlElement
# from html_editor.html_const import HtmlTagName
# from html_editor.html_editor_bs.html_editor_bs import HtmlEditorBs as HtmlWriter
# from html_editor.html_editor_bs.html_editor_bs import HtmlEditorBs as HtmlElement
#/
# from html_editor.html_editor_bs.html_editor_bs import HtmlEditorBs
# from html_editor.html_editor_bs.html_editor_bs import HtmlElementBs
# from html_editor.html_editor import HtmlElement
# from html_editor.html_editor_bs.html_editor_bs import HtmlTagName as HtmlTagName
#/
# from html_log.html_logger_bs import HtmlEditorBs
# from html_log.html_logger_bs import HtmlElementBs
#/
from html_editor.html_editor_bs.html_editor_bs_main import HtmlEditorBs
from html_editor.html_editor_bs.html_editor_bs_main import HtmlElementBs

if __name__ == '__main__':
    from html_log.html_logger import HtmlElement
    from html_log.html_logger import HtmlTagName
    from html_log.html_logger import HtmlLogger
else:
    # from html_log.html_logger import HtmlTagName
    from html_editor.html_const import HtmlTagName
    from html_editor.html_editor_main import HtmlElement

import pathlib
import os
from pathlib import Path

from html_log.html_logger import HtmlLogger

class HtmlLogConst():
    ATTR_CLASS = 'class'
    CLASS_NAME_MAIN_TITLE = 'main-title'
    CLASS_NAME_SECTION_TITLE = 'section-title'
    CLASS_NAME_LOG = 'log'
    CLASS_NAME_LOG_IMAGE = 'log-image'
    CLASS_NAME_LOG_IMAGE_BOX = 'log-image-box'
    CLASS_NAME_LOG_IMAGE_DESC = 'log-image-description'
    CLASS_NAME_PROCEDURE = 'procedure' 
    CLASS_NAME_CONFIRMATION = 'confirmation' 
    INDENT = '    '
import os

class HtmlLoggerBs(HtmlLogger):
    def __init__(self, logger_name: str, log_dir_path: str = '', log_dir_name: str = 'log', log_txt_file_name: str = 'log.txt', log_html_file_name: str = 'log.html', log_html_css_path: str = 'log.css', log_image_dir_name: str = 'image', create_log: bool = False, log_level: int = LogLevel.REPORT.value) -> None:
        super().__init__(logger_name, log_dir_path, log_dir_name, log_txt_file_name, log_html_file_name, log_html_css_path, log_image_dir_name, create_log, log_level)
        # self.html_writer.__class__ = HtmlEditorBs
        # HtmlWriter
        self._init_html_writer(log_html_file_name, log_html_css_path, create_log)

    def _init_html_writer(self,log_html_file_name, log_html_css_path, create_log):
        # HtmlWriter
        # from html_log.html_logger_bs import HtmlEditorBs
        self.log_html_file_name = log_html_file_name
        log_html_path = os.path.join(self.logger_dir_path,log_html_file_name)
        self.html_writer:HtmlEditorBs = HtmlEditorBs(log_html_path)
        self.html_writer.css_path = log_html_css_path
        self.html_writer.init_values_html_writer(log_html_path,log_html_css_path)
        if create_log:
            self.create_log()
            self.html_writer.add_css_file_path(log_html_css_path)

    
    def _add_log_main(self, el:HtmlElement, log_level:int = LogLevel.INFO.value):
        """ ログに追記する main """
        self._add_log_html(el,log_level)
        self.__add_log_txt(el)
    # def __add_log_html(self, el: HtmlElementBs, log_level: int = LogLevel.INFO.value):
    #     # return super().__add_log_html(el, log_level)
    #     """HtmlElement から HTML log に追記する"""
    #     if isinstance(el,HtmlElement):
    #         el = HtmlElementBs.cnv_to_html_element_bs(el)
    #     if self.log_level <= log_level:
    #         self.html_writer.add_to_file(el)

    # def add_main_title(self,value:str):
    #     """
    #     html のメインタイトルをログに出力する
    #      HtmlTagName.P,{'class':'main_title'})
    #     """
    #     el = HtmlElementBs(
    #         value,HtmlTagName.P,
    #         {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_MAIN_TITLE})
    #     self.__add_log_main(el)
        
    # def add_section_title(self,value:str):
    #     """
    #     section のタイトルをログに出力する
    #      HtmlTagName.P,{'class':'section-title'})
    #     """
    #     el = HtmlElement(
    #         value,HtmlTagName.P,
    #         {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_SECTION_TITLE})
    #     self.__add_log_main(el)

    # def __add_log_main(self,el:HtmlElementBs,log_level:int = LogLevel.INFO.value):
    #     """ログに追記する main"""
    #     if isinstance(el, HtmlElement):
    #         el = HtmlElementBs.cnv_to_html_element_bs(el)
    #     self.__add_log_html(el,log_level)
    #     self.__add_log_txt(el)

        
    # def _add_log_main(self,el:HtmlElementBs,log_level:int = LogLevel.INFO.value):
    #     """ログに追記する main"""
    #     if isinstance(el, HtmlElement):
    #         el = HtmlElementBs.cnv_to_html_element_bs(el)
    #     self.__add_log_html(el,log_level)
    #     self.__add_log_txt(el)

    # def __add_log_txt(self,el:HtmlElementBs):
    #     """HtmlElement からテキストlog に追記する"""
    #     self.__add_log_txt_align_format(el)

    # def __add_log_txt_align_format(self,el:HtmlElementBs):
    #     """HtmlElementからテキストlogに追記する"""
    #     value = el.tag_text
    #     #通常ログならインデントする
    #     if el.get_attribute('class') == HtmlLogConst.CLASS_NAME_LOG:
    #         value = HtmlLogConst.INDENT + value
    #     self.add_log_txt(value)
        
    def _add_log_html(self,el:HtmlElementBs,log_level:int = LogLevel.INFO.value):
        """HtmlElement から HTML log に追記する"""
        if isinstance(el,HtmlElement):
            el = HtmlElementBs.cnv_to_html_element_bs(el)
        if self.log_level <= log_level:
            # self.html_writer.add_to_file(el)
            self.html_writer.add_to_file_main_contents(el)

    def finish_to_create_html(self):
        """
        htmlファイルとして完成させる
         ログ追記時、htmlファイルははbody内のデータのみとなっている
          本メソッド実行後にhtmlヘッダー部を書き込み、
          <body><div class="main-contents"></div></body>で囲み、ファイルを完成させる。
        """
        # self.html_writer.add_outline_body_with_div()
        # self.html_writer.add_css_file_path(self.html_writer.css_path)
        self.html_writer.write_css_path()
        self.html_writer.update_file()