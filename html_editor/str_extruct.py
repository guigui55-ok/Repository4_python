

class SearchValue():
    def __init__(self,value:str) -> None:
        self.value = value
        self.pos = 0

import copy

class SearchValues():
    """
    文字列を検索して結果を保存する
    """
    def __init__(self,left:str, right:str) -> None:
        self.left = SearchValue(left)
        self.right = SearchValue(right)
        self.start_pos = 0
        self.pos = 0
        self.next_pos = 0
        self._is_match = False
        self.is_save_target = False
        self.target = ''
        self.result = ''
    def find_next(self, target:str, start_pos:int):
        self.start_pos = start_pos
        pos = target.find(self.left.value, start_pos)
        self.pos = pos
        self.left.pos = int(pos) + len(self.left.value)
        if self.left.pos<0:
            self.right.pos=-1
            return 0
        pos = self.left.pos + len(self.left.value) 
        pos = target.find(self.right.value, pos)
        self.right.pos = int(pos)
        ###
        # ret = target[self.left.pos : self.right.pos]
        ###
        next_pos = self.right.pos + len(self.right.value) 
        self.next_pos = next_pos
        if self.is_save_target:
            self.target = target
        return next_pos
    def excute_function(self, func, argument):
        self.result = func(argument)

    @property
    def is_match(self):
        if self.pos<0:
            self._is_match = False
        else:
            self._is_match = True
        return self._is_match



class StrExtructor():
    def __init__(self, path:str='') -> None:
        self.path = path
        self.pos = 0
        self.results = []
        self.method = cut_str
        self.left = ''
        self.right = ''
        
    def read_data_from_path(self,path:str=''):
        if path=='': path=self.path
        with open(self.path, 'r', encoding='utf-8')as f:
            buf = f.read()
        self.read_data = buf

    def set_value(self, left:str, right:str):
        self.search_value = SearchValues(left,right)
        self.left = left
        self.right = right

    def excute(self):
        self.search_value = SearchValues(self.left,self.right)
        self.pos = self.search_value.find_next(self.read_data, self.pos)
        if self.search_value.is_match:
            self.results.append(self.search_value)
    
    def excute_all(self, left:str='', right:str='', path:str=''):
        if path=='': path=self.path
        self.read_data_from_path(path)
        if left=='': left=self.search_value.left.value
        if right=='': right=self.search_value.right.value
        self.set_value(left,right)
        while True:
            self.excute()
            if not self.search_value.is_match: break
            # self.print_last_result()
        ret:SearchValues
        ###
        for i in range(len(self.results)):
            ret = self.results[i]
            self.results[i] = self.method(self.read_data, ret)
            # print('    {} ,ret = {}'.format(i, self.results[i].result))

    def get_results_as_list(self):
        ret_list = []
        for i in range(len(self.results)):
            ret = self.results[i]
            ret_list.append(ret.result)
        return ret_list
            

    def get_last_result(self):
        if len(self.results)<1:
            print('len(self.results)<1')
            return None
        ret:SearchValues = self.results[-1]
        return ret

    def print_last_result(self):
        ret = self.get_last_result()
        if ret==None: return
        i = len(self.results)
        print('    {} ,pos = {}, {}'.format(i, ret.left.pos, ret.right.pos))
    def print_last_result_ret(self):
        ret = self.get_last_result()
        if ret==None: return
        i = len(self.results)
        print('    {} ,ret = {}'.format(i, ret.result))


def cut_str(value:str, seach_value:SearchValues):
    left_pos = seach_value.left.pos
    right_pos = seach_value.right.pos
    if left_pos < 0 or right_pos < 0: return seach_value
    if left_pos > right_pos: return seach_value
    seach_value.result = value[left_pos : right_pos]
    return seach_value

def cut_str2(value:str, seach_value:SearchValues):
    left_pos = seach_value.left.pos
    right_pos = seach_value.right.pos
    if left_pos < 0 or right_pos < 0: return seach_value
    if left_pos > right_pos: return seach_value
    ret = value[left_pos : right_pos]
    ###
    rets = ret.split(' ')
    ret = rets[0]
    ###
    seach_value.result = ret
    return seach_value


class ListValueCounter():
    def __init__(self) -> None:
        self.values:dict = dict()
        self.index = 0
    def count_up(self, value:str):
        if value in self.values.keys():
            val = int(self.values[value])
            self.values[value] = val+1
        else:
            self.values.update( {value:1} )
    def get_values(self,index:int=-1):
        if index<0: index=self.index
        k = self.get_keys_list()[index]
        return k, self.values[k]
    def get_keys_count(self):
        return len(self.values.keys())
    def get_keys_list(self):
        return [k for k in self.values.keys()]

    def count_list(self,target:'list[str]'):
        """
        count main
        """
        counter = self
        for l in target:
            counter.count_up(l)

    def print_count_list(self,target:'list[str]'):
        for l in target:
            self.count_up(l)
        self.print_list()
    def print_list(self):
        keys = self.get_keys_list()
        for i in range(len(keys)):
            k = keys[i]
            v = self.values[k]
            print('   {} , k,v = {}, {}'.format(i, k, v))
    

def test_main():
    import pathlib
    dir_path = str(pathlib.Path(__file__).parent.joinpath('html_test'))
    file_name='ダウンロード.htm'
    # file_name = 'test_writer.html'
    path = pathlib.Path(dir_path).joinpath(file_name)
    cl = StrExtructor(path)
    cl.method = cut_str2
    cl.set_value('<','>')
    cl.excute_all()
    ret_list = cl.get_results_as_list()
    ListValueCounter().print_count_list(ret_list)
    return

if __name__ == '__main__':
    test_main()


