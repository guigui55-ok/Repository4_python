import sys,pathlib

path = str(pathlib.Path(__file__).parent.parent.parent) #python4
sys.path.append(path)

from html_editor.html_editor_bs.html_editor_bs import HtmlEditorBs, HtmlElement
from html_editor.html_writer import HtmlWriter
from html_editor.html_const import HtmlTagName

def editer_test_main():
    sample_path = r'C:\Users\OK\source\repos\test_media_files\beautigulsoup_test'
    dirname = 'log_test1'
    html_path = str(pathlib.Path(sample_path).joinpath(dirname,'test.html'))
    css_path = str(pathlib.Path(sample_path).joinpath(dirname, 'test.css'))
    editor = HtmlEditorBs()

    editor.create_html(html_path)
    el = HtmlElement('test text',HtmlTagName.DIV)
    editor.add_element(el)
    editor.update_file()

import os
def write_test_main():
    # ファイルを読み込み、一部の要素をコピーする

    sample_path = r'C:\Users\OK\source\repos\test_media_files\beautigulsoup_test'
    dirname = 'log_test1'
    target_path = str(pathlib.Path(__file__).parent)
    html_path = str(pathlib.Path(target_path).joinpath(dirname,'test_writer.html'))
    css_path = str(pathlib.Path(sample_path).joinpath(dirname, 'test.css'))
    css_path2 = str(pathlib.Path(sample_path).joinpath(dirname, 'test_2.css'))
    sample_path2 = r'C:\Users\OK\source\repos\test_media_files\beautigulsoup_test\log_test3_mouse_wheel4'
    js_path = str(pathlib.Path(sample_path2).joinpath('test.js'))
    css_path3 = str(pathlib.Path(sample_path2).joinpath('wheel_test.css'))

    writer = HtmlEditorBs()
    # writer.get_default_basic_path

    dir_path = os.path.dirname(html_path)
    
    # writer.create_html_content(html_path)
    writer.create_html(html_path)
    writer.add_css_file_path_list(css_path2)
    el = HtmlElement('',HtmlTagName.DIV,{'class':'main_contents'})
    writer.add_tag_to(el, 'body')
    #
    el = HtmlElement('box1',HtmlTagName.DIV,{'class':'box1'})
    writer.add_tag_to_last_div(el)
    #
    el = HtmlElement('box2',HtmlTagName.DIV,{'class':'box2'})
    writer.add_tag_to_last_div(el)

    el = HtmlElement('box3',HtmlTagName.DIV,{'class':'box3'})
    writer.add_tag_to(el, 'body')

    
    el_box = HtmlElement('',HtmlTagName.DIV,{'class':'main_title'})
    el_p = HtmlElement('main_title',HtmlTagName.P,{'class':'main_title'})
    el_box.add_element(el_p)
    writer.add_tag_to(el_box, 'body')

    el_box = HtmlElement('',HtmlTagName.DIV,{'class':'procedure'})
    el_p = HtmlElement('procedure',HtmlTagName.P,{'class':'sub_title'})
    el_box.add_element(el_p)
    writer.add_tag_to(el_box, 'body')

    img_src_path = str(pathlib.Path(sample_path).joinpath(dirname,'test.png'))
    abs_path = os.path.basename(img_src_path)
    writer.copy_to_html_dir(img_src_path)
    box_attr = {'class':'log_image_box', 'width':'400', 'height':'300'}
    el_box = HtmlElement('',HtmlTagName.DIV, box_attr)
    # img_path = os.path.join(dir_path,'sample_image.png')
    img_attr ={'src':abs_path, 'class':'log_image', 'width':'400', 'height':'200'}
    el_img = HtmlElement('procedure',HtmlTagName.IMG, img_attr)
    el_span = HtmlElement('procedure',HtmlTagName.SPAN,{'class':'log_image_desc'})
    el_box.add_element(el_img)
    el_box.add_element(el_span)
    writer.add_tag_to(el_box, 'body')

    
    el_sec_box = HtmlElement('',HtmlTagName.DIV,{'class':'section_box'})
    writer.add_tag_to(el_sec_box, 'body')

    
    el_box = HtmlElement('',HtmlTagName.DIV,{'class':'procedure'})
    el_p = HtmlElement('procedure',HtmlTagName.P,{'class':'sub_title'})
    el_box.add_element(el_p)
    writer.add_tag_to_last_div(el_box)
    
    ### image_box
    box_attr = {'class':'log_image_box', 'width':'400', 'height':'300'}
    el_img_box = HtmlElement('',HtmlTagName.DIV, box_attr)
    # img
    img_src_path = str(pathlib.Path(sample_path).joinpath(dirname,'test.png'))
    abs_path = os.path.basename(img_src_path)
    writer.copy_to_html_dir(img_src_path)
    # img_path = os.path.join(dir_path,'sample_image.png')
    img_attr ={'src':abs_path, 'class':'log_image', 'width':'400', 'height':'200'}
    el_img = HtmlElement('procedure',HtmlTagName.IMG, img_attr)
    #
    el_img_span = HtmlElement('procedure',HtmlTagName.SPAN,{'class':'log_image_desc'})
    el_img_box.add_element(el_img)
    el_img_box.add_element(el_img_span)
    writer.add_tag_to_last_div(el_img_box)
    ###
    box_attr = {'class':'wheel_test'}
    el_wheel_box = HtmlElement('',HtmlTagName.DIV, box_attr)
    el_p = HtmlElement('wheel_test_text',HtmlTagName.P)
    el_over = HtmlElement('wheel child over size',HtmlTagName.P, {'class':'over'})
    el_inner = HtmlElement('wheel test box',HtmlTagName.P, {'class':'innerLogBox'})
    el_buttton = HtmlElement('wheel child over size',HtmlTagName.P, {'class':'over'})
    el_wheel_box.add_element(el_p)
    el_wheel_box.add_element(el_over)
    el_wheel_box.add_element(el_inner)
    writer.add_tag_to_body(el_wheel_box)
    writer.add_tag_to_body(el_buttton)

    #####
    writer.add_js_file_path(js_path)
    writer.add_css_file_path_from_file(css_path)
    writer.add_css_file_path_from_file(css_path3)
    # writer.add_css_file_path(css_path)
    writer.add_outline_body()
    print('html path=' + writer.html_path)


import pathlib
def write_test_main():
    # ファイルを読み込み、一部の要素をコピーする
    
    read_dir_path = pathlib.Path(__file__).joinpath('test_sample1')

    write_dirname = 'log_test3'
    write_dir_path = pathlib.Path(__file__).parent
    write_html_path = write_dir_path.joinpath(write_dirname,'test_writer.html')
    
    css_path = write_dir_path.joinpath(write_dirname, 'test.css')
    css_path2 = write_dir_path.joinpath(write_dirname, 'test_2.css')
    sample_path2 = r'C:\Users\OK\source\repos\test_media_files\beautigulsoup_test\log_test3_mouse_wheel4'
    js_path = str(pathlib.Path(sample_path2).joinpath('test.js'))
    css_path3 = str(pathlib.Path(sample_path2).joinpath('wheel_test.css'))

    writer = HtmlEditorBs()
    # writer.get_default_basic_path

    dir_path = os.path.dirname(html_path)
    
    # writer.create_html_content(html_path)
    writer.create_html(html_path)
    writer.add_css_file_path_list(css_path2)

    #####
    writer.add_js_file_path(js_path)
    writer.add_css_file_path_from_file(css_path)
    writer.add_css_file_path_from_file(css_path3)
    # writer.add_css_file_path(css_path)
    writer.add_outline_body()
    print('html path=' + writer.html_path)

if __name__ == '__main__':
    # editer_test_main()

    write_test_main()