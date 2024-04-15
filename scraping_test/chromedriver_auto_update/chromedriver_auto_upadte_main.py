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
         ダウンロードしたファイルはは このスクリプトの場所の chromedriver_binary フォルダに保存される。
          DLしたzipは chromedriver_binary / chromedriver_xxx.x.xxxx.xxx フォルダを作成してその中に解凍する。
           つまり、zip解凍後のバイナリのパスは以下の通りとなる。
            __file__.parent > chromedriver_binary > chromedriver_xxx.x.xxxx.xxx > chromedriver-[platform] > chromedriver.exe
    
    Args:
        version : ダウンロードするバージョン
        file_url : ダウンロードするzipのurl

    Resutns:
        {str} : downloaded_chromedriver_binary_path
        
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
                （より絞り込みたい場合は、マイナーバージョンを含んでもよいが、chromeのバージョンとjsonの中の値と合致しない場合がよくあるので要確認）
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

# https://qiita.com/yuyhiraka/items/6debaf0ad20a7fd4426c
def get_command_chrome_browser_version_win():
    """ コマンドでChromeブラウザのバージョンを取得する Windows """
    win_cmd = 'dir /B /O-N "C:\Program Files (x86)\Google\Chrome\Application" | findstr "^[0-9].*¥>'
    from excute_command_main import excute_command
    ret = excute_command(win_cmd)
    return ret[0].strip()

def get_command_chrome_browser_version_mac():
    """ コマンドでChromeブラウザのバージョンを取得する Mac """
    mac_cmd = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version'
    from excute_command_main import excute_command
    ret = excute_command(mac_cmd)
    return ret[0].strip()

def get_command_chrome_browser_version():
    """ コマンドでChromeブラウザのバージョンを取得する Windows/Mac """
    import platform
    pf = platform.system()
    if pf == 'Windows':
        # print('on Windows')
        return get_command_chrome_browser_version_win()
    elif pf == 'Darwin':
        # print('on Mac')
        return get_command_chrome_browser_version_mac()
    elif pf == 'Linux':
        print('on Linux')
        raise NotImplementedError()

def get_chrome_major_version(version):
    """
    Chromeのバージョン文字列からメジャーバージョンを取得する
        例）123.0.6312.122.0  > 123
    """
    pos = str(version).find('.')
    return str(version)[:pos]

from pathlib import Path
def get_pip_package_path(package_name):
    """
    pip install のパッケージのインストールフォルダパスを取得する
    """
    mac_cmd = 'pip show {}'.format(package_name)
    from excute_command_main import excute_command
    ret_lines = excute_command(mac_cmd)
    for line in ret_lines:
        if 'WARNING: Package(s) not found'in line:
            raise Exception('パッケージが存在しません。(package_name={})'.format(package_name))
        if 'Name:' in line:
            name = line.replace('Name:', '').strip()
        if 'Location:' in line:
            location = line.replace('Location:', '').strip()
    ret = Path(location).joinpath(name)
    return str(ret)
# """ packageがないときは以下となる
# C:\Users\OK>pip show aaa
# WARNING: Package(s) not found: aaa
# """

def get_chromedriver_path_in_pip():
    """
    pip chromedriver-binary パッケージの中のchromedriver実行ファイルのパスを取得する
    """
    path = get_pip_package_path('chromedriver-binary')
    import platform
    pf = platform.system()
    if pf == 'Windows':
        # print('on Windows')
        file_name = 'chromedriver.exe'
    elif pf == 'Darwin':
        # print('on Mac')
        file_name = 'chromedriver'
    elif pf == 'Linux':
        print('on Linux')
        file_name = 'chromedriver'
    return Path(path).joinpath(file_name)

def get_chromedriver_ver_in_pip():
    """
    pip の chromedriver-binary のバージョンを取得する
    """
    mac_cmd = 'pip show chromedriver-binary'
    from excute_command_main import excute_command
    ret_lines = excute_command(mac_cmd)
    for line in ret_lines:
        if 'Version:' in line:
            ret = line.replace('Version:', '').strip()
            break
    return ret
# """
# C:\Users\OK>pip show chromedriver-binary
# Name: chromedriver-binary
# Version: 123.0.6312.122.0
# Summary: Installer for chromedriver.
# Home-page: https://github.com/danielkaiser/python-chromedriver-binary
# Author: Daniel Kaiser
# Author-email: daniel.kaiser94@gmail.com
# License: MIT
# Location: c:\program files\python\python310\lib\site-packages
# Requires:
# Required-by:"""



def update_chrome_driver_in_target_dir(targeet_dir):
    chrome_ver = get_command_chrome_browser_version()
    print('chrome_ver = {}'.format(chrome_ver))
    major_ver = get_chrome_major_version(chrome_ver)
    json_version, download_url = get_cheomr_version_and_url(
        target_major_ver=major_ver,
        target_platform=_TARGET_PLATFORM,
        is_print=False)
    print('chromedriver json version = {}'.format(json_version))
    print('chromedriver url = {}'.format(download_url))
    downloaded_chromedriver_binary_path = download_webdriver_version(json_version, download_url)
    import shutil
    shutil.copy(
        src=downloaded_chromedriver_binary_path,
        dst=targeet_dir)
    from pathlib import Path
    print('COPIED [{}] = {}'.format(Path(downloaded_chromedriver_binary_path).name, targeet_dir))


def _test_method():
    """ テストいろいろ """
    chrome_ver = get_command_chrome_browser_version()
    print('chrome_ver = {}'.format(chrome_ver))
    major_ver = get_chrome_major_version(chrome_ver)
    json_version, download_url = get_cheomr_version_and_url(
        target_major_ver=major_ver,
        target_platform=_TARGET_PLATFORM,
        is_print=False)
    print('chromedriver json version = {}'.format(json_version))
    print('chromedriver url = {}'.format(download_url))
    #/
    cmd = 'pip install chromedriver-binary=={}'.format(json_version)
    from excute_command_main import excute_command
    ret_lines = excute_command(cmd)
    print(''.join(ret_lines))
#     """
#     pip chromedriverインストール成功時
# ['Collecting chromedriver-binary==123.0.6312.122\n', '  Downloading chromedriver-binary-123.0.6312.122.0.tar.gz (5.6 kB)\n', '  Preparing metadata (setup.py): started\n', "  Preparing metadata (setup.py): finished with status 'done'\n", 'Building wheels for collected packages: chromedriver-binary\n', '  Building wheel for chromedriver-binary (setup.py): started\n', "  Building wheel for chromedriver-binary (setup.py): finished with status 'done'\n", '  Created wheel for chromedriver-binary: filename=chromedriver_binary-123.0.6312.122.0-py3-none-any.whl size=8504202 sha256=26a85824b4acc7ba86178cc04200a4e1588aec60b0a90030e43a18fb24659b6e\n', '  Stored in directory: c:\\users\\ok\\appdata\\local\\pip\\cache\\wheels\\cd\\84\\ca\\cdd030eccc82592e1d0023e650cf276dd913ac329469c7e2a8\n', 'Successfully built chromedriver-binary\n', 'Installing collected packages: chromedriver-binary\n', '  Attempting uninstall: chromedriver-binary\n', '    
# Found existing installation: chromedriver-binary 102.0.5005.61.0\n', '    Uninstalling chromedriver-binary-102.0.5005.61.0:\n', '      Successfully uninstalled chromedriver-binary-102.0.5005.61.0\n', 'Successfully installed chromedriver-binary-123.0.6312.122.0\n']
#     pip chromedriver インストールしてすでにあるとき
#     Requirement already satisfied: chromedriver-binary==123.0.6312.122 in c:\program files\python\python310\lib\site-packages (123.0.6312.122.0)
#     """
    #/
    pip_chromedriver_ver = get_chromedriver_ver_in_pip()
    print('chromedriver pip_chromedriver_ver = {}'.format(pip_chromedriver_ver))
    pip_chromedriver_binary_file_path = get_chromedriver_path_in_pip()
    print('pip_chromedriver_binary_file_path = {}'.format(pip_chromedriver_binary_file_path))
    #/
    # download_webdriver_version(json_version, download_url)

CHROME_DRIVER_PATH = r'C:\Users\OK\source\programs\chromedriver_win32\chromedriver'
####
PLATFORMS = ['linux64', 'mac-arm64', 'mac-x64', 'win32', 'win64']
_TARGET_PLATFORM = 'win64'
# _VERSION = '123.0.6312.123'
_TARGET_MAJOR_VER = '123'
####
if __name__ == '__main__':
    update_chrome_driver_in_target_dir(CHROME_DRIVER_PATH)