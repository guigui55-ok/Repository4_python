

class update_value():
    def __init__(self,file_name:str,value:str) -> None:
        self.file_name:str = ''
        self.value:str = value
    

def set_find_list(path:str)->list[str]:
    import os
    file_list = os.listdir(path)
    return file_list

def find_pos(value:str,find_list:list[str])->str:
    pos_list:list[int] = []
    val_list:list[str] = []
    # value の中に Find_list があるか探す
    # find_listの中で一番最初に出現した位置と、そのときのfind_list の値を返す
    for i in range(len(find_list)):
        find_val = find_list[i]
        pos = value.find(find_val)
        if pos > 0:
            pos_list.append(pos)
            val_list.append(find_val)
    # 最小値を取得
    ret_pos = min(pos_list)
    # 最小値の時のファイル名
    ret_val = ''
    for i in range(len(pos_list)):
        n = pos_list[i]
        if n == ret_pos:
            ret_val = val_list[i]
    return ret_pos,ret_val


def exact_json_value():
    try:
        file_list = set_find_list(__file__)


        path = './test_json.txt'
        with open(path,'r') as f:
            read_data = f.read()
        
        print(read_data)

        update_json_list:list[str]=[]
        pos,value = find_pos(read_data,file_list)
        if pos > 0:
            leftpos = 0
            rightpos = pos + len(value)-1
            now_val = read_data[leftpos:rightpos]
            update_json_list.append(now_val)
            next_val = read_data[rightpos:]
            pos,value = find_pos(next_val,file_list)
            while(pos>0):
                leftpos = 0
                rightpos = pos + len(value)-1
                now_val = read_data[leftpos:rightpos]
                update_json_list.append(now_val)
                next_val = read_data[rightpos:]
                pos,value = find_pos(next_val,file_list)


        value = ''
        return
    except:
        import traceback
        traceback.print_exc()


exact_json_value()