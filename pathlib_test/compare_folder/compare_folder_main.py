"""
path_a にあって、path_bに無いものを表示
path_a にあって、path_bにもある、重複するものを表示

"""

import glob
from pathlib import Path
import os
import datetime

def _test_main():
    print('*****\n')
    start_time = datetime.datetime.now()

    base_path_a = r'J:\ZMOVIE_SELECT2'
    base_path_b = r'J:\ZMOVIE_SELECT'
    print('base_path_a = {}'.format(base_path_a))
    print('base_path_b = {}'.format(base_path_b))

    paths_a = glob.glob(str(base_path_a) + '/**/*', recursive=True)
    print('len(paths_a)={}'.format(len(paths_a)))

    paths_b = glob.glob(str(base_path_b) + '/**/*', recursive=True)
    print('len(path_b)={}'.format(len(paths_b)))

    counter = CountPrinter()
    #/
    # exists a , not exists b
    # = only exists a
    list_in_a_not_in_b = []
    #/
    # exists a , exists b
    # = exists both
    list_in_both = []
    #/
    is_match_flag_pahs_a_list = []
    is_match = False
    for i, path_a in enumerate(paths_a):
        counter.count_up()
        if os.path.isdir(path_a):continue
        is_match = False
        for path_b in paths_b:
            if os.path.isdir(path_b):continue
            if os.path.basename(path_a) == os.path.basename(path_b):
            # if Path(path_a).name == Path(path_b).name:
                if os.path.getsize(path_a) == os.path.getsize(path_b):
                    is_match = True
                    break
        # is_match_flag_pahs_a_list.append(is_match)
        if is_match:
            # list_in_both.append(path_a)
            list_in_both.append(str(i))
        else:
            # list_in_a_not_in_b.append(path_a)
            list_in_a_not_in_b.append(str(i))
    print()
    
    print('replace  list_in_both')
    for i, list_in_both_num in enumerate(list_in_both):
        list_in_both[i] = paths_a[int(list_in_both_num)]
    print('replace  list_in_a_not_in_b_num')
    for i, list_in_a_not_in_b_num in enumerate(list_in_a_not_in_b):
        list_in_a_not_in_b[i] = paths_a[int(list_in_a_not_in_b_num)]

    print('len(list_in_a_not_in_b) = {}'.format(len(list_in_a_not_in_b)))
    print('len(list_in_both) = {}'.format(len(list_in_both)))

    dir_path = Path(__file__).parent
    with open(str(dir_path.joinpath('list_in_a_not_in_b.txt')), 'w', errors='ignore')as f:
        f.write('\n'.join(list_in_a_not_in_b))
    with open(str(dir_path.joinpath('list_in_both.txt')), 'w', errors='ignore')as f:
        f.write('\n'.join(list_in_both))
    proc_time = datetime.datetime.now() - start_time
    print('process_time = {}'.format(proc_time))
    print('done.')
    print()
# class InANotInBList():
#     def __init__(self) -> None:
#         self.match_list = []
#     def is_match_condition(path_a:str, path_b:str):
#         if Path(path_a).name != Path(path_b).name:
class CountPrinter():
    def __init__(self) -> None:
        self.max_count = 0
        self.now_count = 0
        # 1、10、100カウントごとに表示させるマークをリストで
        self.mark_list = ['', '.', '*','/','#']
    def count_up(self):
        self.now_count += 1
        self.print_mark()
    
    def print_mark(self):
        for i, mark in enumerate(reversed(self.mark_list)):
            div_num = pow(10, (len(self.mark_list)-1 - i))
            if div_num==0:
                div_num = 1
            if self.now_count % div_num == 0:
                print(mark, end='')
                break


if __name__ == "__main__":
    _test_main()