import csv

def ex_proc(e:Exception):
    import traceback
    traceback.print_exc()
    # str(e)

import os

class CsvDict():
    path:str

    def __init__(self,path:str) -> None:
        self.csv_dict:'list[dict]' = None
        self.path = ''
        self.encoding = 'utf-8'
        self.set_path_and_read_csv(path)

    def set_path(self,path:str):
        """
        self.pathをセットする
         引数pathがNone or 空文字なら self.pathはそのままとする。
          戻り値はself.pathを返す
        """
        if path==None or path=='':
            return self.path
        self.path = str(path)
        return self.path

    def set_path_and_read_csv(self, path:str):
        path = self.set_path(path)
        if os.path.exists(path):
            self.csv_dict = self.read_file_as_dict_list(path)

    def read_file_as_dict_list(self,path:str='')->'list[dict]':
        path = self.set_path(path)
        with open(path, encoding=self.encoding) as f:
            reader = csv.DictReader(f)
            l = [row for row in reader]
        return l
        """
        デフォルトでは一行目の値がフィールド名として使われ、辞書のキーとなる。
                with open(path) as f:
                    reader = csv.DictReader(f)
                    l = [row for row in reader]
        pprint.pprint(l)
        # [OrderedDict([('a', '11'), ('b', '12'), ('c', '13'), ('d', '14')]),
        #  OrderedDict([('a', '21'), ('b', '22'), ('c', '23'), ('d', '24')]),
        #  OrderedDict([('a', '31'), ('b', '32'), ('c', '33'), ('d', '34')])]
        """
    
    def write_self_data_to_file(self):
        keys = self.csv_dict[0].keys()
        self.write_file_for_dict_list(keys,self.csv_dict,self.path)
        
    def write_file_for_dict_list(
            self,dict_keys:list,
            dict_list:list[dict],
            path:str=''):
        with open(path, 'w', encoding=self.encoding) as f:
            # Headerを書き込む
            writer = csv.DictWriter(f, dict_keys)
            writer.writeheader()
            # データを書き込む
            writer.writerows(dict_list)

    def write_file_by_list_2d(self, write_list_2d:'list[list]'):
        with open(self.path, 'w', newline='', encoding=self.encoding) as f:
            writer = csv.writer(f)
            # for row_data in buf_list_2d:
            #     writer.writerow(row_data)
            writer.writerows(write_list_2d)
    
    def read_file_as_list_2d(self):
        """
        csvファイルを2次元のリストとして取得する（dictではない）
         （メンバ変数には格納しない）
        """
        ret_list = []
        with open(self.path, encoding=self.encoding) as f:
            reader = csv.reader(f)
            for row in reader:
                ret_list.append(row)
        return ret_list