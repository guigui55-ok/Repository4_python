import sys

# from package1.module1 import func1 
sys.path.append(r'C:\Users\OK\source\repos\Repository4_python\import_test2\package1')
# sys.path.append(r'C:\Users\OK\source\repos\Repository4_python\import_test2\package1\package2')
# https://office54.net/python/python-unicode-error
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
print(sys.path)

# from ..module3 import func3
# func3()
# 例外が発生しました: ImportError
# attempted relative import with no known parent package

# from package1.pacage2 import func2
#func2()
# 例外が発生しました: ModuleNotFoundError       (note: full exception trace is shown but execution is paused at: <module>)
# No module named 'package1'

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

# from package1.package2 import func2
# from package2 import func2
# 例外が発生しました: ImportError
# cannot import name 'func2' from 'package2' 

# from ..module3 import func3
# 例外が発生しました: ImportError
# attempted relative import with no known parent package

# from .package5.module5 import func5
# func5()
