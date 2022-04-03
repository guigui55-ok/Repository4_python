# import common_base_control_package.common_general.extends_base.extends_base_module


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