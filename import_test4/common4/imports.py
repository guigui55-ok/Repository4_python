
# print(__file__[__file__[:__file__.rfind('\\')-1].rfind('\\'):])

# import pathlib , sys
# path = str(pathlib.Path(__file__).parent.parent)
# print('### sys.path.append = ' + path)
# sys.path.append(path)

# # from common1.common1 import CommonClass,common_function
# from common2.common1 import CommonClass,common_function

import importlib

#mdl = importlib.import_module() #TypeError: import_module() missing 1 required positional argument: 'name'

# mdl = importlib.import_module('buf') #例外が発生しました: ModuleNotFoundError No module named 'buf'
# mdl = importlib.import_module('imports')

com4 = importlib.import_module('com4_1','main')
com4.main()
com4 = importlib.import_module('com4_1')
com4.main()