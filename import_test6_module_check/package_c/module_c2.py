print('module_c2')
# import module_c1
# import module_c2

# https://qiita.com/genchi-jin/items/b72d62ffef3091ee86e7

import sys
for mod in sys.modules:
    # print(mod)
    pass
# print(type(sys.modules))
for mod in sys.modules:
    if 'module_c1' == mod:
        print('match1')
        break
if not 'module_c1' in sys.modules:
    import module_c1
    # mod_name = 'module_c1'
    # import mod_name #ModuleNotFoundError: No module named 'mod_name'