

import json
from collections import OrderedDict
# pprintは結果を見やすくするためにインポートしている。JSONの処理自体には必要ない。
import pprint
import os

class JsonUtil():

    def __init__(self,path) -> None:
        self.path:str = path
        self.values : OrderedDict = None
        self.defalut_file_path:str = './values.json'
        self.indent:int = 4
        if os.path.exists(path):
            self.read_json(path)
    
    def cnv_str_to_dict(self,value:str)->dict:
        ret = json.loads(value)
        return ret

    def read_json(self,read_path:str=''):
        if read_path == '': read_path = self.path
        # read
        with open(read_path) as f:
            buf_dict:OrderedDict = json.load(f, object_pairs_hook=OrderedDict)
        self.values = buf_dict

    def write_json(self,values=None,write_path:str = ''):
        if write_path == '' : write_path = self.path
        if write_path == '': write_path = self.defalut_file_path
        if values == None : values = self.values
        # write
        with open(write_path, 'w') as f:
            json.dump(values, f, indent=self.indent)

    def get_value_from_json(self,path,keys:list)->list[str]:
        self.read_json(path)
        ret_list = []
        for key in keys:
            ret_list.append(self.values[key])
        return ret_list

    def add_value(self,value:dict):
        val = {**self.values,**value}
        self.values = val
    
    def update_value(self,value:dict):
        self.values.update(value)

    def set_value_to_json(self,path,values:dict)->bool:
        # 同じ key は上書きされる、引数 values の値を優先する
        write_val = {**self.values,**values}
        return self.write_json(write_val,path)
        
        