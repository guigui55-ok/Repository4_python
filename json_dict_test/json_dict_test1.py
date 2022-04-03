"""
指定したKeyを読み込み 作成
JsonDictの値を更新
指定したKeyに書き込み
ファイルに書き込み

"""
from json_util.json_dict import JsonDict
from json_util.json_class import JsonUtil

path = './test2_2.json'
def read_key():
    dict_str = ''
    ju = JsonUtil(path)
    # print(ju.values)
    ### 文字列からjson_dictを用意するとき
    # dict_val = ju.cnv_str_to_dict(dict_str)
    # ju.values = dict_val
    jd = JsonDict(ju.values)
    # print(jd.get_json_str())
    target = ['']

def main():
    import plistlib as pl
    import abc
    print(abc)

if __name__ == '__main__':
    read_key()
    # main()