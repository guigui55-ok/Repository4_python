
# https://qiita.com/taiponrock/items/9001ae194571feb63a5e
# Node.js / npmをインストールする（for Windows）

# https://blog.baseballyama.tokyo/java/windows10%E3%81%ABappium%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/


# https://moewe-net.com/nodejs/opencv4nodejs-install-error
# https://dev.classmethod.jp/articles/completely-uninstall-nodejs-from-windows/

# https://qiita.com/exp/items/bdf06a388f30a1726984

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

package = 'com.sega.stella'
activity = 'com.facebook.CustomTabActivity'

def test_main():
    ### log file set
    timestamp = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    file_name = timestamp + '_appium_svr.log'
    appium_log_path = str(pathlib.Path(__file__).parent.joinpath(file_name))
    ###
    cmd = 'appium --log-timestamp -g {}'.format(appium_log_path)
    # cmd = ['appium','']
    # cmd = ['ipconfig','all']
    # proc = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
    proc = subprocess.Popen(cmd,shell=True)
    try:
        time.sleep(5)
        connect_device_main()
        time.sleep(3)
        proc.kill()
        outs, errs = proc.communicate()
    except subprocess.SubprocessError:
        proc.kill()
        outs, errs = proc.communicate()
    enc = 'utf-8'
    enc = 'shift-jis'
    if outs!=None:
        outs_str = outs.decode(enc,'ignore')
        print('outs = {}'.format(outs_str))
    if errs!=None:
        errs_str = errs.decode(enc).split('\n')
        print('errs = {}'.format(errs_str))
    return

def connect_device_main():
    print('connect_device_main')
    # ap_cmd = 'appium -p 9000 -a 127.0.0.1 -pa /wd/hub'
    # port = '9000'
    # address = '0.0.0.0'
    # address = 'localhost'
    # address = '127.0.0.1'
    # address = '192.168.1.9'
    # port = '80'
    # base_path = ''
    address = '127.0.0.1'
    port = '4723'
    base_path = '/wd/hub'
    ap_cmd = 'appium -p {} -a {} -pa {}'.format(port, address, base_path)
    print(ap_cmd)
    desired_caps = adb_desired_caps.create_desired_caps_for_android(
        package,activity)
    # http://127.0.0.1:4723/wd/hub
    url = 'http://{}:{}{}'.format(address, port, base_path)
    print(url)
    print(desired_caps)
    try:
        driver = webdriver.Remote(
            command_executor=url,
            desired_capabilities=desired_caps)
        time.sleep(3)
        # logs = driver.get_log('driver')
        # print('logs=')
        # print(logs)
        driver.quit()
    except:
        print()
        print('**********')
        import traceback
        traceback.print_exc()
        print('**********')
        print()


if __name__ == '__main__':
    test_main()


    #### ERROR ####
    
    # driver = webdriver.Remote(
    #     command_executor=url,
    #     options=desired_caps)