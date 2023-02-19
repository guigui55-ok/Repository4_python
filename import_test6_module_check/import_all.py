
import sys
import pathlib
path = pathlib.Path(__file__).parent.joinpath('package_a')
if not str(path) in sys.path:
    sys.path.append(str(path))
    print('import={}'.format(path.name))

import package_a.module_a
import package_a.package_a_a.module_a_a
import package_b.module_b