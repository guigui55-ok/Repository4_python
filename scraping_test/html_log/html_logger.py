

if __name__ == '__main__':
    from common_utility.log_util.logging_util import LoggerUtility,LogLevel,BasicLogger
else:
    from common_utility.log_util.logging_util import LoggerUtility,LogLevel,BasicLogger

from html_editor.html_writer import HtmlWriter
from html_editor.html_editor_main import HtmlElement
from html_editor.html_const import HtmlTagName
import pathlib
from pathlib import Path
import os

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
    LOG_FORMAT_MAIN_TITLE = 'add_main_title'
    LOG_FORMAT_SECTION_TITLE = 'add_section_title'
    LOG_FORMAT_NORMAL = 'add_log'
    LOG_FORMAT_IMAGE_BOX = 'add_log_image_box'
    LOG_FORMAT_IMAGE_DESC = 'add_log_image_desc'
    LOG_FORMAT_PROCEDURE = 'add_procedure'
    LOG_FORMAT_CONFIRMATION = 'add_confirmation'

class HtmlLogger():
    """
    操作や処理のログなどファイルに保存する
     テキスト、HTMLファイルにそれぞれ保存する
    LogLevel初期設定は TRACE(107):Console,INFO(106):Text,REPORT(105):Htmlとしてある。
     ログ出力時のレベル設定によって consoleのみ、+Text、+Htmlとできるようにしてある。
    
    """
    def __init__(self,
        logger_name: str,
        log_dir_path: str = '',
        log_dir_name: str = 'log',
        log_txt_file_name: str = 'log.txt',
        log_html_file_name: str = 'log.html',
        log_html_css_path: str = 'log.css',
        log_image_dir_name: str = 'image',
        create_log:bool = False,
        log_level:int = LogLevel.REPORT.value
        ) -> None:
        import logging
        # log_format = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s', '%Y-%m-%d %H:%M:%S')
        log_format = logging.Formatter('%(asctime)s  %(message)s', '%Y-%m-%d %H:%M:%S')
        self.log_dir_name = log_dir_name
        self.log_image_dir_name = log_image_dir_name
        self.init_log_dir_path(log_dir_path)
        
        # HtmlWriter
        # self.log_html_file_name = log_html_file_name
        # log_html_path = os.path.join(self.logger_dir_path,log_html_file_name)
        # # self.html_writer:HtmlWriter = HtmlWriter(log_html_path)
        # self.html_writer = HtmlWriter(log_html_path)
        # self.html_writer.css_path = log_html_css_path
        # self.html_writer.init_values_html_writer(log_html_path,log_html_css_path)
        # if create_log:
        #     self.create_log()
        #     self.html_writer.add_css_file_path(log_html_css_path)
        self._init_html_writer(log_html_file_name, log_html_css_path, create_log)

        # TextLog
        self.log_txt_file_name = log_txt_file_name        
        log_text_path = os.path.join(self.logger_dir_path,log_txt_file_name)
        self.log_txt_path = BasicLogger.mkfile_if_not_exists(log_text_path)
        self.txt_logger:LoggerUtility = LoggerUtility(
            logger_name, 
            log_file_name=log_text_path,
             log_format=log_format)

        # self.add_log_image('')
        self.log_level = log_level
        self.log_level_console = LogLevel.TRACE.value
        self.log_level_txt = LogLevel.INFO.value
        # self.add_log_txt('create log')
        # 
        self.log_format_dict = {}
        self._init_css_format_values()
    
    ######################################################################
    ### _init_css_format_values BEGIN
    def _init_css_format_values(self, tag_dict:dict=None):
        """
        log.htmlで使用するcssスタイルを設定する

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
        tag_text = ''
        name = 'add_main_title'
        key = HtmlLogConst.LOG_FORMAT_MAIN_TITLE
        el = HtmlElement(
            tag_text, HtmlTagName.P,
            {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_MAIN_TITLE})
        self.log_format_dict.update({key:el})
        #/
        key = HtmlLogConst.LOG_FORMAT_SECTION_TITLE
        el = HtmlElement(
            tag_text, HtmlTagName.P,
            {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_SECTION_TITLE})
        self.log_format_dict.update({key:el})
        #/
        # add log normal
        key = HtmlLogConst.LOG_FORMAT_NORMAL
        el = HtmlElement(
            tag_text, HtmlTagName.P,
            {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_LOG})
        self.log_format_dict.update({key:el})
        #/
        key = HtmlLogConst.LOG_FORMAT_IMAGE_BOX
        box_el = HtmlElement(
            '',HtmlTagName.DIV,
            {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_LOG_IMAGE_BOX})
        self.log_format_dict.update({key:box_el})
        #/
        key = HtmlLogConst.LOG_FORMAT_IMAGE_DESC
        image_description:str='log-image'
        span_el = HtmlElement(
            image_description,HtmlTagName.SPAN,
            {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_LOG_IMAGE_DESC})
        self.log_format_dict.update({key:span_el})
        #/
        key = HtmlLogConst.LOG_FORMAT_PROCEDURE
        el = HtmlElement(
            tag_text, HtmlTagName.P,
            {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_PROCEDURE})
        self.log_format_dict.update({key:el})
        #/
        key = HtmlLogConst.LOG_FORMAT_CONFIRMATION
        el = HtmlElement(
            tag_text, HtmlTagName.P,
            {HtmlLogConst.ATTR_CLASS:HtmlLogConst.CLASS_NAME_CONFIRMATION})
        self.log_format_dict.update({key:el})
    ### _init_css_format_values END
    ######################################################################

    def _init_html_writer(self,log_html_file_name, log_html_css_path, create_log):
        # HtmlWriter
        self.log_html_file_name = log_html_file_name
        log_html_path = os.path.join(self.logger_dir_path,log_html_file_name)
        self.html_writer:HtmlWriter = HtmlWriter(log_html_path)
        self.html_writer.css_path = log_html_css_path
        self.html_writer.init_values_html_writer(log_html_path,log_html_css_path)
        if create_log:
            self.create_log()
            self.html_writer.add_css_file_path(log_html_css_path)
    # def __init__(self,
    #     logger_name: str,
    #     config_file_path: str = '', 
    #     log_file_path: str = ...,
    #     log_level: int = ..., 
    #     log_format: str = ...,
    #     handler_mode: int = ...) -> None:
    #     super().__init__(logger_name, config_file_path, log_file_path, log_level, log_format, handler_mode)
    # def __init__(self,dir_path) -> None:
    #     self.logger_dir_path = ''
    # label procedure section 
    # heading confirmation details
    # subtitle

    def init_log_dir_path(
        self,
        log_dir_path:str,
        with_reset_image_dir:bool=True,
        log_image_dir_name:str=''):
        log_dir_name = self.log_dir_name
        if log_dir_path=='':
            self.logger_dir_path= str(pathlib.Path(__file__).parent.parent.joinpath(log_dir_name))
        else:
            self.logger_dir_path= os.path.join(log_dir_path, log_dir_name)
        self.log_dir_name = log_dir_name
        self.logger_dir_path = BasicLogger.get_dir_path_from_path(self.logger_dir_path)
        self.logger_dir_path = BasicLogger.mkdir_if_not_exists(self.logger_dir_path)
        if with_reset_image_dir:
            if log_image_dir_name!='':
                self.log_image_dir_name = log_image_dir_name
            self.log_image_dir_path = os.path.join(
                self.logger_dir_path, self.log_image_dir_name)
        

    def create_log(self):
        self.html_writer.create_html_content()
        self.html_writer.add_css_file_path('')
        self.add_log_txt('create log')
        

    def remover_html_source_outer_main_contents(self):
        if not os.path.exists(self.html_writer.html_path):return
        
    ########## HTML
    def __add_log_txt_align_format(self,el:HtmlElement):
        """HtmlElementからテキストlogに追記する"""
        value = el.tag_text
        #通常ログならインデントする
        if el.get_attribute('class') == HtmlLogConst.CLASS_NAME_LOG:
            value = HtmlLogConst.INDENT + value
        self.add_log_txt(value)
    
    def add_log_txt_align_format(self,el:HtmlElement):
        """HtmlElementからテキストlogに追記する"""
        return self.__add_log_txt_align_format(el)
    
    def __add_log_txt(self,el:HtmlElement):
        """HtmlElement からテキストlog に追記する"""
        self.__add_log_txt_align_format(el)

    def __add_log_main(self,el:HtmlElement,log_level:int = LogLevel.INFO.value):
        """ログに追記する main"""
        self._add_log_html(el,log_level)
        self.__add_log_txt(el)
    def __add_log_html(self,el:HtmlElement,log_level:int = LogLevel.INFO.value):
        """HtmlElement から HTML log に追記する"""
        if self.log_level <= log_level:
            self.html_writer.add_to_file(el)

            
    def _add_log_html(self,el:HtmlElement,log_level:int = LogLevel.INFO.value):
        """HtmlElement から HTML log に追記する"""
        if self.log_level <= log_level:
            self.html_writer.add_to_file(el)
    ########## Text
    def add_log_txt(self,value:str,log_level:int = LogLevel.INFO.value):
        """テキストlogのみに追記する base"""
        if self.log_level_txt <= log_level:
            self.txt_logger.info(value)
    ########## Console
    def print_log(self,value,log_level:int=LogLevel.TRACE.value):
        """Logをコンソールに出力する"""
        if self.log_level_console <= log_level:
            print(value)
    
    def reset_log_file(self):
        self.html_writer.create_html_content()
        self.add_log_txt('reset html')

    ########
    # 目的別のログ出力メソッド
    ########
    def add_main_title(self, tag_text:str):
        """
        html のメインタイトルをログに出力する
         HtmlTagName.P,{'class':'main_title'})
        """
        # el = HtmlElement(
        #     value,HtmlTagName.P,
        #     {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_MAIN_TITLE})
        el:HtmlElement = self.log_format_dict[HtmlLogConst.LOG_FORMAT_MAIN_TITLE]
        el.tag_text = tag_text
        self._add_log_main(el)

    def add_section_title(self, tag_text:str):
        """
        section のタイトルをログに出力する
         HtmlTagName.P,{'class':'section-title'})
        """
        # el = HtmlElement(
        #     value,HtmlTagName.P,
        #     {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_SECTION_TITLE})
        el:HtmlElement = self.log_format_dict[HtmlLogConst.LOG_FORMAT_SECTION_TITLE]
        el.tag_text = tag_text
        self._add_log_main(el)

    def add_log(self, tag_text:str):
        """
        ログを出力する（標準）
         HtmlTagName.P,{'class':'log'}
        """
        # el = HtmlElement(
        #     value,HtmlTagName.P,
        #     {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_LOG})
        el:HtmlElement = self.log_format_dict[HtmlLogConst.LOG_FORMAT_NORMAL]
        el.tag_text = tag_text
        self._add_log_main(el)
        
    def add_log_image(
        self,
        image_path:str,
        image_description:str='log-image',
        css_add_class_name:str='',
        log_level:int=LogLevel.INFO.value):
        """
        ログを出力する（画像）
         HtmlTagName.IMG,{'class':'log-image'}
          画像はイメージボックスに入れておく（文字列はIMGタグの後にSPANで配置する）
         HtmlTagName.DIV,{'class':'log-image-box'}
        """
        if image_path == '':
            if not os.path.exists(self.log_image_dir_path):
                os.mkdir(self.log_image_dir_path)
            return
        # box_el = HtmlElement(
        #     '',HtmlTagName.DIV,
        #     {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_LOG_IMAGE_BOX})
        box_el:HtmlElement = self.log_format_dict[HtmlLogConst.LOG_FORMAT_IMAGE_BOX]
        box_el.add_class_name(css_add_class_name)
        
        img_el = HtmlElement.create_html_element_img(image_path, image_description)
        box_el.add_element(img_el)
        # span_el = HtmlElement(
        #     image_description,HtmlTagName.SPAN,
        #     {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_LOG_IMAGE_DESC})
        span_el:HtmlElement = self.log_format_dict[HtmlLogConst.LOG_FORMAT_IMAGE_DESC]
        box_el.add_element(span_el)
        #イメージの場合は DIVタグがからテキストで無駄なログが出力されてしまう
        # self._add_log_main(box_el)
        #htmlに要素を書き込み
        self._add_log_html(box_el,log_level)
        #txtログには説明とイメージパスを追記
        self.__add_log_txt(span_el)
        self.add_log_txt(image_path,self.log_level_txt)

    def add_log_element(self,element:HtmlElement):
        """
        ログにHTML要素を追記する
        """
        self.html_writer.add_to_file(element)
        self.txt_logger.info(element.tag_text)
        
    def info(self,value:str):
        """
        ログを出力する（標準）
         add_log と同じ
          HtmlTagName.P,{'class':'log'}
        """
        self.add_log(value)
    ##########

    def add_procedure(self, tag_text:str):
        """
        手順をログに出力する
         HtmlTagName.P,{'class':'procedure'})
        """
        # el = HtmlElement(
        #     value,HtmlTagName.P,
        #     {HtmlLogConst.ATTR_CLASS: HtmlLogConst.CLASS_NAME_PROCEDURE})
        el:HtmlElement = self.log_format_dict[HtmlLogConst.LOG_FORMAT_PROCEDURE]
        el.tag_text = tag_text
        self._add_log_main(el)

    def add_confirmation(self, tag_text:str):
        """
        確認内容をログに出力する
         HtmlTagName.P,{'class':'confirmation'})
        """
        # el = HtmlElement(
        #     value,HtmlTagName.P,
        #     {HtmlLogConst.ATTR_CLASS:HtmlLogConst.CLASS_NAME_CONFIRMATION})
        el:HtmlElement = self.log_format_dict[HtmlLogConst.LOG_FORMAT_CONFIRMATION]
        el.tag_text = tag_text
        self._add_log_main(el)
    ##########
    # def add_log_element(self,element:HtmlElement):
    #     """
    #     ログにHTML要素を追記する
    #     """
    #     self.html_writer.add_to_file(element=element)
    ##########

    def create_html_from_contents(self):
        """
        空のテキストファイルを作成する
        """
        self.html_writer.create_html_content()
    def finish_to_create_html(self):
        """
        htmlファイルとして完成させる
         ログ追記時、htmlファイルははbody内のデータのみとなっている
          本メソッド実行後にhtmlヘッダー部を書き込み、
          <body><div class="main-contents"></div></body>で囲み、ファイルを完成させる。
        """
        self.html_writer.add_outline_body_with_div()
        # self.html_writer.add_css_file_path(self.html_writer.css_path)
        self.html_writer.write_css_path()

    def set_css_path(self, css_path:str, absolute_path:str='./'):
        """
        cssファイルを設定する
         stylesheetタグに入力する、ルートからの相対パス
        """
        self.html_writer.add_css_file_path_list(css_path, absolute_path)
        # self.html_writer.css_path = css_path
        

    def _add_log_main(self,el:HtmlElement,log_level:int = LogLevel.INFO.value):
        """ログに追記する main"""
        self._add_log_html(el,log_level)
        self.__add_log_txt(el)


def _mkdir(dir_path:str):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        