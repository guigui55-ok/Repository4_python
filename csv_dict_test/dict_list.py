

class DictList():
    value:list[dict]
    def __init__(self,dict_list:dict,is_no_check_type:bool=False) -> None:
        values : list = []
        if not is_no_check_type:
            if isinstance(dict_list, list):
                for val in dict_list:
                    if isinstance(val, dict):
                        values.append(val)
                    else:
                        raise Exception(dict_list.value is not dict)
            else:
                raise Exception('dict_list is not list')
            self.value = values
        else:
            self.value = dict_list
    
    def rows_count(self):
        cnt = len(self.value[0].keys())
        return cnt
    def cols_count(self):
        cnt = len(self.value)
        return cnt
    
    def is_dict_list(self,dict_list)->bool:
        if isinstance(dict_list, list):
            for val in dict_list:
                if isinstance(val, dict):
                    # pass when True. continue for check all value
                    pass
                else:
                    return False
        else:
            return False
        return True
    
    def _raise_error_if_invalid_value(self, value):
        if isinstance(value,dict):
             return value
        else:
            raise TypeError(value)
    
    def update_dict_by_dict(self,update_dict:dict,condition_dict:dict):
        """only first comp(match)"""
        _condition_dict = self._raise_error_if_invalid_value(
            condition_dict)
        
        for i in range(len(self.value)):
            dict_value = self.value[i]
            if self.comp_dict_in_dict(dict_value,_condition_dict):
                self.value[i].update(update_dict)

    def get_value_by_dict(self, key:str, condition_dict:dict):
        """
        condition_dict と一致するとき、そのindexのdictのkeyを取得する

        only first comp(match)
        """
        dict_value = self.get_dict_by_dict(condition_dict)
        return dict_value[key]

    def get_dict_by_dict(self, condition_dict:dict):
        """
        condition_dict と一致するとき、そのindexのdictを取得する

        only first comp(match)
        """
        _condition_dict = self._raise_error_if_invalid_value(
            condition_dict)
        
        for dict_value in self.value:
            if self.comp_dict_in_dict(dict_value,_condition_dict):
                return dict_value
    
    def comp_dict_in_dict(self,target_dict:dict,condition_dict:dict):
        """
        dictがcondition_dictとすべて合致する(含まれる)か判定する
         return bool
        """
        for key in condition_dict.keys():
            comp_val = condition_dict[key]
            target_val = target_dict.get(key)
            if str(comp_val) != str(target_val):
                return False
                # 異なるものが一つでもある場合終了する
        return True


def main():
    try:
        d = {'Alice': 5, 'Bob': 3, 'Charlie': 7}
        d2 = {'Alice': 5, 'Bob': 3}
        d3 = {'Bob': 3}
        n = len(d)
        print('n = ' + str(n))
        for val in d:
            print(val)
            print(val[1]) # l,o,h
        
        print('d.items')
        print(d.items())
        print('d2.items')
        print(d2.items())
        print('d3.items')
        print(d3.items())
        flag = d2 in d.items()
        print(flag)
        flag = d3 in d.items()
        print(flag)
        flag = d2.items() in d.items()
        print(flag)
        flag = d3.items() in d.items()
        print(flag)

        chk = (d3.keys(),d3.values())
        print('chk')
        print(chk)
        #chk = (d3.keys()[0],d3.values()[0]) #TypeError: 'dict_keys' object is not subscriptable
        val2:dict
        for val2 in d3:
            # chk = (val2.keys(),val2.values())#AttributeError: 'str' object has no attribute 'keys'
            chk = val2
            print('chk')
            print(chk)

        return

    except:
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()