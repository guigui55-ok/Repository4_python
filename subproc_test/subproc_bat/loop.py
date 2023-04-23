"""
Python スクリプトの実行中にリアルタイムで出力を表示するには、バッチファイルで python コマンドの後に -u オプションを追加します。これにより、Python の標準出力がアンバッファリングモードになり、リアルタイムで表示されるようになります。

バッチファイル（例：run_python_script.bat）を以下のように更新してください。

bash
Copy code
@echo off
python -u myscript.py
pause
これで、myscript.py の実行中に出力がリアルタイムでコマンドプロンプトに表示されるはずです。
"""

"""

ちなみに、macのshファイル（シェルファイル）の場合は以下の通り。

シェルスクリプト内で自分自身に実行権限を付与し、実行するには、以下のように run_python_script.sh を作成します。

bash
Copy code
#!/bin/sh

# 実行権限を付与
chmod +x "$0"

# Pythonスクリプトを実行
python -u myscript.py
このスクリプトでは、$0 はシェルスクリプト自身のファイル名を表します。chmod +x "$0" で、シェルスクリプトに実行権限が付与されます。ただし、この方法では最初の実行時に実行権限を付与するため、最初の実行時にはPythonスクリプトが実行されません。2回目以降の実行でPythonスクリプトが正常に実行されます。

最初の実行時にもPythonスクリプトを実行する場合は、以下のようにスクリプトを作成します。

bash
Copy code
#!/bin/sh

# シェルスクリプトが実行可能であることを確認
if [ ! -x "$0" ]; then
    chmod +x "$0"
    # スクリプトを再実行
    exec "$0" "$@"
fi

# Pythonスクリプトを実行
python -u myscript.py
このスクリプトでは、-x オプションを使ってシェルスクリプトが実行可能かどうかを確認し、実行可能でなければ実行権限を付与してスクリプトを再実行します。これにより、最初の実行時にもPythonスクリプトが実行されます。

"""


import time
def main():
    max = 5
    count = 0
    while True:
        count += 1
        print('*', end='')
        time.sleep(1)
        if max < count:
            print('')
            break
    print('done.')
    return


if __name__ == '__main__':
    main()