#https://codezine.jp/article/detail/12230


from bs4 import BeautifulSoup
import requests



def test_main():
    ###
    import pathlib
    dir_path = str(pathlib.Path(__file__).parent.parent.joinpath('html_test'))
    file_name='ダウンロード.htm'
    file_name = 'test_writer.html'
    path = str(pathlib.Path(dir_path).joinpath(file_name))
    ###
    load_url = "https://codezine.jp/article/detail/12230"
    html = requests.get(load_url)
    print(type(html)) #<class 'requests.models.Response'>
    soup = BeautifulSoup(html.content, "html.parser")
    # soup = BeautifulSoup(open(path), 'html.parser')
    # HTML全体を表示する
    # print(soup)
    print(soup.find('title'))
    print(soup.find('h2'))
    # print(soup.find('h1'))
    print(soup.find('h1').text)
    print('******')
    # print(soup.find_all('div'))
    print('******')
    el = soup.find(class_="c-stacknav_listitem")
    print(el)
    print('******')
    el = soup.find(id='password')
    print(el)
    return


def test_main2():
    ###
    import pathlib
    dir_path = str(pathlib.Path(__file__).parent.parent.joinpath('html_test'))
    file_name='ダウンロード.htm'
    file_name = 'test_writer.html'
    path = str(pathlib.Path(dir_path).joinpath(file_name))
    ###
    # load_url = "https://codezine.jp/article/detail/12230"
    # html = requests.get(load_url)
    # soup = BeautifulSoup(html.content, "html.parser")
    soup = BeautifulSoup(open(path), 'html.parser')
    # HTML全体を表示する
    # 存在しないときはNoneが返る
    #AttributeError: 'NoneType' object has no attribute 'text'
    # print(soup)
    print(soup.find('title'))
    print(soup.find('div'))
    # print(soup.find('h1'))
    print(soup.find('div').text)
    print('******')
    # print(soup.find_all('div'))
    print('******')
    el = soup.find(class_="image_class")
    print(el)
    print('******')
    el = soup.find(id='id1')
    print(el)
    tag = soup.new_tag('a', href='http://example.com/')
    tag.string = 'クリックしてね'  # タグのテキストを設定
    div = soup.find('div')
    div.insert(0, tag)  # 0番目の位置にタグを挿入
    soup.div = div
    ##
    tag = soup.new_tag('a', href='http://localhost/')
    tag.string = 'クリックしてね'  # タグのテキストを設定
    num = len(soup.body.contents)
    soup.body.insert(num-1, tag)
    # soup.body.insert(num+10, tag) # エラーにはならない

    ##
    # soup.div.insert(0,tag)
    selector = 'body > table > thead > tr > th'
    elems = soup.select(selector)
    #子の要素を取得
    # for child in soup.body.contents:
    print(elems[0].contents[0])
    
    import re
    elems = soup.find_all(href=re.compile("https://ai-inter1.com/beautifulsoup_1/"))
    print(elems[0])
    print(elems[0].attrs['href'])
    # soup.title.parent

    # for child in soup.head.descendants:
    print('//////')
    for child in soup.head.descendants:
        if child != '\n':
            print(child)

    print('/////////////')
    buf = soup.prettify()
    print(buf)
    wpath = get_path(path)
    with open(wpath, 'w', encoding='utf-8')as f:
        f.write(buf)
    return

def get_path(path:str):
    import os
    import datetime
    base_name = os.path.splitext(path)[0]
    dstr = datetime.datetime.now().strftime('_%y%m%d_%H%M%S_')
    file_name = base_name + dstr + os.path.splitext(path)[1]
    dir = os.path.dirname(path)
    return os.path.join(dir, file_name)


if __name__ == '__main__':
    # test_main()
    test_main2()
