# import pathlib
# import sys
# path = str(pathlib.Path(__file__).parent.parent)
# sys.path.append(path)

from pathlib import Path
import sys
path = Path(__file__)
target = 'html_editor'
target_b = 'Repository4_python'
is_appended = False
# print('DEBUG')
# print(__file__)
while True:
    path = path.parent
    # print('*{}'.format(path.name))
    if str(path.name) == target:
        is_appended = True
        sys.path.append(str(path.parent))
        if not str(path.parent) in sys.path:
            pass
        break
    if str(path.name) == target_b:
        is_appended = True
        sys.path.append(str(path.joinpath(target)))
        if not str(path.joinpath(target)) in sys.path:
            pass
        break
    if path.name == '':
        if not is_appended:
            print('find path({})'.format(__file__))
            print('html_editor is Nothing')
        break