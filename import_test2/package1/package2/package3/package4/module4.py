# from package1.pacage2.module2 import func2
# from ...module2 import func2
# 例外が発生しました: ModuleNotFoundError       (note: full exception trace is shown but execution is paused at: <module>)
# No module named 'package1'

# from package1.pacage2.pacage3.module3 import func3
# from ..module3 import func3
# from .. import module3
# 
# 例外が発生しました: ImportError       (note: full exception trace is shown but execution is paused at: <module>)
# attempted relative import with no known parent package

import sys 
sys.path.append(r'C:\Users\OK\source\repos\Repository4_python\import_test2\package1\pacage2\pacage3')
# https://office54.net/python/python-unicode-error
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
print(sys.path)
import module3
from module3 import func3
func3()
# pacakge1.package2.module2.func2()
