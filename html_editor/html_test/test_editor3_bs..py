import sys,pathlib

path = str(pathlib.Path(__file__).parent.parent.parent) #python4
sys.path.append(path)

from html_editor.html_editor_bs.html_editor_bs import HtmlEditorBs, HtmlElement
from html_editor.html_writer import HtmlWriter
from html_editor.html_const import HtmlTagName

def editer_test_main():
    sample_path = r'C:\Users\OK\source\repos\test_media_files\beautigulsoup_test'
    dirname = 'log_test1'
    html_path = str(pathlib.Path(sample_path).joinpath(dirname,'test_writer.html'))
    css_path = str(pathlib.Path(sample_path).joinpath(dirname, 'test.css'))
    editor = HtmlEditorBs()

    editor.create_html(html_path)
    el = HtmlElement('test text',HtmlTagName.DIV)
    editor.add_element(el)
    editor.update_file()

import os
def write_test_main():
    sample_path = r'C:\Users\OK\source\repos\test_media_files\beautigulsoup_test'
    dirname = 'log_test1'
    html_path = str(pathlib.Path(sample_path).joinpath(dirname,'test_writer.html'))
    css_path = str(pathlib.Path(sample_path).joinpath(dirname, 'test.css'))
    css_path2 = str(pathlib.Path(sample_path).joinpath(dirname, 'test_2.css'))

    writer = HtmlEditorBs()

    dir_path = os.path.dirname(html_path)
    
    # writer.create_html_content(html_path)
    writer.create_html(html_path)
    writer.add_css_file_path_list(css_path2)
    #
    el = HtmlElement('test text',HtmlTagName.DIV)
    writer.add_to_file(el)
    #
    img_attr = {'src':'test.png','alt':'test_image','class':'image_class'}
    el = HtmlElement('',HtmlTagName.IMG, img_attr)
    writer.add_to_file(el)
    #
    attr = {'id':'id1', 'class':'classA'}
    el = HtmlElement('id1, classA',HtmlTagName.P,attr)
    writer.add_to_file(el)
    #
    attr = {'id':'id2', 'class':'classB'}
    el = HtmlElement('id1, classA',HtmlTagName.P,attr)
    writer.add_to_file(el)
    #
    attr = {'id':'id3', 'class':'classB'}
    el = HtmlElement('id1, classA',HtmlTagName.P,attr)
    writer.add_to_file(el)
    #####
    writer.add_css_file_path(css_path)
    writer.add_outline_body()
    print('html path=' + writer.html_path)


if __name__ == '__main__':
    # editer_test_main()

    write_test_main()