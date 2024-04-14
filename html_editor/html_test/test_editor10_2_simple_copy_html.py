"""
htmlを作成する。

"""


import sys
import pathlib
from pathlib import Path
import os

path = str(pathlib.Path(__file__).parent.parent.parent) #python4
sys.path.append(path)

from html_editor.html_editor_bs.html_editor_bs_main import HtmlEditorBs, HtmlElement
from html_editor.html_writer import HtmlWriter
from html_editor.html_const import HtmlTagName

def editer_test_main():
    print('*sample_pathフォルダの中のフォルダ「log_test1」に')
    print('test.htmlとtest.cssというファイル名のhtmlとcssを作成する')
    print('cssは作成されない？')
    sample_path = r'C:\Users\OK\source\repos\Repository4_python\html_editor\html_test\test_sample_new1'
    print('sample_path = {}'.format(sample_path))
    dirname = ''
    html_path = str(pathlib.Path(sample_path).joinpath(dirname,'test.html'))
    css_path = str(pathlib.Path(sample_path).joinpath(dirname, 'test.css'))
    editor = HtmlEditorBs()

    print('create_html')
    editor.create_html(html_path)
    el = HtmlElement('test text',HtmlTagName.DIV)
    editor.add_element(el)
    print('update_file')
    editor.update_file()
    print('file_path = {}'.format(editor.html_path))

# def write_test_main_a():
#     # ファイルを読み込み、一部の要素をコピーする

#     sample_path = r'C:\Users\OK\source\repos\test_media_files\beautigulsoup_test'
#     dirname = 'log_test1'
#     target_path = str(pathlib.Path(__file__).parent)
#     html_path = str(pathlib.Path(target_path).joinpath(dirname,'test_writer.html'))
#     css_path = str(pathlib.Path(sample_path).joinpath(dirname, 'test.css'))
#     css_path2 = str(pathlib.Path(sample_path).joinpath(dirname, 'test_2.css'))
#     sample_path2 = r'C:\Users\OK\source\repos\test_media_files\beautigulsoup_test\log_test3_mouse_wheel4'
#     js_path = str(pathlib.Path(sample_path2).joinpath('test.js'))
#     css_path3 = str(pathlib.Path(sample_path2).joinpath('wheel_test.css'))

#     writer = HtmlEditorBs()
#     # writer.get_default_basic_path

#     dir_path = os.path.dirname(html_path)
    
#     # writer.create_html_content(html_path)
#     writer.create_html(html_path)
#     writer.add_css_file_path_list(css_path2)
#     el = HtmlElement('',HtmlTagName.DIV,{'class':'main_contents'})
#     writer.add_tag_to(el, 'body')
#     #
#     el = HtmlElement('box1',HtmlTagName.DIV,{'class':'box1'})
#     writer.add_tag_to_last_div(el)
#     #
#     el = HtmlElement('box2',HtmlTagName.DIV,{'class':'box2'})
#     writer.add_tag_to_last_div(el)

#     el = HtmlElement('box3',HtmlTagName.DIV,{'class':'box3'})
#     writer.add_tag_to(el, 'body')

    
#     el_box = HtmlElement('',HtmlTagName.DIV,{'class':'main_title'})
#     el_p = HtmlElement('main_title',HtmlTagName.P,{'class':'main_title'})
#     el_box.add_element(el_p)
#     writer.add_tag_to(el_box, 'body')

#     el_box = HtmlElement('',HtmlTagName.DIV,{'class':'procedure'})
#     el_p = HtmlElement('procedure',HtmlTagName.P,{'class':'sub_title'})
#     el_box.add_element(el_p)
#     writer.add_tag_to(el_box, 'body')

#     img_src_path = str(pathlib.Path(sample_path).joinpath(dirname,'test.png'))
#     abs_path = os.path.basename(img_src_path)
#     writer.copy_to_html_dir(img_src_path)
#     box_attr = {'class':'log_image_box', 'width':'400', 'height':'300'}
#     el_box = HtmlElement('',HtmlTagName.DIV, box_attr)
#     # img_path = os.path.join(dir_path,'sample_image.png')
#     img_attr ={'src':abs_path, 'class':'log_image', 'width':'400', 'height':'200'}
#     el_img = HtmlElement('procedure',HtmlTagName.IMG, img_attr)
#     el_span = HtmlElement('procedure',HtmlTagName.SPAN,{'class':'log_image_desc'})
#     el_box.add_element(el_img)
#     el_box.add_element(el_span)
#     writer.add_tag_to(el_box, 'body')

    
#     el_sec_box = HtmlElement('',HtmlTagName.DIV,{'class':'section_box'})
#     writer.add_tag_to(el_sec_box, 'body')

    
#     el_box = HtmlElement('',HtmlTagName.DIV,{'class':'procedure'})
#     el_p = HtmlElement('procedure',HtmlTagName.P,{'class':'sub_title'})
#     el_box.add_element(el_p)
#     writer.add_tag_to_last_div(el_box)
    
#     ### image_box
#     box_attr = {'class':'log_image_box', 'width':'400', 'height':'300'}
#     el_img_box = HtmlElement('',HtmlTagName.DIV, box_attr)
#     # img
#     img_src_path = str(pathlib.Path(sample_path).joinpath(dirname,'test.png'))
#     abs_path = os.path.basename(img_src_path)
#     writer.copy_to_html_dir(img_src_path)
#     # img_path = os.path.join(dir_path,'sample_image.png')
#     img_attr ={'src':abs_path, 'class':'log_image', 'width':'400', 'height':'200'}
#     el_img = HtmlElement('procedure',HtmlTagName.IMG, img_attr)
#     #
#     el_img_span = HtmlElement('procedure',HtmlTagName.SPAN,{'class':'log_image_desc'})
#     el_img_box.add_element(el_img)
#     el_img_box.add_element(el_img_span)
#     writer.add_tag_to_last_div(el_img_box)
#     ###
#     box_attr = {'class':'wheel_test'}
#     el_wheel_box = HtmlElement('',HtmlTagName.DIV, box_attr)
#     el_p = HtmlElement('wheel_test_text',HtmlTagName.P)
#     el_over = HtmlElement('wheel child over size',HtmlTagName.P, {'class':'over'})
#     el_inner = HtmlElement('wheel test box',HtmlTagName.P, {'class':'innerLogBox'})
#     el_buttton = HtmlElement('wheel child over size',HtmlTagName.P, {'class':'over'})
#     el_wheel_box.add_element(el_p)
#     el_wheel_box.add_element(el_over)
#     el_wheel_box.add_element(el_inner)
#     writer.add_tag_to_body(el_wheel_box)
#     writer.add_tag_to_body(el_buttton)

#     #####
#     writer.add_js_file_path(js_path)
#     writer.add_css_file_path_from_file(css_path)
#     writer.add_css_file_path_from_file(css_path3)
#     # writer.add_css_file_path(css_path)
#     writer.add_outline_body()
#     print('html path=' + writer.html_path)


# def write_test_main_b():
#     # ファイルを読み込み、一部の要素をコピーする
    
#     read_dir_path = pathlib.Path(__file__).parent.joinpath('test_sample2')
#     html_path = read_dir_path.joinpath('index.html')

#     write_dirname = 'log_test3'
#     write_dir_path = pathlib.Path(__file__).parent
#     write_html_path = write_dir_path.joinpath(write_dirname,'test_writer.html')
    
#     css_path = write_dir_path.joinpath(write_dirname, 'test.css')
#     css_path2 = write_dir_path.joinpath(write_dirname, 'test_2.css')
#     sample_path2 = r'C:\Users\OK\source\repos\Repository4_python\html_editor\html_test\test_sample2\base'
#     js_path = str(pathlib.Path(sample_path2).joinpath('test.js'))
#     css_path3 = str(pathlib.Path(sample_path2).joinpath('wheel_test.css'))
#     sample_html_path = Path(sample_path2).joinpath('updated_sample_report.html')

#     writer = HtmlEditorBs()
#     # writer.get_default_basic_path

#     dir_path = os.path.dirname(html_path)
    
#     # writer.create_html_content(html_path)
#     writer.create_html(html_path, sample_html_path, encoding='utf-8')
#     writer.add_css_file_path_list(css_path2)
#     #####

#     ### tableに任意の番号があるか判定、
#     # https://beautiful-soup-4.readthedocs.io/en/latest/
#     # writer.clear_tag(HtmlTagName.TD, text='99')
    
#     tag = writer.soup.find(
#         HtmlTagName.TD ,attrs={}, recursive=True ,text='99')
#     if tag == None:
#         print('tag==None')
#     # for tag in tags:
#     #     print(tag)
    

#     ### tableタグに複数のtdを追加
#     tr = HtmlElement('',HtmlTagName.TR)
#     td_num = HtmlElement('99',HtmlTagName.TD)
#     td_text = HtmlElement('コメント',HtmlTagName.TD)
#     td_image = HtmlElement('',HtmlTagName.TD)
#     img_path = 'placeholder.jpg'
#     img_attr ={'src':img_path, 'alt':'スマホ画面B', 'width':'400', 'height':'200'}
#     img = HtmlElement('procedure',HtmlTagName.IMG, img_attr)
#     td_image.add_element(img)
#     # tags = soup.find(
#     #     tag_name,attrs,recursive,text=text,kwargs=kwargs)
#     tr.add_element(td_num)
#     tr.add_element(td_text)
#     tr.add_element(td_image)
#     writer.add_tag_to(tr,'table')

#     ### tableに任意の番号があるか判定、
#     ### tableタグの中の任意のタグを削除
#     # https://beautiful-soup-4.readthedocs.io/en/latest/
#     # writer.clear_tag(HtmlTagName.TD, text='99')
    
#     # tag = writer.soup.find(
#     #     HtmlTagName.TD ,attrs={}, recursive=True ,text='99')
#     # if tag == None:
#     #     print('tag==None')
#     # else:
#     #     print(tag.parent)
#     #     tag.parent.clear()
#     #     print('cleard tag')
        

#     """
#     https://ai-inter1.com/beautifulsoup_1/
# select: 子孫要素の取得
# soup.select("body a")
# select: 子要素の取得
# # body要素の子要素の内、class属性に"end"をもつp要素を取得する場合
# soup.select("body > p.end")
# select: 隣接する直後の兄弟要素の取得
# class属性に"title"をもつp要素の直後の兄弟要素
# soup.select("p.title + p")
# select: 後ろの全ての兄弟要素の取得
# class属性に"title"をもつp要素の後ろの兄弟要素を取得
# soup.select("p.title ~ p")
# リストのn番目の要素の取得
# soup.select("ul#book > li:nth-of-type(1)")
#     """

#     #####
#     writer.add_js_file_path(js_path)
#     writer.add_css_file_path_from_file(css_path)
#     # writer.add_css_file_path_from_file(css_path3)
#     # writer.add_css_file_path(css_path)
#     #####
#     writer.add_outline_body()
#     # writer.update_file() #img タグの"<"が文字化けする
#     print('html path=' + str(writer.html_path))

#     # ゼロからeditorでhtml作成
#     # 元ファイルをコピー、テンプレ用htmlから作成

if __name__ == '__main__':
    # editer_test_main()
    print()
    print('*****')
    # write_test_main_a()
    # write_test_main_b()
    editer_test_main()


    """
    ・PageTitle
    ・Subject
    ・SubTitle
    ・
    
    """