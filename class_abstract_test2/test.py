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

いったん、ソースは、platform_control_methodに作成するが
行数が増えて、分けるときはどうする

　methodはそのまま、新たに作成

1.TestClass を委譲したor継承したクラスを作成、既存クラスのメソッドをオーバーライド
　　新しい、TestClass＞NewTestClass　→　既存のクラス・モジュールには影響がないが、既存コードに影響がある
  def hogehoge(test_obj:TestClass)

　この場合型が違っても動く test_obj に NewTestClassが入っていてもよいが、作法的にはNG

2.test_class.pyを改変
　共用部を改変する、既存コードには影響がない




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