

if __name__ == '__main__':
    import html_const
    from html_const import NEW_LINE, HtmlTagName
    from html_editor import HtmlElement
else:
    import html_editor.html_const as html_const
    from html_editor.html_const import NEW_LINE, HtmlTagName
    from html_editor.html_editor import HtmlElement

import os
import pathlib


BODY_BEFORE_STR = '<body><!--main contents--></body>'
BODY_AFTER_LEFT_STR = '<body>\n<div class="main-contents">\n'
BODY_AFTER_RIGHT_STR = '\n</div>\n</body>'


class CssTag():
    def __init__(self, path:str='', absolute_path:str='./') -> None:
        self.path = os.path.basename(path)
        self.absolute_path = absolute_path



class HtmlWriter():
    def __init__(self,html_path:str='') -> None:
        self.init_values_html_writer(html_path)
    
    def init_values_html_writer(self,html_path:str='', css_path:str=''):
        self.css_path = css_path
        self.html_path = html_path
        self.body:HtmlElement = HtmlElement('',HtmlTagName.BODY,{},1)
        self.indent_space = 4
        self.css_path = ''
        self.css_tags:'list[CssTag]' = []
    
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
    
    def add_css_file_path_list(self, css_path:str, absolute_path:str='./'):
        import shutil
        dir_path = os.path.dirname(self.html_path)
        if absolute_path.startswith('./'):
            buf = absolute_path[2:]
        dir_path = os.path.join(dir_path , buf)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        # print(os.path.dirname(css_path))
        if not _equals_path(dir_path, os.path.dirname(css_path)):
            _remove_if_exists(dir_path, css_path)
            shutil.copy(css_path, dir_path)
        self.css_tags.append(CssTag(css_path,absolute_path))

    
    def write_css_path(self):
        for css_tag in self.css_tags:
            self._create_css_tag(css_tag.path, css_tag.absolute_path)

    def _create_css_tag(self, css_file_path:str, absolute_path_from_root:str='./'):
        path = self._get_css_absolute_path(css_file_path, absolute_path_from_root)
        indent = self._get_indent(self.indent_space)
        tag = indent + html_const.CSS_TAG_SAMPLE.replace(
            html_const.REPLACE_VALUE,path) + NEW_LINE
        self._insert_str_to_file(self.html_path, '</head>',tag)

    def _get_indent(self,num:int):
        ret = ''
        for _ in range(num): ret+=' '
        return ret

    def add_css_in_header(self,css_path:str):
        pass
        self._insert_str_to_file(
            self.html_path,
            '</head>'
        )


    def _get_css_path(self,css_file_path:str):
        """
        値が空ならselfを取得する
        """
        if isinstance(css_file_path,str):
            if css_file_path=='':
                css_path_list = self.css_path_list
                pass
            else:
                self.css_path_list.append(css_file_path)
                css_path_list = self.css_path_list
        elif isinstance(css_file_path,list):
            if len(css_file_path)<1:
                css_path_list = self.css_path_list
            else:
                self.css_path_list += css_file_path
                css_path_list = self.css_path_list
        else:
            css_path_list = css_file_path
        return css_path_list

    def _get_css_absolute_path(self, css_path:str, absolute_path_from_root:str='./'):
        file_name = os.path.basename(css_path)
        return absolute_path_from_root + file_name

    def _is_exists_css_path(self, css_file_name:str, absolute_path_from_root:str='./'):
        css_base_name = os.path.basename(css_file_name)
        dir = os.path.basename(self.html_path)
        if absolute_path_from_root.startswith('./'):
            abs = absolute_path_from_root[2:]
        path = os.path.join(dir, abs, css_base_name)
        if os.path.exists(path):
            return True
        return False

    def add_css_file_path_from_file(self,css_file_path:str,absolute_path_from_root:str='./'):
        """
        CSS パスはタグ内に記載されるもの（htmlルートからの相対パス）をセットする
         （cssが格納されているファイルパスではない）
        """
        css_path_list = self._get_css_path(css_file_path)
        for path in css_path_list:
            css_abs = self._get_css_absolute_path(path,absolute_path_from_root)
            self.add_css_file_path(css_abs)
        # path = self.html_path
        # value = html_const.CSS_BEGIN_TAG + css_path + html_const.CSS_END_TAG
        # if self._is_exists_str_in_file(path,html_const.CSS_BEGIN_TAG):
        #     self._replace_line_to_file(path,html_const.CSS_BEGIN_TAG,value)
        #     return
        # if self._is_exists_str_in_file(path,html_const.CSS_MARKER):
        #     self._replace_str_to_file(path,html_const.CSS_MARKER,value)
        #     return

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


    def _insert_str_to_file(self,path:str,target_value:str,insert_value:str, offset:int=0):
        with open(path,'r',encoding='utf-8')as f:
            buf = f.read()
        pos = buf.find(target_value)
        if pos<0: return
        pos += offset
        buf = buf[:offset] + insert_value + buf[offset:]
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

    def get_default_basic_path(self,
    basic_html_file_path:str=''):
        import pathlib
        if basic_html_file_path=='':
            basic_html_file_path = str(pathlib.Path(__file__).parent.joinpath(html_const.BASIC_FILE_NAME))
        return basic_html_file_path

        
    def get_default_basic_css_path(self,basic_css_file_path_list:'list[str]'=[]):
        import pathlib
        if basic_css_file_path_list==[]:
            basic_css_file_path_list = [
                str(pathlib.Path(__file__).parent.joinpath(html_const.BASIC_CSS_FILE_NAME))]
        return basic_css_file_path_list

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
        

def _remove_if_exists(dist_dir_path:str, src_path:str):
    base_name = os.path.basename(src_path)
    path = os.path.join(dist_dir_path, base_name)
    if os.path.exists(path):
        os.remove(path)

def _equals_path(path_a:str, path_b:str):
    pathp_a = pathlib.Path(path_a)
    pathp_b = pathlib.Path(path_b)
    if str(pathp_a) == str(pathp_b):
        return True
    return False