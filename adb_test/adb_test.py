# This Python file uses the following encoding: utf-8
# pip install android-auto-play-opencv
import android_auto_play_opencv as am
adbpath = '..\\platform-tools\\'
def main():
    aapo = am.AapoManager(adbpath)
    while True:
        # 画面キャプチャ
        aapo.screencap()
if __name__ == '__main__':
    main()