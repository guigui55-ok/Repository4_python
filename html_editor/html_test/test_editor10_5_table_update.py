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

##########################################################################################
##########################################################################################

def write_test_main2():
    """
    html編集、テーブルその2
    既存のhtmlのテーブルに、1行追記する
     重複チェック無し
    """
    import datetime
    date_str = datetime.datetime.now().strftime('_%y%m%d_%H%M')
    
    #####
    print('*それぞれのファイルのパスを読み込みセットする')
    read_dir_path = pathlib.Path(__file__).parent.joinpath('test_sample_new4')
    print('  read_dir_path = {}'.format(read_dir_path))
    html_path = read_dir_path.joinpath('index.html')
    # write_dirname = 'log_test3' + date_str
    write_dirname = 'log_test3'
    write_dir_path = pathlib.Path(__file__).parent
    write_html_path = write_dir_path.joinpath(write_dirname,'test_writer.html')
    css_path = write_dir_path.joinpath(write_dirname, 'test.css')
    css_path2 = write_dir_path.joinpath(write_dirname, 'test_2.css')
    sample_path2 = r'C:\Users\OK\source\repos\Repository4_python\html_editor\html_test\test_sample_new4\base'
    print('  sample_path2 = {}'.format(sample_path2))
    js_path = str(pathlib.Path(sample_path2).joinpath('test.js'))
    css_path3 = str(pathlib.Path(sample_path2).joinpath('wheel_test.css'))
    sample_html_path = Path(sample_path2).joinpath('updated_sample_report.html')
    #####
    print('*オブジェクトを生成、htmlを作成する')
    writer = HtmlEditorBs()
    writer.create_html(html_path, sample_html_path, encoding='utf-8')
    writer.add_css_file_path_list(css_path2)
    #####

    print('*tableに任意の番号があるか判定する')
    # https://beautiful-soup-4.readthedocs.io/en/latest/
    # writer.clear_tag(HtmlTagName.TD, text='99')
    
    value = '99'
    is_exists_tag = False
    soup = writer.soup
    # 条件に一致するtr要素をすべて検索
    matching_rows = []
    for tr in soup.find_all('tr'):
        td = tr.find('td')  # 最初のtd要素を取得
        if td and value in td.text:  # td要素が存在し、そのテキストに'99'が含まれているか確認
            matching_rows.append(tr)

    # 一致した行の内容を表示（または他の処理を実行）
    for row in matching_rows:
        # ここでは、行内のすべてのtd要素のテキストを取得して表示します
        tds = row.find_all('td')  # 行内のすべてのtd要素を取得
        row_data = [td.text.strip() for td in tds]  # 各td要素のテキストを取得し、前後の空白を削除
        print(row_data)
        is_exists_tag = True

    if not is_exists_tag:
        print('*タグが存在しない場合、tableタグに複数のtdを追加')
        tr = HtmlElement('',HtmlTagName.TR)
        td_num = HtmlElement('99',HtmlTagName.TD)
        td_text = HtmlElement('コメント',HtmlTagName.TD)
        td_image = HtmlElement('',HtmlTagName.TD)
        img_path = 'placeholder.jpg'
        img_attr ={'src':img_path, 'alt':'スマホ画面B', 'width':'400', 'height':'200'}
        img = HtmlElement('procedure',HtmlTagName.IMG, img_attr)
        td_image.add_element(img)
        tr.add_element(td_num)
        tr.add_element(td_text)
        tr.add_element(td_image)
        writer.add_tag_to(tr,'table')
    else:
        print('*タグが既に存在している「{}」'.format(value))
        

    """
    Memo
https://ai-inter1.com/beautifulsoup_1/
select: 子孫要素の取得
soup.select("body a")
select: 子要素の取得
# body要素の子要素の内、class属性に"end"をもつp要素を取得する場合
soup.select("body > p.end")
select: 隣接する直後の兄弟要素の取得
class属性に"title"をもつp要素の直後の兄弟要素
soup.select("p.title + p")
select: 後ろの全ての兄弟要素の取得
class属性に"title"をもつp要素の後ろの兄弟要素を取得
soup.select("p.title ~ p")
リストのn番目の要素の取得
soup.select("ul#book > li:nth-of-type(1)")
    """

    #####
    print('*ファイルを更新書き込み')
    writer.add_js_file_path(js_path)
    writer.add_css_file_path_from_file(css_path)
    writer.add_outline_body()
    print('html path=' + str(writer.html_path))
    #####


def write_test3():
    pass
    # ゼロからeditorでhtml作成
    # 元ファイルをコピー、テンプレ用htmlから作成


if __name__ == '__main__':
    # editer_test_main()
    print()
    print('*****')
    write_test_main2()


    """
    ・PageTitle
    ・Subject
    ・SubTitle
    ・
    
    """