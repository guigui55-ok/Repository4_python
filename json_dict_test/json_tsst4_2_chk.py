


from json_util.json_class import JsonUtil
path = './test.json'
path2 = './test2.json'
import traceback

def dict_test():
    try:
        dict_str = '{"abc":"value-abc"}'
        dict_str = '{"key1": {"key2":"value-abc"} }'
        # dict_str = '{"kay1": {"key2":"value-abc"},{"key2":"value-abc"} }'#json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 31 (char 30)
        
        # dict_str = '{"kay1": {  {"key2":"value-abc"},{"key3":"value-abc"}  } }' #error
        dict_str = '{"key1": [  {"key2":"value-abc"}, {"key3":"value-abc"}  ] , "key1_2":"val_1_2"  ,"key3": {"key3":"value-abc"}  }' 
        # dict_str = '{"key1": [  {"key2":"value-abc"}, {"key3":"value-abc"}  ] , {"key1_2":"val_1_2"}  ,"key3": {"key3":"value-abc"}  }'#NG 
        # //
        # dict_str = '{"key11":"key111":"value111"}'#NG 
        # //- Exception: Json Format Is Invalid (Expecting ',' delimiter: line 1 column 18 (char 17))
        dict_str = '{"key1": [  {"key2":"value-abc"}, {"key3":"value-abc"}  ] , "key1_2":"val_1_2"}' #OK
        dict_str = '{"key1": {"key2":"value-abc"}, "key1_2":"val_1_2"}' #OK
        #dict_str = '{"key1": {"key2":"value-abc"}, {"key1_2":"val_1_2"} }' #NG
        #dict_str = '{"key1":["key1_2":"value-abc1_2","key1_3":"value-abc1_3"] }'#NG
        #Exception: Json Format Is Invalid (Expecting ',' delimiter: line 1 column 18 (char 17))
        # /\ Exception: Json Format Is Invalid (Expecting property name enclosed in double quotes: line 1 column 32 (char 31))  
        dict_str2 = '{"key3": {"key3":"value-abc"} }'

        dict_str = '{"key1": [  {"key2":"value-abc"}, {"key3":"value-abc"}  ] , "key1_2":"val_1_2"}' #OK
        dict_str = '{"key4": {"key41": [{"key41_2": "value-abc41_2"},{"key41_3": "value-abc41_3"}],"key42": "va42","key43":{"key43_1": "value-abc43_3"} }' #NG
        dict_str = '{ "key4": {"key41": [{"key41_2": "value-abc41_2"},{"key41_3": "value-abc41_3"}],"key42":"va42","key43":{"key43_1":"value-abc43_3"}  } }' #OK
        dict_str = '{ "key4": {"key41": [{"key41_2": "value-abc41_2"},{"key41_3": "value-abc41_3"}],{"key42":"va42"},"key43":{"key43_1":"value-abc43_3"}  } }' #NG
        dict_str = """
{
    "key1":[
        {"key1_2":"value-abc1_2"},
        {"key1_3":"value-abc1_3"}
    ],
    "key2":"val_2",
    "key3":{
        "key31":"value-abc31"
    },
    "key4":{
        "key41":[
            {"key41_2":"value-abc41_2"},
            {"key41_3":"value-abc41_3"}
        ],
        "key42":"va42",
        "key43":{
            "key43_1":"value-abc43_1"
        }
    }
} 
"""
        print('#####')
        num = 214
        print(dict_str[num-4:num+4])
        #Exception: Json Format Is Invalid (Expecting property name enclosed in double quotes: line 1 column 81 (char 80))  
        # dict_str = '"{ key4": {"key41":"VALUE41","key42":"va42","key43":"Value43"  }' #NG
        #/\Exception: Json Format Is Invalid (Expecting ',' delimiter: line 1 column 134 (char 133))

        cl_json = JsonUtil(path2)
        cl_json.indent = 4
        dict_val = cl_json.cnv_str_to_dict(dict_str)
        cl_json.values = dict_val
        # cl_json.set_value_to_json('',dict_val)
        cl_json.write_json()
        print('----')
        print(dict_val)
        print(type(dict_val))

# key : {key : value}

        print('----')
        for d in dict_val:
            print('key={} , value2={} , type={}'.format(d, dict_val[d], type(dict_val[d])))
            # print(d)
            # print(dict_val[d])
            # print(type(dict_val[d]))
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