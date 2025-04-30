"""
URLの文字列のリストが記載されているテキストファイルを読み込み、
URLのショートカットファイル（lnk）を作成する
"""
"""
ModuleNotFoundError: No module named 'winshell'

winshellモジュールがインストールされていないことが原因で、ModuleNotFoundErrorエラーが発生しています。winshellはWindowsのショートカットを操作するためのライブラリであるため、Windows環境でのみ使用することができます。

以下の手順で、winshellモジュールをインストールすることができます。

コマンドプロンプトを開きます。
pip install pywin32を実行します。
pip install winshellを実行します。
これでwinshellモジュールがインストールされ、ショートカットの作成が可能になります。
"""

"""
■shortcut.save() でエラーとなるケース

URLから取得したタイトル
\x83\x89\x83Y\x83p\x83C\x81\x95\x83o\x81[\x83R\x81[\x83h\x82Å\x8dH\x8fê\x93à\x83g\x83\x8c\x81[\x83T\x83r\x83\x8a\x83e\x83B\x81[\x82Ì\x90¸\x93x\x8cü\x8fã\x82ð\x90}\x82é\x81F\x83\x89\x83Y\x83p\x83C\x82Å\x90»\x91¢\x8bÆ\x82Ì\x82¨\x8eè\x8cyIoT\x8a\x88\x97p\x81i13\x81j\x81i1/2_\x83y\x81[\x83W\x81j_-_MONOist

文字列として変換
"???Y?p?C???o?[?R?[?h?A?H?e?a?g???[?T?r???e?B?[?I?，?x?u?a?d?}?e?F???Y?p?C?A?≫?￠?A?I?¨?e?yIoT???p?i13?" 


'c:\\Users\\OK\\source\\repos\\Repository4_python\\tool_create_shortcut_url\\shortcuts\\\x83\x89\x83Y\x83p\x83C\x81\x95\x83o\x81[\x83R\x81[\x83h\x82Å\x8dH\x8fê\x93à\x83g\x83\x8c\x81[\x83T\x83r\x83\x8a\x83e\x83B\x81[\x82Ì\x90¸\x93x\x8cü\x8fã\x82ð\x90}\x82é\x81F\x83\x89\x83Y\x83p\x83C\x82Å\x90»\x91¢\x8bÆ\x82Ì\x82¨\x8eè\x8cyIoT\x8a\x88\x97p\x81i13\x81.url'

'ã\x83ªã\x83³ã\x82¯&#x2F;ã\x83\x9cã\x82¿ã\x83³&#x2F;ã\x83\x95ã\x82©ã\x83¼ã\x83\xa0ã\x82\x92ã\x82\x88ã\x82\x8aè\x89¯ã\x81\x8fã\x81\x99ã\x82\x8bHTMLã\x83»CSS_17é\x81¸_-_ICS_MEDIA'

'ã\x83ªã\x83³ã\x82¯&#x2F;ã\x83\x9cã\x82¿ã\x83³&#x2F;ã\x83\x95ã\x82©ã\x83¼ã\x83\xa0ã\x82\x92ã\x82\x88ã\x82\x8aè\x89¯ã\x81\x8fã\x81\x99ã\x82\x8bHTMLã\x83»CSS_17é\x81¸_-_ICS_MEDIA'


ã\x83ªã\x83³ã\x82¯&#x2F;ã\x83\x9cã\x82¿ã\x83³&#x2F;ã\x83\x95ã\x82©ã\x83¼ã\x83\xa0ã\x82\x92ã\x82\x88ã\x82\x8aè\x89¯ã\x81\x8fã\x81\x99ã\x82\x8bHTMLã\x83»CSS_17é\x81¸_-_ICS_MEDIA


url=https://qiita.com/tatsumi_t2/items/1a19a588682d78c90bfa
title=「悪〜いコード」を読んだので、ついでにコードメトリクスを計測してみた - Qiita

create_target_path=c:\Users\OK\source\repos\Repository4_python\tool_create_shortcut_url\shortcuts\悪〜 
いコードを読んだので、ついでにコードメトリクスを計測してみた_-_Qiita.url


"""


import os
import sys
import requests
import winshell
from win32com.client import Dispatch
from win32com.client.dynamic import CDispatch

import re

def sanitize_filename(filename: str) -> str:
    # 置き換える文字の正規表現パターン
    pattern = r'[\\/*?:"<>|]'

    # 置き換える文字をアンダースコアに置き換える
    sanitized_filename = re.sub(pattern, '_', filename)
    sanitized_filename = sanitized_filename.replace('\n','')

    # 特定の文字列を除外する
    sanitized_filename = sanitized_filename.replace('「', '').replace('」', '')

    return sanitized_filename

# # ショートカットを作成する関数
# def create_shortcut(url, target_path):
#     shell = Dispatch('WScript.Shell')
#     shortcut = shell.CreateShortCut(target_path)
#     shortcut.Targetpath = url
#     shortcut.save()

# ショートカットを作成する関数
def create_shortcut(url, target_dir):
    # URLからタイトルを取得
    print(f'url={url}')
    response = requests.get(url)
    title = response.text.split('<title>')[1].split('</title>')[0]
    print(f'title={title}')
    _REPLACE_CHAR = '_'
    title = title.strip().replace(' ', _REPLACE_CHAR)
    # ショートカットのファイル名を作成
    filename = title + '.url'
    sanitized_filename  = sanitize_filename(filename)
    if 120 < len(sanitized_filename):
        sanitized_filename = sanitized_filename[:100] + '.url'
    target_path = os.path.join(target_dir, sanitized_filename )
    ###
    if '\x83' in title or 'ã\x83' in title:
        title_new = decode_japanese_title(title)
        if title_new == '':
            title_new=url
        filename = title_new + '.url'
        sanitized_filename  = sanitize_filename(filename)
        # 122文字のファイル名でエラーとなることがあった（詳細不明）
        # パスの長さかもしれない
        if 120 < len(sanitized_filename):
            sanitized_filename = sanitized_filename[:100] + '.url'
        target_path = os.path.join(target_dir, sanitized_filename )
    ###
    target_path = replace_emoji(target_path, _REPLACE_CHAR)
    target_path = replace_specal_char(target_path, _REPLACE_CHAR)
    if sanitized_filename == '.url':
        print()
    # ショートカットを作成
    print(f'\ncreate_target_path={target_path}\n')
    shell:CDispatch = Dispatch('WScript.Shell')
    shortcut  = shell.CreateShortCut(target_path)
    shortcut.Targetpath = url
    shortcut.save()
    return

def replace_specal_char(text, replacement):
    values = ['〜']
    for value in values:
        text = text.replace(value, replacement)
    return text

def replace_emoji(text, replacement):
    # 絵文字を置き換える正規表現パターン
    emoji_pattern = re.compile("[\U0001F000-\U0001F6FF]|[\U0001F900-\U0001F9FF]")
    # 絵文字を指定された文字列に置き換える
    return emoji_pattern.sub(replacement, text)

def decode_japanese_title(title):
    try:
        decoded_title = title.encode('iso-8859-1').decode('shift-jis')
        return decoded_title
    except UnicodeDecodeError as e:
        import html
        # HTMLエンティティをデコード
        decoded_title = html.unescape(title)
        print(title)
        # print(type(title))
        title = title.encode('utf-8')
        decoded_title = title.decode('utf-8')
        print(decoded_title)
        return ""
    except Exception as e:
        print('Exception = ' + str(e))
        return ""


def excute_create_shortcut_url_main(read_path, target_dir):
    read_path = str(read_path)
    target_dir = str(target_dir)

    # URLのリストを含むファイルを読み込む
    with open(read_path, 'r') as f:
        urls = f.readlines()

    # ディレクトリが存在しない場合は作成する
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # ショートカットを作成する
    for url in urls:
        url = url.strip() # URLの前後の空白を削除
        # filename = os.path.splitext(os.path.basename(url))[0] + '.lnk'
        filename = ''
        target_path = os.path.join(target_dir, filename)
        create_shortcut(url, target_path)
        print(f'created. url={url}')
    print('*****')
    print(f'target_dir={target_dir}')
    return

def main():
    # ショートカットを作成するディレクトリを設定
    desktop = winshell.desktop()
    from pathlib import Path
    target_dir_path = Path(__file__).parent
    shortcut_dir = target_dir_path.joinpath('shortcuts')
    read_path = target_dir_path.joinpath('shortcut_list.txt')
    excute_create_shortcut_url_main(read_path, shortcut_dir)

if __name__ == '__main__':
    print()
    print('*****')
    main()


