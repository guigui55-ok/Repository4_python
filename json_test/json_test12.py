
import json
from collections import OrderedDict

def main():
    # 元の並びを保持したい場合は、引数object_pairs_hook=OrderedDictとする。
    path = 'test.json'
    # with open(path) as f:
    #     buf_dict:OrderedDict = json.load(
    #         f, object_pairs_hook=OrderedDict)
    with open(path) as f:
        buf_dict = json.load(f)
    print(buf_dict)
        
    data = open(path, "r")
    
    val = json.loads('{"a":123}')
    print(val)
    print(type(data))
    nyankoTextlist = []
    for d in data:
        print(d)
        val = json.loads(d)["text"]
        print(val)
        nyankoTextlist.append(val)
    
    # nyankoTextlist=[json.loads(tweet)["text"] for tweet in file_content]
    # print(buf_dict)
    # buf = [json.loads(tweet)["text"] for tweet in path]
    # print(buf)
    
    path = ''
    read_file_object = open("20220728-00.json", "r")
    for line in read_file_object:
        val = json.loads(d)




    # value : dict ={
    #     'key1': 'value1',
    #     'key2': 'value2',
    #     'key3': 'value3'
    # }
    import datetime
    dstr = datetime.datetime.now().strftime('%H%M%S')
    buf_dict.update({dstr:'value'})
    
    with open('./test.json', 'w') as f:
        json.dump(buf_dict, f, indent=4)
    return

if __name__ == '__main__':
    main()