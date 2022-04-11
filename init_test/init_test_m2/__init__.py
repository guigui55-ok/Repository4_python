print('** __init__')
indent = '    '
print(indent + __file__)

import sys,os,pathlib

path = str(pathlib.Path(__file__).parent.parent)
sys.path.append(path)
print(indent + 'sys.path.append = ' + path)