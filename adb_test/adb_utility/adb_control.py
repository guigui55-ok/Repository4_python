import subprocess
logger = None

def input_keyevent(keycode:str = ''):
    """キーイベントを送信する"""
    try:
        if keycode!='':
            subprocess.call('adb shell input keyevent ' + keycode)
        else:
            logger.error('keycode value is nothing')
    except Exception as e:
        logger.error(e)
"""
※Keyevent 一例
KEYCODE_HOME	ホーム キー
KEYCODE_BACK	バック(戻る)キー
KEYCODE_CAMERA	カメラキー
KEYCODE_COPY	コピーキー
KEYCODE_PASTE	ペーストキー
KEYCODE_POWER	電源ボタン　(起動状態ならスリープ、スリープ中なら復帰)
KEYCODE_SLEEP	スリープ (スリープ中に再実行しても何も起きない)
KEYCODE_WAKEUP	スリープ解除 (起動状態で再実行しても何も起きない)
"""

def adb_reboot():
    """再起動させる"""
    try: 
        subprocess.call('adb reboot')
    except Exception as e:
        logger.error(e)

def unlock():
    try:
        pass
    except Exception as e:
        logger.error(e)


def screen_capture_for_android(file_name = 'screenshot.png'):
    """スクリーンキャプチャをAndroidのSDルートに作成する"""
    try:
        screen_capture = (
            'adb', 'shell', 'screencap', '-p', 
            '/sdcard/' + file_name)
        subprocess.call(screen_capture)
    except Exception as e:
        logger.error(e)

def save_file_to_pc_from_android(
    android_path = '/sdcard/',
    file_name = 'screenshot.png'
):
    """android からファイルを取得する
    """
    try:
        screen_capture = (
            'adb', 'pull', android_path + file_name)
        subprocess.call(screen_capture)
    except Exception as e:
        logger.error(e)