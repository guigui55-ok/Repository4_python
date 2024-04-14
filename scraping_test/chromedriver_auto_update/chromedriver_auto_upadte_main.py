"""
chromedriver の binary を更新するスクリプト


"""
import urllib
import zipfile
import os
import requests
from urllib import request

# 指定されたバージョンのWebDriverをダウンロードする関数
def download_webdriver_version(version, file_url):
    """
    chromedriverのバイナリを取得する。
        file_url から 対象の version の zip ファイルをダウンロードして、その中のバイナリのパスを取得する。
         ダウンロードは このスクリプトの場所の chromedriver_binary フォルダに、
          DLしたzipは chromedriver_binary / chromedriver_xxx.x.xxxx.xxx フォルダを作成してその中に解凍する。
           つまり、バイナリのパスは以下の通りとなる。
            __file__.parent > chromedriver_binary > chromedriver_xxx.x.xxxx.xxx > chromedriver-platform > chromedriver.exe
    
    Args:
        version : ダウンロードするバージョン
        file_url : ダウンロードするzipのurl

    Memo:
        file_url は外部で取得すること
    """
    from pathlib import Path
    dl_dir = Path(__file__).parent.joinpath('chromedriver_binary')
    file_name = 'chromedriver_{}.zip'.format(version)
    save_path = str(dl_dir.joinpath(file_name))
    print(version + ' のバージョンをダウンロードします。')
    print('ダウンロードURL = {}'.format(file_url))
    print('# zipファイルをダウンロード')
    with request.urlopen(file_url) as download_file:
        data = download_file.read()
        with open(save_path, mode='wb') as save_file:
            save_file.write(data)
    print('# zipファイルダウンロード完了 : {}'.format(save_path))
    # 240413
    # zipファイルの中身は[chromedriver.exe , LICENSE.chromedriver]
    print('# ダウンロードしたzipファイルを解凍')
    import shutil
    unzip_dir = dl_dir.joinpath(Path(save_path).stem)
    unzip_dir.mkdir(exist_ok=True)
    shutil.unpack_archive(save_file.name, str(unzip_dir))
    print('# zipファイルはいらないので削除 ')
    os.remove(save_path)
    # chromedriver_binary > chromedriver_xxx.x.xxxx.xxx > chromedriver-platform > chromedriver.exe があるはず
    import glob
    paths = glob.glob(str(unzip_dir) + '/**/chromedriver*', recursive=True)
    paths = list(paths)
    for path in paths:
        if Path(path).is_file():
            downloaded_chromedriver_binary_path = path
            break
    if len(paths)<1:
        msg = 'ダウンロードしたzipにchromedriverが見つからない。'
        msg += '(unzip dir = {})'.format(unzip_dir)
        raise Exception(msg)
    print('# 対象のchromedriverの用意が完了。 ')
    print('downloaded_chromedriver_binary_path = {}'.format(downloaded_chromedriver_binary_path))
    return downloaded_chromedriver_binary_path
    

def _debug_print(value, is_print:bool):
    if is_print:
        print(str(value))

def get_cheomr_version_and_url(target_major_ver, target_platform, is_print:bool=True):
    """
    chromedriver の バージョンとurl一覧のjson から、
        chromedriverのバイナリのダウンロードバージョンとURLを取得する
            メジャーバージョンの最後のVerを取得する

    Args:
        target_major_ver :
            目的のchromedriver のメジャーバージョンを指定する
                （より絞り込みたい場合は、マイナーバージョンを含んでもよい）
        target_platform :
            目的のプラットフォームを指定する
                PLATFORMS = ['linux64', 'mac-arm64', 'mac-x64', 'win32', 'win64']
    
    Returns:
        {str, str} : chromedriverのバージョン, chromedriverのダウンロードURL
    """
    url_json = 'https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json'
    
    _debug_print('read url = {}'.format(url_json), is_print)
    from pathlib import Path
    file_name = '__sample_' + Path(__file__).stem + '_chromedriver_ver_list.json'
    save_path = Path(__file__).parent.joinpath(file_name)
    save_path = str(save_path)
    with request.urlopen(url_json) as download_file:
        data = download_file.read()
        with open(save_path, mode='wb') as save_file:
            save_file.write(data)
    _debug_print('json saved = {}'.format(save_path), is_print)
    import json
    json_open = open(save_path, 'r')
    json_load:dict = json.load(json_open)
    import pprint
    _debug_print('*****', is_print)
    #/
    # メジャーバージョンがおないものは、本当にたくさんあるので、
    # 特定のバージョンのみを絞り込む
    #/
    # json_load には'timestamp' と 'versions' keyがある
    versions_dict:'list[dict]' = json_load['versions']
    # versions_dict=versions_dict[-110:]
    temp_json_list:'list[dict]' = []
    for i, buf_data in enumerate(versions_dict):
        version = buf_data['version']
        if str(version)[:3] == target_major_ver:
            _debug_print('[{}] version = {}'.format(i, version), is_print)
            temp_json_list.append(buf_data)
    _debug_print('version[{}] matched len = {}'.format(target_major_ver, len(temp_json_list)), is_print)
    # 絞り込んだメジャーバージョンの最後のものだけを採用する。
    for i, buf_data in enumerate(temp_json_list[-1:]):
        _debug_print('===============================', is_print)
        _debug_print('i = {}'.format(i), is_print)
        version = buf_data['version']
        _debug_print('version = {}'.format(version), is_print)
        buf_data_b:'list' = buf_data['downloads']['chromedriver']
        ret_dict = [x for x in buf_data_b if  x['platform']==target_platform]
        ret_url = ret_dict[0]['url']
        if is_print:
            pprint.pprint(ret_dict)
    return str(version), str(ret_url)


"""
JSONの中身の一部配下の通り
===============================
i = 4
{'downloads': {'chrome': [{'platform': 'linux64',
                           'url': 'https://storage.googleapis.com/chrome-for-testing-public/125.0.6418.0/linux64/chrome-linux64.zip'},
                          {'platform': 'mac-arm64',
                           'url': 'https://storage.googleapis.com/chrome-for-testing-public/125.0.6418.0/mac-arm64/chrome-mac-arm64.zip'},
                          {'platform': 'mac-x64',
                           'url': 'https://storage.googleapis.com/chrome-for-testing-public/125.0.6418.0/mac-x64/chrome-mac-x64.zip'},
                          {'platform': 'win32',
                           'url': 'https://storage.googleapis.com/chrome-for-testing-public/125.0.6418.0/win32/chrome-win32.zip'},
                          {'platform': 'win64',
                           'url': 'https://storage.googleapis.com/chrome-for-testing-public/125.0.6418.0/win64/chrome-win64.zip'}],
               'chrome-headless-shell': [{'platform': 'linux64',
                                          'url': 'https://storage.googleapis.com/chrome-for-testing-public/125.0.6418.0/linux64/chrome-headless-shell-linux64.zip'},
                                         {'platform': 'mac-arm64',
                                          'url': 'https://storage.googleapis.com/chrome-for-testing-public/125.0.6418.0/mac-arm64/chrome-headless-shell-mac-arm64.zip'},
                                         {'platform': 'mac-x64',
                                          'url': 'https://storage.googleapis.com/chrome-for-testing-public/125.0.6418.0/mac-x64/chrome-headless-shell-mac-x64.zip'},
                                         {'platform': 'win32',
                                          'url': 'https://storage.googleapis.com/chrome-for-testing-public/125.0.6418.0/win32/chrome-headless-shell-win32.zip'},
                                         {'platform': 'win64',
                                          'url': 'https://storage.googleapis.com/chrome-for-testing-public/125.0.6418.0/win64/chrome-headless-shell-win64.zip'}],
               'chromedriver': [{'platform': 'linux64',
                                 'url': 'https://storage.googleapis.com/chrome-for-testing-public/125.0.6418.0/linux64/chromedriver-linux64.zip'},
                                {'platform': 'mac-arm64',
                                 'url': 'https://storage.googleapis.com/chrome-for-testing-public/125.0.6418.0/mac-arm64/chromedriver-mac-arm64.zip'},
                                {'platform': 'mac-x64',
                                 'url': 'https://storage.googleapis.com/chrome-for-testing-public/125.0.6418.0/mac-x64/chromedriver-mac-x64.zip'},
                                {'platform': 'win32',
                                 'url': 'https://storage.googleapis.com/chrome-for-testing-public/125.0.6418.0/win32/chromedriver-win32.zip'},
                                {'platform': 'win64',
                                 'url': 'https://storage.googleapis.com/chrome-for-testing-public/125.0.6418.0/win64/chromedriver-win64.zip'}]},
 'revision': '1287014',
 'version': '125.0.6418.0'}

"""

PLATFORMS = ['linux64', 'mac-arm64', 'mac-x64', 'win32', 'win64']
_TARGET_PLATFORM = 'win64'
# _VERSION = '123.0.6312.123'
_TARGET_MAJOR_VER = '123'
if __name__ == '__main__':
    version, download_url = get_cheomr_version_and_url(
        target_major_ver=_TARGET_MAJOR_VER,
        target_platform=_TARGET_PLATFORM,
        is_print=False)
    download_webdriver_version(version, download_url)