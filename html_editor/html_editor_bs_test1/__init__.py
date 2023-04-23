# import pathlib
# import sys
# path = str(pathlib.Path(__file__).parent.parent)
# sys.path.append(path)

import pathlib,sys
path = pathlib.Path(__file__)
target = 'html_editor'
while True:
    path = path.parent
    if path.name == target:
        if not str(path.parent) in sys.path:
            sys.path.append(str(path.parent))
            break
    if path.name == '': break