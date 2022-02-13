import json
from collections import OrderedDict
# pprintは結果を見やすくするためにインポートしている。JSONの処理自体には必要ない。
import pprint

def write_json(data:dict,write_path:str = './values.json'):
    with open(write_path, 'w') as f:
        json.dump(data, f, indent=4)

def read_json(read_path:str)-> OrderedDict:
    with open(read_path) as f:
        buf_dict:OrderedDict = json.load(f, object_pairs_hook=OrderedDict)
    return buf_dict