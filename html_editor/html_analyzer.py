
if __name__ == '__main__':
    ##
    import pathlib
    import sys
    path = str(pathlib.Path(__file__).parent.parent)
    sys.path.append(path)
    ##
    import html_const
    from html_const import NEW_LINE, HtmlTagName, tag_is_closing_type
    from html_editor_main import HtmlElement
else:
    import html_editor.html_const as html_const
    from html_editor.html_const import NEW_LINE, HtmlTagName, tag_is_closing_type
    from html_editor.html_editor import HtmlElement

class HtmlAnalyzer():
    def __init__(self, html_path:str) -> None:
        self.html_path = html_path
        self.body:HtmlElement = HtmlElement('',HtmlTagName.BODY,{},1)
        self.indent_space = 4
        self.css_path = ''


from str_extruct import StrExtructor,cut_str2
from str_extruct import ListValueCounter
class HtmlTagCounter(ListValueCounter):
    class DiffList():
        def __init__(self) -> None:
            self.values=[]
        def append(self,tag:str):
            self.values.append(tag)
        def is_exists_diff(self):
            if len(self.values)>0:
                return True
            return False
    
    def __init__(self) -> None:
        super().__init__()
        self.diff_list = self.DiffList()

    def tag_count_is_match_closing_tag(self):
        tag_names = self.get_tag_name_list()
        for tag in tag_names:
            if '!--' in tag:
                continue
            if not tag_is_closing_type(tag):
                self._check(tag)
        if self.diff_list.is_exists_diff():
            return False
        return True
    
    def _check(self,tag:str):
        cnt = self.values[tag]
        cnt_close = self.values['/'+tag]
        if cnt != cnt_close:
            self.DiffList.append(tag)

    def get_tag_name_list(self):
        keys = self.get_keys_list()
        tag_name_list = []
        for k in keys:
            if k[0]!='/':
                tag_name_list.append(k)
        return tag_name_list

def test_main():
    import pathlib
    dir_path = str(pathlib.Path(__file__).parent.joinpath('html_test'))
    file_name='ダウンロード.htm'
    # file_name = 'test_writer.html'
    path = pathlib.Path(dir_path).joinpath(file_name)
    cl = StrExtructor(path)
    cl.method = cut_str2
    cl.set_value('<','>')
    cl.excute_all()
    ret_list = cl.get_results_as_list()
    counter = HtmlTagCounter()
    counter.count_list(ret_list)
    flag = counter.tag_count_is_match_closing_tag()
    print(flag)
    # ListValueCounter().print_count_list(ret_list)
    return

if __name__ == '__main__':
    test_main()
