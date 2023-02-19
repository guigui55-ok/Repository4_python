print('module_c1')
# import module_c2

import sys
for mod in sys.modules:
    if 'module_c2' == mod:
        print('match2')
        break
    else:
        # print('    ' + mod)
        pass
if not 'module_c2' in sys.modules:
    import module_c2

if __name__ == '__main__':
    pass