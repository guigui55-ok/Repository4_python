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


3.
# BaseClass(コード改変をしたくないクラス) に ExtendClass(機能追加するクラス) 両方を加えた BaseClass_New を外部モジュールで作成する
# これをBaseClassインスタンス（オブジェクト）置き換えて使う
#  ＞＞既存クラスモジュールには影響なく、新たに NoChangeExtends_b クラスメソッドも組み込みやすい

さらにこれをas句で名前を置き換え連と、実装済みの既存コードには影響なし
from inherit_test3_3 import NoChangeMain_New as NoChangeMain
  ※共同作業をしている場合は、周知が必要
    以前のBaseClassのままだと思って、作業を進める可能性がある
"""

import os,pathlib

def test_path():
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

from common_control_app.common_control.common_control_factory import ModelName
def main():
  from base_package.base_module import BaseClass
  from common_control_app.common_control.common_control_factory import get_object,ExtendsBaseClass
  base = BaseClass('platform_test1','model_test1','ver1')
  base_ext = ExtendsBaseClass(base)
  obj = get_object(base_ext,ModelName.MODEL_BASE)
  print('===========')
  obj.excute_by_base_class()
  print('===========')
  obj.excute_by_common_methods()
  return

if __name__ == '__main__':
  main()