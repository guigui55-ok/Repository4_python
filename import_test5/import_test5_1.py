#https://qiita.com/genchi-jin/items/b72d62ffef3091ee86e7


import sys
import subprocess

if "subprocess" in sys.modules:
    print("module already imported")
else:
    print("module not imported")

    
import import_sample5_1
module_name = 'import_sample5_1'
if module_name in sys.modules:
    print(f"module already imported , module_name = {module_name}")
else:
    print(f"module not imported , module_name = {module_name}")


import import_test5_1_sub
module_name = 'import_sample_5_1_1'
if module_name in sys.modules:
    print(f"module already imported , module_name = {module_name}")
else:
    print(f"module not imported , module_name = {module_name}")


# {'sys': <module 'sys' (built-in)>, 
# 'builtins': <module 'builtins' (built-in)>, 
# '_frozen_importlib': <module '_frozen_importlib' (frozen)>, ...
count = str(sys.modules).count(module_name)
print(f'count = {count}')

print()
print(str(sys.modules))
print()

# print()
# print('*****')
# module_name = 'sample'
# for buf in sys.modules:
#     print(buf)
#     # if module_name in buf:
#     #     print(buf)

