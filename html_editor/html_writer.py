

if __name__ == '__main__':
    import html_const
    from html_const import NEW_LINE, HtmlTagName
    from html_editor import HtmlElement
else:
    import html_editor.html_const as html_const
    from html_editor.html_const import NEW_LINE, HtmlTagName
    from html_editor.html_editor import HtmlElement

import os

BODY_BEFORE_STR = '<body><!--main contents--></body>'
BODY_AFTER_LEFT_STR = '<body>\n<div class="main-contents">\n'
BODY_AFTER_RIGHT_STR = '\n</div>\n</body>'




class HtmlWriter():
    def __init__(self,html_path:str='') -> None:
        self.html_path = html_path
        self.body:HtmlElement = HtmlElement('',HtmlTagName.BODY,{},1)
        self.indent_space = 4
        self.css_path = ''
    
    def init_values(self,css_path:str=''):
        self.css_path = css_path
    
    def add_outline_body_with_div(self,html_basic_path:str=''):
        """
        bodyタグの前後を追記する
         メインコンテンツ部も追記している
          <body><div class="main-contents"></div></body> 
        """
        html_basic_path = self.get_default_basic_path(html_basic_path)
        with open(html_basic_path, 'r',encoding='utf-8')as f:
            html_buf = f.read()
        with open(self.html_path,'r',encoding='utf-8')as f:
            contents_buf = f.read()
        before_str = BODY_BEFORE_STR
        after_str = '{}{}{}'.format(
            BODY_AFTER_LEFT_STR, NEW_LINE+contents_buf , BODY_AFTER_RIGHT_STR)
        w_data = html_buf.replace(before_str,after_str)
        with open(self.html_path,'w',encoding='utf-8')as f:
            f.write(w_data)
    
    def remover_html_source_outer_main_contents(self):
        """
        bodyタグの前後があれば削除する
         メインコンテンツ部も追記している
          <body><div class="main-contents"></div></body> 
        """
        import os
        if not os.path.exists(self.html_path): return
        with open(self.html_path, 'r',)as f:
            buf = f.read()
        left_pos = buf.find(BODY_AFTER_LEFT_STR)
        if left_pos < 0: return
        right_pos = buf.find(BODY_AFTER_RIGHT_STR)
        if right_pos < 0: return
        w_buf = buf[left_pos + len(BODY_AFTER_LEFT_STR)+1 : right_pos]
        with open(self.html_path, 'w',encoding='utf-8')as f:
            f.write(w_buf)

    def add_outline_body(self,html_basic_path:str=''):
        """
        bodyタグの前後を追記する
        """
        html_basic_path = self.get_default_basic_path(html_basic_path)
        with open(html_basic_path, 'r',encoding='utf-8')as f:
            html_buf = f.read()
        with open(self.html_path,'r',encoding='utf-8')as f:
            contents_buf = f.read()
        w_data = html_buf.replace('<body>','<body>'+NEW_LINE+contents_buf)
        with open(self.html_path,'w',encoding='utf-8')as f:
            f.write(w_data)
    
    def add_css_file_path(self,css_path:str):
        """
        CSS パスはタグ内に記載されるもの（htmlルートからの相対パス）をセットする
         （cssが格納されているファイルパスではない）
        """
        if css_path=='':
            css_path = self.css_path
        path = self.html_path
        value = html_const.CSS_BEGIN_TAG + css_path + html_const.CSS_END_TAG
        if self._is_exists_str_in_file(path,html_const.CSS_BEGIN_TAG):
            self._replace_line_to_file(path,html_const.CSS_BEGIN_TAG,value)
            return
        if self._is_exists_str_in_file(path,html_const.CSS_MARKER):
            self._replace_str_to_file(path,html_const.CSS_MARKER,value)
            return

    def _is_exists_str_in_file(self,path:str,value:str):
        with open(path,'r',encoding='utf-8')as f:
            buf = f.read()
        if buf.find(value)>=0:
            return True
        return False

    def _replace_str_to_file(self,path:str,target_value:str,replace_value:str):
        with open(path,'r',encoding='utf-8')as f:
            buf = f.read()
        buf = buf.replace(target_value,replace_value)
        with open(path,'w',encoding='utf-8')as f:
            f.write(buf)
            
    def _replace_line_to_file(self,path:str,target_value:str,replace_line:str):
        """
        target_valueが含まれる行を、replace_lineに置き換える
        """
        with open(path,'r',encoding='utf-8')as f:
            lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i]
            if line.find(target_value)>=0:
                lines[i] = replace_line + NEW_LINE
        with open(path,'w',encoding='utf-8')as f:
            f.writelines(lines)

    def get_default_basic_path(self,basic_html_file_path:str=''):
        import pathlib
        if basic_html_file_path=='':
            basic_html_file_path = str(pathlib.Path(__file__).parent.joinpath(html_const.BASIC_FILE_NAME))
        return basic_html_file_path

    def create_html_content(self,html_path:str=''):
        """空のテキストファイルを作る"""
        if html_path=='': html_path = self.html_path
        else: self.html_path = html_path
        #mkdir
        dir_path = os.path.dirname(self.html_path)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        with open(html_path,'w',encoding='utf-8')as f:
            f.write('')

    def add_to_file(self,element:'HtmlElement'):
        """ html ファイルに追記する"""
        buf = element.cnv_html_element_to_str()
        with open(self.html_path,'a',encoding='utf-8')as f:
            f.write(buf)
        self.__add_element(element)

    def add_to_file_by_text(self,text:str='',tag_name:str=HtmlTagName.DIV,attribute:dict={},is_begin_only:bool=False,indent:int=-1):
        element = HtmlElement(text,tag_name,attribute,1)
        self.add_to_file(element)
    
    def __add_element_by_text(self,text:str='',tag_name:str=HtmlTagName.DIV,attribute:dict={},is_begin_only:bool=False,indent:int=-1):
        self.body.add_element(HtmlElement(text,tag_name,attribute,1))

    def __add_element(self,element:HtmlElement):
        element.indent = self.body.indent + 1
        self.body.add_element(element)
        