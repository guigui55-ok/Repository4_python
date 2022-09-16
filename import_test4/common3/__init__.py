print(__file__)
pos = __file__.rfind('\\')-1
print(pos)
pos = __file__[:pos].rfind('\\')
print(pos)
print(__file__[pos:])

print(__file__[__file__[:__file__.rfind('\\')-1].rfind('\\'):])


import pathlib , sys
path = str(pathlib.Path(__file__).parent.parent)
print('### sys.path.append = ' + path)
sys.path.append(path)

NUMBER = '1-2'
NUMBER = '1-2-3'

# import common1
from common1.common1 import CommonClass,common_function