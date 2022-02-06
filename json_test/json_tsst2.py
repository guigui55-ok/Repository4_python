


def main():
    try:
        import json_util.logger_init
        logger = json_util.logger_init.initialize_logger()

        path = './test.json'
        
        import json_util.json_class
        cl_json = json_util.json_class.JsonUtil(path,logger)
        
        cl_json

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