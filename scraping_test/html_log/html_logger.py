


from common_utility.log_util.logging_util import MyLogger,LoggerUtility
from html_editor.html_writer import HtmlWriter
from html_editor.html_editor import HtmlElement
from html_editor.html_const import HtmlTagName
import pathlib,os

class HtmlLogger():
    def __init__(self,
        logger_name: str,
        log_dir_path: str = '',) -> None:
        if log_dir_path=='':
            self.logger_dir_path= str(pathlib.Path(__file__).parent.parent.joinpath('log'))
        else:
            self.logger_dir_path= log_dir_path

        log_text_path = os.path.join(self.logger_dir_path,'log.txt')
        self.txt_logger:LoggerUtility = LoggerUtility(logger_name,log_file_path=log_text_path)
        log_html_path = os.path.join(self.logger_dir_path,'log.html')
        self.html_logger:HtmlWriter = HtmlWriter(log_html_path)
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
    def reset_log_file(self):
        self.html_logger.create_html_content()
    def add_main_title(self,value:str):
        el = HtmlElement(value,HtmlTagName.P,{'class':'main_title'})
        self.html_logger.add_to_file(el)
    def add_section_title(self,value:str):
        el = HtmlElement(value,HtmlTagName.P,{'class':'section-title'})
        self.html_logger.add_to_file(el)
    def add_log(self,value:str):
        el = HtmlElement(value,HtmlTagName.P,{'class':'log'})
        self.html_logger.add_to_file(el)
    def info(self,value:str):
        self.add_log(value)
    ##########
    def add_procedure(self,value:str):
        el = HtmlElement(value,HtmlTagName.P,{'class':'procedure'})
        self.html_logger.add_to_file(el)
    def add_confirmation(self,value:str):
        el = HtmlElement(value,HtmlTagName.P,{'class':'confirmation'})
        self.html_logger.add_to_file(el)
    ##########
    def add_log_element(self,element:HtmlElement):
        self.html_logger.add_to_file(element=element)
    ##########
    def create_html_from_contents(self):
        self.html_logger.create_html_content()
    def finish_to_create_html(self):
        self.html_logger.add_outline_body()
        self.html_logger.add_css_file_path(self.html_logger.css_path)
    def set_css_path(self,css_path):
        self.html_logger.css_path = css_path