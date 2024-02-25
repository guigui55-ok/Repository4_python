
from typing import Union

class DictUtil():
    def __init__(self, dict_value:dict={}) -> None:
        self.value = dict_value
        # 存在しないKeyのvalueを指定したとき取得する値
        # 使用する場合によっては[-（ハイフン）]やNoneを設定する。
        # デフォルトは空文字
        self.nothing_key_value = ''
        #
        self.print_err = True
    
    def _align_type_key(self, key:Union[str,list[str]]):
        """ 型をそろえる """
        if isinstance(key, str):
            return [key]
        elif isinstance(key, list):
            return key
        else:
            return key

    def get(self, key:Union[str,list[str]]):
        """ self.valueから値を取得する """
        return self.get_value(key)

    def get_value(self, key:Union[str,list[str]]):
        """ self.valueから値を取得する """
        keys = self._align_type_key(key)
        ret_d = {}
        for key in keys:
            ret = self.get_value_single(key)
            ret_d.update({key:ret})
        return ret_d

    def get_value_single(self, key:str):
        """ self.valueからKeyを1つだけ指定して、値を取得する """
        try:
            ret = self.value[key]
        except KeyError:
            if self.print_err:
                print('# KeyError[Key={}]'.format(key))
            ret = self.nothing_key_value
        return ret

    def update(self, *arg):
        """
        self.valueに値をセットする
        
         引数が1つの場合、
           型がdictの場合は、そのままupdateする
            型がそれ以外の場合は、{arg[0] : self.nothing_key_value} をupdateする
          引数が2つ以上なら、
           1つ目(arg[0])の型がdictの場合は、そのまま1つ目のみをupdateする
           それ以外の場合は
            1つ目をkey、2つ目をvalueとしたdict（={arg[0] : arg[1]}）をupdateする
        """
        d = self._get_dict_from_arg(arg)
        self.value.update(d)
    
    def _get_dict_from_arg(self, args):
        """
        *argを判定して、dictを取得する
         self.update 用
          引数が1つの場合、
           型がdictの場合は、そのまま dictを返す
            型がそれ以外の場合は、{arg[0] : self.nothing_key_value} を 返す
          引数が2つ以上なら、
           1つ目(arg[0])の型がdictの場合は、そのまま1つ目のみを 返す
           それ以外の場合は
            1つ目をkey、2つ目をvalueとしたdict（={arg[0] : arg[1]}）を 返す
        """
        try:
            if 0<len(args):
                if len(args)==1:
                    if isinstance(args[0], dict):
                        return args[0]
                    else:
                        # argsが1つのみでdict以外の場合はkey扱いとする
                        return {args[0]:self.nothing_key_value}
                else:
                    # 2 <= len(args)
                    # 値が2個以上でもdictの場合は1つ目のみを採用して、
                    # それ以降は無視をする
                    if isinstance(args[0], dict):
                        return args[0]
                    else:
                        # argsが2つ以上の場合でdict以外の場合は
                        # 1つ目をkey、2つ目をvalueとしたdictとして扱い
                        # それ以降は無視をする
                        return {args[0]:args[1]}
            else:
                return {}
        except Exception as e:
            raise e


def _test_a():
    print('# _test_a')
    print('## set_test')
    dict_obj = DictUtil()
    dict_obj.update({'aaa':111})
    dict_obj.update({'aaa':112}, {'bbb':222})
    dict_obj.update('ccc')
    dict_obj.update('ddd', 123)
    dict_obj.update('eee', 444, 'fff', 'abc')
    print(dict_obj.value)

    print('## get_test')
    key = 'aaa'
    dict_val = dict_obj.get_value(key)
    print(dict_val)
    key = 'zzz'
    dict_val = dict_obj.get_value(key)
    print(dict_val)
    dict_val = dict_obj.get_value(['aaa','eee'])
    print(dict_val)
    dict_val = dict_obj.get_value(['ddd','yyy'])
    print(dict_val)


def _test_b():
    from pathlib import Path
    path_c = Path(__file__).parent.joinpath('test_data/power_query_test_data.csv')
    path_str_c = str(path_c)

    from csv_dict import CsvDict
    csv_obj = CsvDict(None)
    csv_obj.encoding = 'utf-8-sig'
    csv_obj.csv_dict = csv_obj.read_file_as_dict_list(path_str_c)


    conf_key = 'ID'
    get_key = '名前'
    for val_dict in csv_obj.csv_dict:
        # print(val_dict)
        if val_dict[conf_key] == '41000':
            print(val_dict)
    
    from dict_list import DictList
    dict_list_obj = DictList(csv_obj.csv_dict)
    val_dict = dict_list_obj.get_dict_by_dict({'ID':'41000'})
    print(val_dict)

if __name__ == '__main__':
    print('*****')
    # _test_a()
    _test_b()