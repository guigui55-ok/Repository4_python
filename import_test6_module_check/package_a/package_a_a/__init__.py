print('pacakge_a_a')

import sys
import pathlib
path = pathlib.Path(__file__).parent.parent
if not str(path) in sys.path:
    sys.path.append(str(path))
    print('import={}'.format(path.name))
import sys_path_append_base


# import pathlib
# import sys
# path = pathlib.Path(__file__)
# target = 'import_test6_module_check'
# while True:
#     path = path.parent
#     if path.name == target:
#         if not str(path) in sys.path:
#             sys.path.append(str(path))
#             break
# import import_all