"""
非同期確認用スクリプト
    3秒おきに標準出力に文字列（ファイル名と日付）を出力する
    コマンドライン引数で実行時間を設定する（秒）
"""


import sys
import time
from datetime import datetime

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <duration_in_seconds>")
        sys.exit(1)

    try:
        duration = int(sys.argv[1])
    except ValueError:
        print("The duration must be an integer.")
        sys.exit(1)

    start_time = datetime.now()
    file_name = __file__

    elapsed_time = 0
    while elapsed_time < duration:
        current_time = datetime.now()
        elapsed_time = (current_time - start_time).seconds
        print(f"{file_name} {elapsed_time} sec {current_time}")
        time.sleep(3)

    print("Script finished.")

if __name__ == "__main__":
    main()