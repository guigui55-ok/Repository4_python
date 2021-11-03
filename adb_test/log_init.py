"""
外部pathからlogging_utilを使用する
"""
import sys,os
from pathlib import Path

# get parent path
package_name = 'logging_util'
parent_parent_path = \
    str(Path('__file__').resolve().parent.parent)+'\\' + 'common_util'
print('get_parent_parent_path : '+ parent_parent_path)
# import
import_path = os.path.join('..', 'common_util/' + package_name)
import_pat = '../common_util\\' + package_name
print('sys.path.append : '+ parent_parent_path)
sys.path.append(parent_parent_path)
print('sys.path.append : '+ import_path)
sys.path.append(import_path)
# print('sys.path.append : '+ parent_parent_path)
# sys.path.append(parent_parent_path)
print('----------\nsys.path:')
print(sys.path)
# import_path = str(Path('__file__').resolve().parent.parent)+'\\logger_util'
# print('import_path:'+import_path)
# import_path = os.path.join('..', 'logger_util')
# print('import_path:'+import_path)
# sys.path.append(import_path)
import log_util
import log_util.logger_init as logger_init
import log_util.logging_util as logging_util


def initialize_logger_new() -> log_util.logging_util.logger_util:
    return logger_init.initialize_logger()

    return logging_util.logger_init.initialize_logger()
