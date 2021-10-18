import sys

# 失敗パターン1
# 上位 directory の package は指定できない
#from package2.package3.package4.package5.module5 import func5
#例外が発生しました: ModuleNotFoundError       (note: full exception trace is shown but execution is paused at: <module>)
#No module named 'package2'

# from .package5 import module5
# 例外が発生しました: ImportError       (note: full exception trace is shown but execution is paused at: <module>)
# attempted relative import with no known parent package

# from . import package5
# 例外が発生しました: ImportError   attempted relative import with no known parent package

# OK
import package5
# OK
from package5 import module5

# NG
# 下位 directory は import できない
# from package1.module1 import func1 

# 引数の場所を path に追加する
sys.path.append(r'C:\Users\OK\source\repos\Repository4_python\import_test2\package1')

# sys.path.append(r'C:\Users\OK\source\repos\Repository4_python\import_test2\package1\package2')
# https://office54.net/python/python-unicode-error
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

# 現在通っている path を表示する
print(sys.path)

# 上記 path 追加後だと以下 package が import できる
from package2 import module2

# ModuleNotFoundError No module named 'package2'　# path を通していないとエラーとなる
# from package3 import module3
#  ModuleNotFoundError No module named 'package3'

# OK
from package2.package3 import module3 

# NG
# path を通していない場所からだとエラーとなる
# from package3.package4 import module4 

# NG
# # import 先で module3 を import していると、import 先で実行時にエラーとなる
# from package2.package3.package4 import module4  

# OK
# root Package から辿っていけば、エラーが発生しない
from package2.package3.package4 import module4_3 

# OK
# root Package から辿っていけば、エラーが発生しない
from package2.package3.package4.package5 import module5 
module5.func5()

# NG
# 下位 directory は import できない
# from ..module3 import func3
# func3()
# 例外が発生しました: ImportError
# attempted relative import with no known parent package

# NG
# 下位 directory は import できない
# from package1.pacage2 import func2
#func2()
# 例外が発生しました: ModuleNotFoundError       (note: full exception trace is shown but execution is paused at: <module>)
# No module named 'package1'

# NG
# 下位 directory は import できない
# from package1.module1 import func1
# func1()
# 例外が発生しました: ModuleNotFoundError       (note: full exception trace is shown but execution is paused at: <module>)
# No module named 'package1'
# ModuleNotFoundError No module named

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
print('__name__ is', __name__)

from module1 import func1
func1()

# NG
# 上位 directory は import できない
# from package1.package2 import func2
# from package2 import func2
# 例外が発生しました: ImportError
# cannot import name 'func2' from 'package2' 

# NG
# 上位 directory は import できない
# from ..module3 import func3
# 例外が発生しました: ImportError
# attempted relative import with no known parent package

# NG
# 間違った記述
# from .package5.module5 import func5
# func5()

# NG
# 間違った記述　- module を飛び越えて指定はできない
# from package5 import func5 
# 例外が発生しました: ImportError       (note: full exception trace is shown but execution is paused at: <module>)
# cannot import name 'func5' from 'package5' (c:\Users\OK\source\repos\Repository4_pytho
# func5()

# OK
from package5.module5 import func5

# NG
# 間違った記述　- 存在しない package
# from . import package5
# 例外が発生しました: ImportError       (note: full exception trace is shown but execution is paused at: <module>)
# attempted relative import with no known parent package

# NG
# 間違った記述　- 存在しない package
# from . import package3
# 例外が発生しました: ImportError  cannot import name 'package3' from 'package2.package3.package4' 

# NG
# 上位 directory は import できない
# from ... import package3
# 例外が発生しました: ImportError   attempted relative import with no known parent package