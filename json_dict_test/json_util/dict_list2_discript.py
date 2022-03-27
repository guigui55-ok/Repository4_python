
import pstats
from typing import Dict
from numpy import isin

import enum
class DictListType(enum.Enum):
    #not has iterable
    TERMINATE_VALUE=0
    TERMINATE_DICT=1
    TERMINATE_LIST=2
    #has iterable
    HAS_ITERABLE_DICT=3
    HAS_ITERABLE_LIST=4
    VALUE=10
    KEY=11
    DICT=12



def cnv_list_str(value:list):
    """valueをlist[str]にする"""
    ret_list = []
    if len(value)<1:
        return []
    else:
        if not is_list_str(value):
            for buf in value:
                if not isinstance(buf ,str):
                    ret_list.append(str(buf))
                else:
                    ret_list.append(buf)
            return buf
        else:
            return value

def is_list_str(value:list):
    """valueがlist[str]か判定する"""
    ret_list = []
    if len(value)<1:
        return None
    else:
        for buf in value:
            if not isinstance(buf ,str):
                return False
        return True

def is_exists_in_dict(arg_dict:dict, key:str,value=None):
    """
    arg_dictにkeyが存在するか判定する。
     valueを指定する場合は、arg_dict[key]==valueの結果を返す。
    value=Noneの場合は、keyの存在だけを判定する。
    """
    if arg_dict == None: return False
    flag = False
    for d in arg_dict.keys():
        if d == key:
            flag = True
    else:
        flag = False
    if value == None:
        return flag
    else:
        if flag:
            target_key_value = arg_dict[key]
            if target_key_value == value:
                return True
            else:
                return False
        else:
            return False

def count_in_dict(arg_dict:dict, key:str,value=None)->int:
    """
    arg_dictに存在するkeyをカウントする。
     valueを指定する場合は、arg_dict[key]==valueをカウントする。
    value=Noneの場合は、keyの存在だけを判定する。
     ※dict型に同じkeyは存在しない(python 3.10.0 22/3/14)(value = json.loads('{"key3": "value3", "key3":"value4" }')#str->dictで確認済み)が、同じkeyが存在することになる可能性も考慮する。
    """
    if arg_dict == None: return 0
    count:int = 0
    if key != None and value == None:
        for k in arg_dict.keys():
            if k == key:
                count += 1
        else:
            count = 0
    elif key == None and value != None:
        for v in arg_dict.values():
            if v == value:
                count += 1
    elif key != None and value != None:
        is_exists = is_exists_in_dict(arg_dict,key,value)
        if is_exists:
            # 念のため複数同じkeyが含まれることも考慮している
            for k in arg_dict.keys():
                if k == key:
                    if arg_dict[k] == value:
                        # 同じkeyが含まれることになった場合は、この処理で同じ値を参照していることになる
                        count += 1
            return count
        else:
            return 0
    else:
        raise Exception()
    return count


class DictListElement():
    key:str=None
    value=None
    dictlist_elements:'list[DictListElement]'=None
    __is_terminate:bool = True
    __is_terminate_dict:bool = False
    __is_terminate_list:bool = False
    hierarchy = 0
    def __init__(self,value,hierarchy:int=0) -> None:
        self.hierarchy = hierarchy + 1
        if isinstance(value,dict):
            self.set_value(value)
        elif isinstance(value,list):
            self.set_value(value)
        else:
            self.set_value(value)
            
    @property
    def is_terminate(self):
        return self.__is_terminate
    @is_terminate.setter
    def is_terminate(self, value):
        self.__is_terminate = value
        if value == True:
            self.__is_terminate_dict = False
            self.__is_terminate_list = False
    @property
    def is_terminate_dict(self):
        return self.__is_terminate_dict
    @is_terminate_dict.setter
    def is_terminate_dict(self, value):
        self.__is_terminate_dict = value
        if value == True:
            self.__is_terminate = False
            self.__is_terminate_list = False
    @property
    def is_terminate_list(self):
        return self.__is_terminate_list
    @is_terminate_list.setter
    def is_terminate_list(self, value):
        self.__is_terminate_list = value
        if value == True:
            self.__is_terminate_dict = False
            self.__is_terminate = False

    def reset_self(self):
        self.key = None
        self.value = None
        self.dictlist_elements = None
        self.__is_terminate = False
        self.__is_terminate_dict = False
        self.__is_terminate_list = False
        self.hierarchy = 0
        self.root_is_list = False
    
    def get_value_type(self):
        if self.is_terminate:
            return DictListType.TERMINATE_VALUE
        elif self.is_terminate_dict:
            return DictListType.TERMINATE_DICT
        elif self.is_terminate_list:
            return DictListType.TERMINATE_LIST
        elif self.is_dict():
            return DictListType.HAS_ITERABLE_DICT
        elif self.is_list():
            return DictListType.HAS_ITERABLE_LIST
    
    def set_value(self,value):
        """受け取った値をセットする。
         valueはself.valueに格納し、その後、valueがdict,listである場合は、持っている要素を分割してself.dictlistに格納する。
        この場合、メモリ領域は2倍使うことになる。
         """
        # セットするときは値をリセットしておく
        self.reset_self()
        if isinstance(value,dict):
            # 受け取った値はvalueに格納、その子要素はdictlistに格納する
            self.value:dict = value
            self.dictlist_elements = []
            for buf in value.keys():
                self.dictlist_elements.append(DictListElement(value[buf],self.hierarchy))
            # self.dictlist_elements が実値の場合はis_terminate==Trueとなる。
            # さらに、len(dictlist_elements)==1の時、この階層(このクラス)は最下層から2つ目「{"key":value}」となる
            if len(self.dictlist_elements)==1 and self.dictlist_elements[0].is_terminate:
                self.is_terminate_dict = True
                self.key = value.keys()[0]
        elif isinstance(value,list):
            self.value:list = value
            self.dictlist_elements = []
            is_iterable = True
            for buf in value:
                self.dictlist_elements.append(DictListElement(buf,self.hierarchy))
                if (isinstance(buf,dict) or isinstance(buf,list)):
                    # single value(not iterable)
                    is_iterable = True
            # 要素にdict,listを含む場合は、末端のlistではない
            if not is_iterable:
                self.is_terminate_list = True
            # self.dictlist_elements が実値の場合はis_terminate==Trueとなる
            # この時、この階層は最下層から2つ目となる
        else:
            # terminate value(str,int、boolなどの実値)
            self.value = value
            self.is_terminate = True
            ###
            # 再帰的に値を代入していって、最終的には
            # str,int,boolなどの実値が代入される。その時はis_terminateフラグをTrueにする。
            ###
            # 末端値（実値）の1階層上は 
            # {"key":value} or {"key":[]}（末端dict値[keyと値が1つずつしかないdict]）、
            # または、[value]（末端list値[要素がlist,dictを持たないlist]）
            # となっていることは確定（3パターン）
            ###
            # さらにその上の階層からは、1.実値、2.末端dict値、3.末端list、
            # 4.dictまたはlistを持つdict、5.dictまたはlistを持つlist、の5種類混在となる（パターンは5種類のみ）
            # dictまたはlistを持つdict は dictとlist両方を持つdictを含む
            # dictまたはlistを持つlist は dictとlist両方を持つlistを含む
            # key検索などの場合に、末端dict,listとそうでないdict,listで異なる処理が必要なため上記のパターンに分類する。
            ###
            # 末端化の判定は is_terminate , is_terminate_dict , is_terminate_list 変数で行う
            # list,dictの判定は isinstans 関数で行う
            ###
            # 値を扱うときは、is_terminate、

    def is_exists(self,key=None,value=None):
        """key,valueが存在するか判定する。
         keyを指定する場合は、dict型のみを対象とする。（key=key_name[str],value=[Any/None]）
        keyのみを指定する場合は、key in dict.keys() の判定結果を返す。
         keyとvalueを指定する場合は、dict[key] == value の判定結果を返す。
        valueのみを指定する場合は、すべての要素・型を対象とする。（key=None,value=Any）
        """
        if self.is_terminate:
            # 終端値の場合はKeyを持たない
            # self.dictlist_elements == None
            if key == None:
                if self.value == value:
                    ret = True
                else:
                    ret = False
            else:
                ret = False
            return ret
        elif self.is_terminate_dict:
            # 末端の場合は単に確認する
            self_value:dict = self.value
            ret = is_exists_in_dict(self_value,key,value)
            return ret
        elif isinstance(self.value,dict):
            # まず単に確認する
            ret = is_exists_in_dict(self_value,key,value)
            if not ret:
                # 末端ではない場合、Falseの場合は、下層まで確認する
                dictlist:DictListElement = None
                for dictlist in self.dictlist_elements:
                    ret = dictlist.is_exists(key,value)
                    if ret: return ret
            return ret
        elif self.is_terminate_list:
            # key を指定する場合は、dict型のみを対象とする
            if key != None:
                return False
            else:
                self_value:list = self.value
                for buf in self_value:
                    if buf == value:
                        return True
                return False
        elif isinstance(self.value,list):
            # 末端ではないlistの場合は、下層にdictがあるかもしれないので、下層まで確認する
            dictlist:DictListElement = None
            for dictlist in self.dictlist_elements:
                ret = dictlist.is_exists(key,value)
                if ret: return ret
        else:
            raise Exception('unexpected case')
        return False
    
    def is_list(self):
        return isinstance(self.value,list)
    def is_dict(self):
        return isinstance(self.value,dict)

    def count(self,key=None,value=None,internal_count:int=0)->int:
        """key,valueが存在する回数(個数)をカウントする。
         keyを指定する場合は、dict型のみを対象とする。（key=key_name[str],value=[Any/None]）
        keyのみを指定する場合は、key in dict.keys() のカウントを返す。
         keyとvalueを指定する場合は、dict[key] == value のカウントを返す。
        valueのみを指定する場合は、すべての要素・型を対象としてカウントする（この場合keyはカウントしない）。（key=None,value=Any）
         ※主にkey重複しているか判定するのに使う想定。
        """
        # internal_count は内部カウント用
        # 再帰的に実行するため、カウント数を引き継ぐための変数
        # internal_count を隠蔽した外部用関数も定義する予定
        count:int = internal_count
        if self.is_terminate:
            # 終端値の場合はKeyを持たない
            # self.dictlist_elements == None
            if key != None:
                return count
            else:
                if self.value == value:
                    count += 1
                    return count
                else:
                    return count
        elif self.is_terminate_dict:
            # 末端の場合は単にカウントする
            self_value:dict = self.value
            count = count_in_dict(self_value,key,value)
            return count
        elif isinstance(self.value,dict):
            # まず単にカウントする
            count = count_in_dict(self_value,key,value)
            # 末端ではない場合、下層までカウントする
            dictlist:DictListElement = None
            for dictlist in self.dictlist_elements:
                count += dictlist.count(key,value)
            return count
        elif self.is_terminate_list:
            # key を指定する場合は、dict型のみを対象とする
            if key != None:
                return count
            else:
                self_value:list = self.value
                for buf in self_value:
                    if buf == value:
                        count += 1
                return count
        elif isinstance(self.value,list):
            # 末端ではないlistの場合は、下層までカウントする
            dictlist:DictListElement = None
            for dictlist in self.dictlist_elements:
                count += dictlist.count(key,value)
            return count
        else:
            raise Exception('unexpected case')
        return count
    
    def update_target(self,target_values,value=None):
        """target_values(dict型)を指定して、その場所のvalueを更新する"""
        pass

    def update_value_core(self,self_value,update_value,count=0):
        pass

    def update_part(self,value,hierarchy=0):
        """
        単に値を更新する場合は、dict.updateを使用する
        部分的に更新したい場合は、この関数を使う
        ** そこまでたどってから、valueを代入する

        valueがjson:dict+listの時
        valueがterminate_valueのとき

        元の値 : {"key":[{"key21":"value21"},{"key22":"value22"}]}
        更新する値 : {"key":[{"key21":"value21_1"}]}
        のとき、元の値{"key22":"value22"}が消えてしまう。

        更新したい値のパターン
        更新データ：更新先備考
        {"key1":"value1"}  更新先には複数のdictがある
        {"key2":["value2"]}  更新先のリストには複数のデータがある
        {"key3":{"key3-2":"value3-2"}}  更新先のdictには複数のデータがある
          →key:value, dict 形式のものはひとくくりにして扱う

        [
            {"key4":"value4",
             "key5":"value5"}
        ]
        ※"key4":"value4" のとき "key5":"value5" にしたいとき
          （"key4":"value4-2" などの時は、更新されない）
          →update_with_condition 関数で扱う、update_with_compare

        単に値を変更したい場合
        "value1" -> "value2"
          →value1 を探して value2にする

        値を更新する
        値を追加する
        すでに値がなければ追加する（すでに値があるものは更新）
        すでに値がなければ追加しない
        値があっても追加する（値がなくても追加する）

        リストに追加するのは置き換えればOK
        Dictに追加するのは、フラグ管理
        """
        if not isinstance(value,dict):
            #最初に与える値はdictでなければならない
            raise Exception('cant add value. value is not dict')

        if not isinstance(value,DictListElement):
            update_val:DictListElement = DictListElement(value)
        else:
            update_val = value
        
        if hierarchy < 0:
            hierarchy =0
        self_el : DictListElement 

        if hierarchy == 0:
            # rootの処理
            # rootの値はdict限定,update
            for dict_el in update_val.dictlist_elements:
                for i in range(len(self.dictlist_elements)):
                    self_el = self.dictlist_elements[i]
                    if hierarchy > self.hierarchy:
                        self.dictlist_elements[i].update_part(dict_el,hierarchy+1)
                        continue

                    if dict_el.is_terminate:
                        #最初に与える値はdictでなければならない
                        raise Exception('cant add value. value is not dict')
                        
                    elif dict_el.is_terminate_dict:
                        #keyが合うものは更新
                        #keyがないものは追加
                        if dict_el.key == self_el.key:
                            self.dictlist_elements[i] = self_el.value
                    elif dict_el.is_terminate_list:
                        #最初に与える値はdictでなければならない
                        raise Exception('cant add value. value is not dict')
                    elif dict_el.is_list():
                        #最初に与える値はdictでなければならない
                        raise Exception('cant add value. value is not dict')
                    elif dict_el.is_dict():
                        #合うものがあれば次の階層に
                        self.dictlist_elements[i].update_part(dict_el,hierarchy+1)
                ### end for
            ### end for
        else:
            #hierarucy>0
            for dict_el in update_val.dictlist_elements:
                for i in range(len(self.dictlist_elements)):
                    self_el = self.dictlist_elements[i]
                    if hierarchy > self.hierarchy:
                        self.dictlist_elements[i].update_part(dict_el,hierarchy+1)
                        continue

                    if dict_el.is_terminate:
                        pass
                        #dict>>terminate_list>>value
                        #dict>>terminate_dict>>value xxx
                        #dict>>value のパターンはない
                        #self_el.is_terminateの場合がある

                        raise Exception('cant add value. value is not dict')
                    elif dict_el.is_terminate_dict:
                        if self_el.is_terminate_dict:
                            #構成が異なる場合
                            pass
                        #keyが合うものは更新
                        #keyがないものは追加
                        if dict_el.key == self_el.key:
                            self.dictlist_elements[i] = dict_el.value

                    elif dict_el.is_terminate_list:
                        #keyが存在しないので、値をそのまま更新する
                        #子にイテラブルな値がない場合、すべて上書きする
                        self.dictlist_elements[i] = dict_el.value
                    elif dict_el.is_list():
                        # self.dictlist_elements[i].update_part(dict_el,hierarchy+1)
                        if dict_el.key == self_el.key:
                            self.dictlist_elements[i] = dict_el.value
                        """
                        list
                            list
                            list
                        のときは、１に追加するか、２に追加するか
                        ------
                        パターン
                        dict 1
                            list
                                list *
                                list
                                    dict 2
                            list
                                list 4
                                list
                                    dict 3
                        この時は１，２，３どれに追加・更新するか
                        ------
                        通常は、すべて最初のリストを選択する（上記パターン○では*を選択する）
                        target_hierarucyを用意して
                        1-1-2,0-1-2,*-1-2 の場合2を更新
                        1-2-2,0-2-2,*-2-2の場合は3を更新
                        1-1、の場合は1を更新
                        1-2、の場合は4に追加
                            不採用
                            list-listはすべて上書きする
                            key:valueのみを対象とする
                        ------
                        パターン
                        update_val が
                        dict
                            list
                                list 1
                                list 2
                        の場合
                        1更新後2で上書きされる
                            →
                        -----
                        以下のパターンが必要
                            replace_list_index
                            append_list
                            ×not_update_exists:すでにある値は更新しない：外部で対応
                        -----
                        パターン
                        self_valが
                        dict
                            list
                                list
                                list
                                list
                        、update_valが
                        dict
                            list
                                list 1
                                list 2
                        のとき
                        -----
                        dict
                            list
                            dict
                            list
                        このパターンは存在しない
                        key:Value=listを持つ階層は、listが1つしか存在できない
                            親がlistの場合、list,value、dictなどを持つことがある（listの中身は自由）
                        つまり、
                        dict
                        key:[],[]となることはない
                        key:[[] , []]これはある
                        -----
                        リストinリストは外部で扱う-get_valueを充実させ、任意の値を取得しやすくすれば処理が容易になるはず
                        原則としてkey:value を対象にする
                        ke:[[],[key:value]]
                         これを更新したいときはDictListElementにこれを入れて加工したあと、Add、Updteすればよい
                        ------
                        List in list を扱うのは別の関数

                        """

                    elif dict_el.is_dict():
                        #合うものがあれば次の階層に
                        #list<listを考慮すると、対応が煩雑になるため,dictであればすべて更新して処理は終了する
                        #list<list<dictなどの構成パターンは、外部で別途DictListElementで加工してから、追加・更新する
                        self.dictlist_elements[i].update_part(dict_el,hierarchy+1)
                ### end for
            ### end for



    ################################################################
    ################################################################
    ################################################################
    ################################################################
    def get_value_dictlist_has(self,value,type:int=DictListType.KEY,hierarchy=0,count=1):
        """target_valueを持っている値を返す（target_valueそのものではない）"""
        target = value
        if hierarchy < 0:
            hierarchy =0
        self_el : DictListElement 
        ret_els : 'list[DictListElement]' = []
        for i in range(count):
            for i in range(len(self.dictlist_elements)):
                self_el = self.dictlist_elements[i]
                if self_el.is_terminate:
                    if self.is_match_self(target,type):
                        ret_els.append(self)
                elif self_el.is_terminate_dict:
                    if self.is_match_self(target,type):
                        ret_els.append(self)
                    else:
                        #dict{key:value}1つのみの値、なければNoneを返す
                        pass
                elif self_el.is_terminate_list:
                    pass
                elif self_el.is_list():
                    #Keyがないので次の階層に
                    ret = self_el.get_value_dictlist_has(value,type,hierarchy+1)
                    ret_els.append(ret)
                elif self_el.is_dict():
                    #合うものがなければ次の階層に
                    if self.is_match_self(target,type):
                        ret_els.append(self)
                    else:
                        ret = self_el.get_value_dictlist_has(value,type,hierarchy+1)
                        ret_els.append(ret)
            ### end for
        return ret_els

    def is_match_self(self,value,type):
        if type == DictListType.KEY:
            if self.key == value:
                return True
            else:
                return False
        elif type == DictListType.DICT:
            value_dict:dict = value
            key = value_dict.keys()[0]
            value = value_dict.values()[0]
            if self.key == key and self.value == value:
                return True
            else:
                return False
    ################################################################
    def get_value_dictlist(self,value,type:int=DictListType.KEY,hierarchy=0,count=1):
        """
        Keyかdict{key:value}が一致するdictlistElementを取得する

        valueにkey,dictを入れて、比較し、値を取得することを想定する
        """
        target = value
        if hierarchy < 0:
            hierarchy =0
        self_el : DictListElement 
        ret_els : 'list[DictListElement]' = []
        for i in range(count):
            for i in range(len(self.dictlist_elements)):
                self_el = self.dictlist_elements[i]

                if self_el.is_terminate:
                    if self.is_match_self(target,type):
                        ret_els.append(self_el)
                elif self_el.is_terminate_dict:
                    if self.is_match_self(target,type):
                        ret_els.append(self_el)
                    else:
                        #dict{key:value}1つのみの値、なければNoneを返す
                        pass
                elif self_el.is_terminate_list:
                    pass
                elif self_el.is_list():
                    #Keyがないので次の階層に
                    ret = self_el.get_value_dictlist(value,type,hierarchy+1)
                    ret_els.append(ret)
                elif self_el.is_dict():
                    #合うものがなければ次の階層に
                    if self.is_match_self(target,type):
                        ret_els.append(self_el)
                    else:
                        ret = self_el.get_value_dictlist(value,type,hierarchy+1)
                        ret_els.append(ret)
            ### end for
        return ret_els

    def is_match_self(self,value,type):
        if type == DictListType.KEY:
            if self.key == value:
                return True
            else:
                return False
        elif type == DictListType.DICT:
            value_dict:dict = value
            key = value_dict.keys()[0]
            value = value_dict.values()[0]
            if self.key == key and self.value == value:
                return True
            else:
                return False

    # update _list


                





class DictList():
    """dict型を取り扱うユーティリティクラス
    dict型でも、JSONをdictとして読み込んだ場合valueがlistの場合があり、それに対応したもの
    扱うデータがdictの場合もあるしlistの場合もある
    """
    value = None
    def __init__(self,value_dict_or_list,is_no_check_type:bool=False) -> None:
        arg_value = value_dict_or_list
        list : list = []
        if not is_no_check_type:
            if isinstance(arg_value, list):
                for val in arg_value:
                    if isinstance(val, dict):
                         list.append(val)
                    else:
                        raise Exception('value is not dict')
            else:
                raise Exception('dict_list is not list')
            self.value = arg_value
        else:
            self.value = arg_value
    
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
    
    def update_dict_by_dict(self,update_dict:dict,condition_dict:dict):
        """only first comp(match)"""
        _condition_dict:dict = None
        if isinstance(condition_dict,dict):
            _condition_dict = condition_dict
        else:
            raise Exception('condition_dict is invalid')
        
        for i in range(len(self.value)):
            dict_value = self.value[i]
            if self.comp_dict_in_dict(dict_value,_condition_dict):
                self.value[i].update(update_dict)

    def get_value_by_dict(self,key:str,condition_dict:dict):
        """only first comp(match)"""
        _condition_dict:dict = None
        if isinstance(condition_dict,dict):
            _condition_dict = condition_dict
        else:
            raise Exception('condition_dict is invalid')
        
        for dict_value in self.value:
            if self.comp_dict_in_dict(dict_value,_condition_dict):
                value = dict_value[key]
                return value
    
    def comp_dict_in_dict(self,target_dict:dict,condition_dict:dict):
        """dictがcondition_dictとすべて合致する(含まれる)か判定する
        return float?
        """
        for key in condition_dict.keys():
            comp_val = condition_dict[key]
            target_val = target_dict.get(key)
            if str(comp_val) != str(target_val):
                return False
                # 異なるものが一つでもある場合終了する
        return True
    
    def get_key_list(self,key:str=''):
        ret_list = []
        if key=='':
            ret_list = self.value
    

    def get_value(self,key:str):
        pass


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