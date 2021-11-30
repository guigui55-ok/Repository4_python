

from os import read
from typing import OrderedDict
import json
from collections import OrderedDict
# pprintは結果を見やすくするためにインポートしている。JSONの処理自体には必要ない。
import pprint
import json_methods
import logger_init

class JsonUtil():
    logger = None
    path : str = ''
    values : OrderedDict
    defalut_file_path = './values.json'

    def __init__(self,path,logger) -> None:
        try:
            self.logger = logger
            self.path = path
        except Exception as e:
            self.logger.exp.error(e)

    def get_logger(self)->logger:
        return logger_init.initialize_logger()

    def read_json(self,read_path:str='')-> bool:
        try:
            if read_path == '': read_path = self.path
            self.values = json_methods.read_json(self.logger,read_path)
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def write_json(self,values=None,write_path:str = '')->bool:
        try:
            if write_path == '' : write_path = self.path
            if write_path == '': write_path = self.defalut_file_path
            if values == None : values = self.values
            return json_methods.write_json(self.logger,values,self.path)
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def get_value_from_json(self,path,keys:list)->list(str):
        try:
            self.read_json(path)
            ret_list = []
            for key in keys:
                ret_list.append(self.values[key])
            return ret_list
        except Exception as e:
            self.logger.exp.error(e)
            return []

    def set_value_to_json(self,path,values:dict)->bool:
        try:
            # 同じ key は上書きされる、引数 values の値を優先する
            write_val = {**self.values,**values}
            return self.write_json(write_val,path)
        except Exception as e:
            self.logger.exp.error(e)
            return False
        
        