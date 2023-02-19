
import sys
import pathlib
path = pathlib.Path(__file__).parent.parent
if not str(path) in sys.path:
    sys.path.append(str(path))
    print('import={}'.format(path.name))
import import_all