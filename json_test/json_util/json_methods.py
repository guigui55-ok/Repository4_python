import json
from collections import OrderedDict
# pprintは結果を見やすくするためにインポートしている。JSONの処理自体には必要ない。
import pprint

def write_json(logger,data:dict,write_path:str = './values.json'):
    try:
        with open(write_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        logger.exp.error(e)
        return False

def read_json(logger,read_path:str)-> OrderedDict:
    try:        
        with open(read_path) as f:
            buf_dict:OrderedDict = json.load(f, object_pairs_hook=OrderedDict)
        return buf_dict
    except Exception as e:
        logger.exp.error(e)
        return []
