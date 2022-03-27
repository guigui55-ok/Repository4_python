import import_init
from import_init import get_path_from_current
import json_util.dict_list3 as dict_list
from json_util.dict_list3 import DictList, DictListElement
from json_util.json_class import JsonUtil

def main():
    try:
        dict_val1="""
{

}
        """
        file_name = 'dict_list1.json'
        path = get_path_from_current(__file__,file_name)
        bar = '###############################################################'
        ju = JsonUtil(path)
        dict_data = ju.values
        # print(bar)
        # print(dict_data)
        dl = DictListElement(dict_data)
        # print(bar)
        # dl.print_values(True,True)
        print(bar)
        val = dl.get_json_str()
        print(val)

        return
    except:
        import traceback
        traceback.print_exc()

main()
