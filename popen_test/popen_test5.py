
"""
Popenでコマンド実行テスト
    結果を文字列で取得
"""

import sys
import subprocess

# https://qiita.com/megmogmog1965/items/5f95b35539ed6b3cfa17
def get_lines(cmd):
    '''
    :param cmd: str 実行するコマンド.
    :rtype: generator
    :return: 標準出力 (行毎).
    '''
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    while True:
        line = proc.stdout.readline()
        if line:
            yield line

        if not line and proc.poll() is not None:
            break

# https://python.civic-apps.com/python3-bytes-str-convert/
def cnv_byte_to_str(value)->str:
    try:
        # if type(value) is type(Bytes): # not define
        ret = value.decode('utf-8')
        return ret
    except Exception as e:
        print(str(e))
        return ''

if __name__ == '__main__':
    cmd = 'adb shell getevent /dev/input/event2'
    for line in get_lines(cmd):
        buf = cnv_byte_to_str(line)
        sys.stdout.write(buf)