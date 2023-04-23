
# appimでAndroidデバイスに接続する方法について
# 関連ドキュメント
# Androidテスト自動化のためにappiumを導入(windows+python)
# https://qiita.com/exp/items/bdf06a388f30a1726984
# Node.js / npmをインストールする（for Windows）
# https://qiita.com/taiponrock/items/9001ae194571feb63a5e
# Windows10にAppiumをインストールする方法
# https://blog.baseballyama.tokyo/java/windows10%E3%81%ABappium%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/
# opencv4nodejsのインストールが失敗する時の解決方法
# https://moewe-net.com/nodejs/opencv4nodejs-install-error
# Windows 環境から Node.js を完全に削除する方法をやってみた
# https://dev.classmethod.jp/articles/completely-uninstall-nodejs-from-windows/


##########
# module import
##########
from subprocess import SubprocessError
from selenium.webdriver.remote.webdriver import WebDriver

from selenium import webdriver
import adb_desired_caps
import adb.adb_main as adb_main
import time
import pathlib
import datetime
import subprocess
from subprocess import PIPE

# 起動するアプリのpackageとacrivityを指定する
PACKAGE = 'com.sega.stella'
ACTIVITY = 'com.facebook.CustomTabActivity'

def test_appium_main():
    ### set log file_name
    timestamp = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    file_name = timestamp + '_appium_svr.log'
    appium_log_path = str(pathlib.Path(__file__).parent.joinpath(file_name))
    ###
    cmd = 'appium --log-timestamp -g {}'.format(appium_log_path)
    # appiumサーバーを起動する（ログはappium_log_pathに出力される）
    proc = subprocess.Popen(cmd,shell=True)
    try:
        # サーバー起動後に安定するまで待機する
        time.sleep(5)
        connect_and_controll_device_main()
        # appiumサーバーを終了させる
        proc.kill()
        outs, errs = proc.communicate()
    except subprocess.SubprocessError:
        ### エラー発生時の処理
        # appiumサーバーを終了させる
        proc.kill()
        outs, errs = proc.communicate()
        ###
    ### appiumサーバーを実行した後の結果の文字列を出力する
    # enc = 'utf-8'
    enc = 'shift-jis'
    if outs!=None:
        outs_str = outs.decode(enc,'ignore')
        print('outs = {}'.format(outs_str))
    if errs!=None:
        errs_str = errs.decode(enc).split('\n')
        print('errs = {}'.format(errs_str))
    ###
    return

def connect_and_controll_device_main():
    """
    appiumサーバーとデバイスを接続する
    """
    print('connect_device_main')
    address = '127.0.0.1'
    port = '4723'
    base_path = '/wd/hub'
    ap_cmd = 'appium -p {} -a {} -pa {}'.format(port, address, base_path)
    print(ap_cmd)
    desired_caps = adb_desired_caps.create_desired_caps_for_android(
        PACKAGE,ACTIVITY)
    # http://127.0.0.1:4723/wd/hub
    url = 'http://{}:{}{}'.format(address, port, base_path)
    print(url)
    print(desired_caps)
    print('##################  webdriver.Remote  ######################')
    try:
        driver = webdriver.Remote(
            command_executor=url,
            desired_capabilities=desired_caps)
        time.sleep(3)
        #########
        #########
        #操作したい内容をここに実装する
        #########
        #########
        driver.quit()
    except:
        print()
        print('**********')
        import traceback
        traceback.print_exc()
        print('**********')
        print()
    print('########################################')

if __name__ == '__main__':
    test_appium_main()
