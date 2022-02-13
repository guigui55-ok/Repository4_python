import csv
import pprint

from csv_dict import CsvDict
from dict_list import DictList

def test_csv_dict_write_val():
    try:
        import test_com
        path = test_com.get_path()

        import csv_dict
        csv_d = CsvDict(path)

        # print('csv_d.csv_dict')
        # print(csv_d.csv_dict)

        import dict_list
        dic_list = DictList(csv_d.csv_dict)

        print('---------------')
        print('dic_list.value')
        print(dic_list.value)
        cond = {'b':12}
        key = 'a'
        val = dic_list.get_value_by_dict(key,cond)
        print('key = {} , val = {}'.format(key,val))
        # set value
        val = str(int(val)+1)

        w_data = {key:val}
        dic_list.update_dict_by_dict(w_data,cond)
        print('---------------')
        print('dic_list.value')
        print(dic_list.value)

        csv_d.csv_dict = dic_list.value
        csv_d.write_self_data_to_file()

        print('path = ' + path)
        return
    except:
        import traceback
        traceback.print_exc()



def get_path()->str:
    import pathlib,os
    file_name = 'test.csv'
    sub_dir = 'test_data'
    path = os.path.join(pathlib.Path(__file__).parent,sub_dir,file_name)
    return path

def main():
    test_csv_dict_write_val()

if __name__ == '__main__':
    main()