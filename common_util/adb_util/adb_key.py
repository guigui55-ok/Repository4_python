import subprocess
logger = None

def input_keyevent(keycode:str = ''):
    """キーイベントを送信する"""
    result = 0
    try:
        if keycode!='':
            result = subprocess.call('adb shell input keyevent ' + keycode)
        else:
            logger.ext.error('keycode value is nothing')
        return result
    except Exception as e:
        logger.ext.error(e)
        return result