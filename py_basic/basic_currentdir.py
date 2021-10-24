import os
# https://note.nkmk.me/python-os-getcwd-chdir/
# Pythonでカレントディレクトリを取得、変更（移動）
path = os.getcwd()
print('os.getcwd() = ' + path)

# Pythonでカレントディレクトリを変更（移動）
os.chdir('../')
path = os.getcwd()
print('os.getcwd() = ' + path)

# 実行しているスクリプトファイル（.py）があるディレクトリ
path = os.path.abspath(__file__)
print('os.path.abspath(__file__) = ' + path)