


from json_util.json_class import JsonUtil
path = './test.json'

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
    create_json()