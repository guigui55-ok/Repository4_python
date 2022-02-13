import csv

def ex_proc(e:Exception):
    import traceback
    traceback.print_exc()
    # str(e)

class CsvDict():
    path:str

    def __init__(self,path:str) -> None:
        self.csv_dict:list[dict] = None
        self.set_path(path)

    def set_path(self,path:str):
        self.path = path
        import os
        if os.path.exists(path):
            self.csv_dict = self.read_file_as_dict_list(path)

    def read_file_as_dict_list(self,path:str='')->list[dict]:
        if path == '': path=self.path
        with open(path) as f:
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
        
    def write_file_for_dict_list(self,dict_keys:list, dict_list:list[dict], path:str=''):
        with open(path, 'w') as f:
            # Headerを書き込む
            writer = csv.DictWriter(f, dict_keys)
            writer.writeheader()
            # データを書き込む
            writer.writerows(dict_list)