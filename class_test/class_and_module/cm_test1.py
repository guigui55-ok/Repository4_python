

from cls1 import Cls1,Cls2
from cls1 import Cls2_2 as Cls2
import copy
from pack import mod1

# モジュールはコピーができない、単一のオブジェクト（Singleton的）
# 引数としては渡すことは可能
# オーバーライド不可、継承不可
# classmethodはコピーはできるが、参照元がすべて同じ
# オーバーライドは可能（継承可能）
# classは参照元が別のコピーが作成可

def main1():
    # クラスのオブジェクト自体が持つ変数の参照IDについて
    cls2 = copy.copy(Cls2)
    Cls2.print_value()
    cls2.print_value()
    #
    cls2.value = 'cls2_change'
    Cls2.print_value()
    cls2.print_value() #同じIDを参照している

def main2():
    # モジュールの変数について
    # obj = copy.copy(mod1)
    # 例外が発生しました: TypeError
    # cannot pickle 'module' object
    mod1.print_value()
    # obj.print_value()
    #
    mod1.value = 'change'
    # obj.value = 'change'
    mod1.print_value()
    # obj.print_value() #同じIDを参照している

def main3(mod1:mod1):
    # モジュールの変数について
    # obj = copy.copy(mod1)
    # 例外が発生しました: TypeError
    # cannot pickle 'module' object
    mod1.print_value()
    # obj.print_value()
    #
    mod1.value = 'change'
    # obj.value = 'change'
    mod1.print_value()
    # obj.print_value() #同じIDを参照している

if __name__ == '__main__':
    main1()
    # main2()
    # main3(mod1)