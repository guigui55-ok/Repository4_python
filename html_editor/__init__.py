

import pathlib,sys
path = pathlib.Path(__file__)
target = 'html_editor'
target_b = 'Repository4_python'
while True:
    path = path.parent
    if path.name == target:
        if not str(path.parent) in sys.path:
            sys.path.append(str(path.parent))
            break
    if path.name == target_b:
        if not str(path.joinpath(target)) in sys.path:
            sys.path.append(str(path.joinpath(target)))
            break
    if path.name == '':
        print('find path({})'.format(__file__))
        print('html_editor is Nothing')
        break