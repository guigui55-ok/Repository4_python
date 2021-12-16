"""
外部pathから log_util を使用する
"""

import os,pathlib,sys
image_path = os.getcwd()
path = str(pathlib.Path(__file__).resolve().parent.parent)
path = os.path.join(path,'common_util','log_util')
sys.path.append(path)
print('sys.path.append')
print(path)

import common_util.log_util.logging_util as logging_util 
from common_util.log_util.logger_init import initialize_logger
