"""
外部pathからutilを使用する
"""
import sys,os
from pathlib import Path
# get parent path
package_name = 'common_util'
parent_parent_path = \
    str(Path('__file__').resolve().parent.parent)+'\\' + package_name
parent_parent_path = str(Path('__file__').resolve().parent.parent)
print('get_parent_parent_path : '+ parent_parent_path)
# import
import_path = os.path.join('..', package_name)
print('sys.path.append : '+ import_path)
print('sys.path.append : '+ parent_parent_path)
sys.path.append(parent_parent_path)
print('---------\nsys.path : ')
print(sys.path)
import common_util
import common_util.adb_util as adb_util
import adb_util.adb_common as adb_com

common = common_util