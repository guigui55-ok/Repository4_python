#https://neko-py.com/python-dict-to-str
import json

def dict_str():
    dict_data = []
    # dict_data = {"key1": "data1",
    #             "key2": "data2",
    #             "key3": "data3"}
    # print(dict_data)
    # print(type(dict_data))

    # dict -> str
    # str_data = json.dumps(dict_data)

    # str
    str_data = '{"key4":"data4"}'
    str_data = """
{
    "key4":"data4"
}
    """
    str_data = '"key4":"data4"'
    print(str_data)
    print(type(str_data))

    # str -> dict
    re_conversion_data = json.loads(str_data)
    print(re_conversion_data)
    print(type(re_conversion_data))

def main():
    try:
        dict_str()
        return
    except:
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()