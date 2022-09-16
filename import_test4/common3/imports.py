
print(__file__[__file__[:__file__.rfind('\\')-1].rfind('\\'):])

import pathlib , sys
path = str(pathlib.Path(__file__).parent.parent)
print('### sys.path.append = ' + path)
sys.path.append(path)

# import common1
# from common1.common1_ import CommonClass,common_function
# ImportError: cannot import name 'CommonClass' from partially initialized module 'common1.common1' (most likely due to a circular import) (c:\Users\OK\source\repos\Repository4_python\import_test4\common1\common1.py)

# from common1.common1 import CommonClass,common_function
from common2.common1 import CommonClass,common_function