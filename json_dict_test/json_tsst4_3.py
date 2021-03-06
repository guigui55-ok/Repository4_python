


from json_util.dict_list2 import DictListType
from json_util.json_class import JsonUtil
from json_util.json_dict import JsonDict
path = './test.json'
path3 = './test4_3.json'
import traceback

def dict_test():
    try:
        ##################
        ## dict をJsonDictに代入して、表示する（ファイルからではない）

        ##################
        cl_json = JsonUtil(path3)
        dict_val = cl_json.values
        # print('----')
        # print(dict_val)
        # print(type(dict_val))
        jd = JsonDict(cl_json.values)
        ##################
        update_dict = {'key1':['key1_2_b','key1_3_b']}
        update_dict = {'key2':'value2_b'}
        update_dict = {'key3':{"key31":"value-abc31"}}
        update_dict = {'key3':{"key31":"value-abc31"}}
        update_dict = {"key4":[{"key41_2":"value-abc41_2"},{"key41_3":"value-abc41_3"}]}
        temp_jd = JsonDict(update_dict)
        print('**********')
        temp_jd.print_values()
        print('**********')
        ##################
        key = 'key1'
        jd_els = jd.get_value_dictlist(key,DictListType.KEY.value)
        #ゼロ[]で上書きされている
        jd_el:JsonDict=None
        print('key='+key)
        for jd_el in jd_els:
            jd_el.print_values()

        ##################
        ##################
        json_str = jd.get_json_str()
        print('----')
        print(json_str)

        path4 = './test4_4.json'
        cl_json.path = path4
        cl_json.write_json()
        
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
        return
    except:
        import traceback
        print(traceback.print_exc())
        return {}

if __name__ == '__main__':
    # get_test_dict()
    # main()
    # create_json()
    dict_test()