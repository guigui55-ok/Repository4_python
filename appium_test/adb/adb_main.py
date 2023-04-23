import subprocess
from subprocess import CompletedProcess, PIPE, STDOUT 

import os
import datetime
from typing import Union
import pathlib
def _get_date_str():
    return datetime.datetime.now().strftime('%y%m%d_%H%M%S_')

NEW_LINE = str('\n')
CRLF = '\r\n'
TAB = '\t'

def write_stdout(path:str, result: 'Union[CompletedProcess,str]'):
    if os.path.isdir(path):
        file_name = _get_date_str() + 'adb.txt'
        path = os.path.join(path, file_name)
    if isinstance(result , CompletedProcess):
        wbuf = get_stdout_from_result(result)
    else:
        wbuf = str(result)
    if len(wbuf)<1:
        print('###  Write Data Is Nothing. ###')
        return ''
    with open(path, 'w', encoding='utf-8')as f:
        f.write(wbuf)
    return path

def excute_command(command:str = ''):
    """
    コマンドを実行し、結果を取得する
     戻り値は(bool,str)
    """
    result = get_result_subprocess_run_command(command)
    ret_bool = is_success_adb_result(result)
    stdout = get_stdout_from_result(result)
    return ret_bool, stdout

def get_stdout_from_result(result:CompletedProcess):
    """
    CompletedProcess からstdout または stderr を文字列で取得する
    """
    # title = '#####  STDOUT/STDERR  #####'
    title = ''
    buf:str = result.stdout.decode('shift-jis')
    """
    adb deviceが認識されていない場合は以下のエラーとなる
    "adb.exe: device unauthorized.\r\nThis adb server's $ADB_VENDOR_KEYS is not set\r\nTry 'adb kill-server' if that seems wrong.\r\nOtherwise check for a confirmation dialog on your device.\r\n"
    """
    if buf!='':
        buf = buf.replace(CRLF , NEW_LINE)
        # ret_str = title + NEW_LINE + buf
        ret_str = buf
    else:
        ret_str = ''
    return ret_str

def adb_shell_with_show_result(command:str):
    """
    subprocess.run でコマンドを実行する
    """
    ret = get_result_subprocess_run_command(command)
    return ret

def subprocess_popen(command:str):
    result = subprocess.Popen(
        command,
        shell=True,
        stdout=PIPE,
        stderr=STDOUT,
        text=False)
    return result


def get_result_subprocess_run_command(command:str):
    """ subprocess.run でコマンドを実行する """
    result = subprocess.run(
        command,
        shell=True,
        stdout=PIPE,
        stderr=STDOUT,
        text=False)
    #https://docs.python.org/ja/3/library/subprocess.html
    #capture_output を true に設定すると、stdout および stderr が捕捉されます。]
    #text=True
    #UnicodeDecodeError: 'cp932' codec can't decode byte 0x85 in position 62153: illegal multibyte sequence
    # プロセスが stderr=subprocess.STDOUT で実行された場合、標準出力と標準エラー出力が混合されたものがこの属性に格納され、stderr は None になります
    return result

def is_success_adb_result(result):
    """subprocess.run の実行結果が成功したか判定する"""
    flag = False
    # returncode から bool に変換する
    if isinstance(result,CompletedProcess):
        if result.returncode != 0: 
            flag = False
        else:
            flag = True
    else:
        if result != 0:
            flag = False
        else:
            flag = True
    return flag


def get_connect_adb_devices() -> 'list[str,str]':
    """
    adb devices で取得される結果をList[str,str]で取得する
    """
    # 出力
    # List of devices attached
    # 2889adb7        offline
    # List of devices attached
    # 2889adb7        device
    cmd = 'adb devices'     
    _ ,ret = excute_command(cmd)
    buf:str = str(ret)
    results = buf.split(NEW_LINE)
    ret_id_list:'list[str]' = []
    # i=1 から実行する
    for i in range(len(results))[1:]:
        buf = results[i]
        if len(buf)>0:
            # device_id\tdevice
            info = buf.split(TAB)
            if info[1] == 'device':
                ret_id = info[0]
                ret_status = info[1]
                ret_id_list.append([ret_id,ret_status])            
    return ret_id_list

def get_device_product_model():
    """デバイスのプロダクトモデルを取得する"""
    cmd = 'adb shell getprop ro.product.model'
    result = get_result_subprocess_run_command(cmd)
    ret = get_stdout_from_result(result)
    return ret.strip()

def get_android_version():
    cmd = 'adb shell getprop ro.build.version.release'
    result = get_result_subprocess_run_command(cmd)
    ret = get_stdout_from_result(result)
    ret = erase_beggining_adb_result(ret)
    return ret.strip()

def erase_beggining_adb_result(result_str:str):
    #'* daemon not running; starting now at tcp:5037\n* daemon started successfully\n11\n'
    lines = result_str.split(NEW_LINE)
    ret = ''
    for l in lines:
        if l=='': continue
        if 'daemon not running' in l: continue
        if 'daemon started' in l: continue
        ret += str(l) + NEW_LINE
    ret = ret[:-1]
    return ret

###################
def test_excute_adb_and_save_stdout():
    ###
    desc = 'インストール済みのパッケージ名一覧'
    cmd = 'adb shell pm list package'
    is_write = True
    ###
    desc = 'パッケージの詳細情報'
    cmd = 'adb shell pm dump [package]'
    package = 'com.kirito.app.wallpaper.rezero'
    package = 'com.sega.stella'
    cmd = cmd.replace('[package]', package)
    is_write = True
    ###
    desc = 'パッケージを起動する'
    cmd = 'adb shell am start -n [package]/[classname]'
    # package = 'com.kirito.app.wallpaper.rezero'
    # activity = 'com.kirito.app.wallpaper.activity.MainActivity'
    package = 'com.sega.stella'
    activity = 'com.facebook.CustomTabActivity'
    cmd = cmd.replace('[package]', package)
    cmd = cmd.replace('[classname]', activity)
    is_write = False
    ###
    desc = 'Androidのバージョンを取得する'
    cmd = 'adb shell getprop ro.build.version.release'
    is_write = False
    ###
    print('command = {}'.format(cmd))
    flag,stdout = excute_command(cmd)
    if is_write:
        path = write_stdout(os.path.dirname(__file__),stdout)
        print(path)
    else:
        print(stdout)
    print('command is success = {}'.format(flag))

if __name__ == '__main__':
    # print(_get_date_str())
    # test_excute_adb_and_save_stdout()
    l = get_connect_adb_devices()
    print(l)
    model = get_device_product_model()
    print(model)