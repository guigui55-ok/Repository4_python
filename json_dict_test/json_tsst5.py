


from cv2 import trace
from json_util.json_class import JsonUtil
path = './test4.json'
path2 = './test42.json'
import traceback

def dict_test():
    try:
        dict_str = '{"abc":"value-abc"}'
        dict_str = '{"key1": {"key2":"value-abc"} }'
        # dict_str = '{"kay1": {"key2":"value-abc"},{"key2":"value-abc"} }'#json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 31 (char 30)
        
        # dict_str = '{"kay1": {  {"key2":"value-abc"},{"key3":"value-abc"}  } }' #error
        dict_str = '{"key1": [  {"key2":"value-abc"}, {"key3":"value-abc"}  ] , "key1_2":"val_1_2"  ,"key3": {"key3":"value-abc"}  }' 
        dict_str2 = '{"key3": {"key3":"value-abc"} }'
        dict_str = """
    {
        "key1": [
            {"key2":"value-abc"},
            {"key3":"value-abc"}
            ],
        "key1_2":"val_1_2",
        "key3": {"key3":"value-abc"},
        "key4" : {
            "key41": [
                {"key42":"value-abc"},
                {"key43":"value-abc"}
            ],
            "key41_2":"val_1_2",
            "key43": {"key3":"value-abc"} 
        }
    }
        """
        # かぎ括弧でくくっている
        # dict_str = '[{"key3": {"key3":"value-abc"} }]'#TypeError: list indices must be integers or slices, not dict
        # ダブルクォーテーションがない
        # dict_str = '{"key3": value3, "key3":value4 }'#Exception: Json Format Is Invalid (Expecting value: line 1 column 10 (char 9))
        # ダブルクォーテーションがない
        # dict_str = '{"key3": value3, "key4":value4 }'
        dict_str = '{"key3": "value3", "key4":"value4" }'
        # dict_str = '{"key3": "value3", "key3":"value4" }'
        cl_json = JsonUtil(path2)
        cl_json.indent = 4
        
        dict_val = cl_json.cnv_str_to_dict(dict_str)
        cl_json.values = dict_val
        # cl_json.set_value_to_json('',dict_val)
        cl_json.write_json()
        print(dict_val)
        print(type(dict_val))


        print('----')
        print('len(dict_val) = {}'.format(len(dict_val)))
        for d in dict_val:
            print(d)
            print(dict_val[d])
            print(type(dict_val[d]))
        return
    except:
        traceback.print_exc()

def main():
    try:
        
        cl_json = JsonUtil(path)

        return
    except:
        import traceback
        traceback.print_exc()
        return

# main()

def create_json():
    try:
        data = get_test_dict()
        cl_json = JsonUtil(path)
        d = {'key2':'value33'}
        cl_json.add_value(d)
        print(cl_json.values)
        cl_json.write_json()
        print('path = ' + cl_json.path)
        return
    except:
        import traceback
        traceback.print_exc()

def get_test_dict():
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
        print('buf_dict3')
        print(buf_dict3)
        return buf_dict3
    except:
        import traceback
        print(traceback.print_exc())
        return {}

if __name__ == '__main__':
    # get_test_dict()
    # main()
    # create_json()
    dict_test()