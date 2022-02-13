#https://note.nkmk.me/python-json-load-dump/

import json
from collections import OrderedDict
# pprintは結果を見やすくするためにインポートしている。JSONの処理自体には必要ない。
import pprint





def main():
    try:
        path = './test.json'

        # buf_dict : dict ={
        #     'key1': 'value1',
        #     'key2': 'value2',
        #     'key3': 'value3'
        # }

        # read json
        # 元の並びを保持したい場合は、引数object_pairs_hook=OrderedDictとする。
        with open(path) as f:
            buf_dict:OrderedDict = json.load(f, object_pairs_hook=OrderedDict)
        
        # 存在しないkeyは追加される
        buf_dict['key4'] = 'value4'

        # 読み書きテスト用、値を変更して書き込む
        value = buf_dict['key3']
        # value3 は val3 に、それ以外 (val3) は value3 にする
        if value == 'value3': value = 'val3'
        else: value = 'value3'
        buf_dict['key3'] = value

        # write json
        with open(path, 'w') as f:
            json.dump(buf_dict, f, indent=4)
        print(path)

        return
    except:
        import traceback
        print(traceback.print_exc())
        return

# main()

def test_dict():
    try:
        # TypeError: 'key1' is an invalid keyword argument for print()
        #print(**buf_dict)
        # KeyError: 0
        #print(buf_dict[0])
        # OK value1
        # print(buf_dict['key1'])
        # OK v a l u e 1
        # print(*buf_dict['key1'])
        
        buf_dict1 : dict ={
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3'
        }

        buf_dict2 : dict ={
            'key1': 'value11',
            'key2': 'value22',
            'key3': 'value33'
        }

        buf_dict3 = {**buf_dict1,**buf_dict2}
        print(buf_dict3)
        return
    except:
        import traceback
        print(traceback.print_exc())
        return

test_dict()
main()