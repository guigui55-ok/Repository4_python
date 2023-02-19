import pathlib
import sys
path = pathlib.Path(__file__)
target = 'import_test6_module_check'
while True:
    path = path.parent
    if path.name == target:
        if not str(path) in sys.path:
            sys.path.append(str(path))
            print('import={}'.format(path.name))
        break
if path.name == '':
    raise ModuleNotFoundError(__file__)
import import_all