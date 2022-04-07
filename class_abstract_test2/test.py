# import common_base_control_package.common_general.extends_base.extends_base_module
"""

android_base
model 1
    android_base
model 2
    android_2(android_base)


ExtendsBaseClass(abs)
  ExtendsBaseClass_B
CommonActionBase
CommonActionBase_A
それぞれバージョンを記載する
   コード上でバージョンを読み込む、ファイル内から　open(__file__)でreadする処理ををget_verメソッドとして、実装すればよい
   付加的な情報として出力しておく（、デバッグ時に、バージョンから原因特定を早めるため）
   
"""

import os


import os,pathlib

path = os.getcwd()
print('os.cwd = ' + path)

path = '.'
path = str(pathlib.Path(path).resolve)
print('.resolve = ' + path)
#.resolve = <bound method Path.resolve of WindowsPath('.')>

path = '.'
path = str(pathlib.Path(path).resolve())
print('.resolve = ' + path)

path = str(pathlib.Path('/test.py').resolve())
print('.resolve = ' + path)