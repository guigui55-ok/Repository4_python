

from pathlib import Path
import datetime
import copy
def _test_main():
    start_time = datetime.datetime.now()
    # dir_path_str = r'C:\Users\OK\Desktop'
    dir_path_str = r'C:\Users\OK\source\repos\Learning\learning_python\scraping_tool\scraping_main\__test_data'
    path = Path(dir_path_str).joinpath('url_list.txt')
    with open(path, 'r')as f:
        lines = f.readlines()
    # lines = [1,2,3,4,5,6,7,7,8,9]
    lines_a = copy.copy(lines)
    print('lines_a = {}'.format(len(lines_a)))
    lines = [x[:-1].replace('https://sports.yahoo.co.jp/keiba/','') for x in lines]
    new_lines = []
    for line in lines:
        if '?detail=1' in line:
            continue
        elif 'odds/tfw' in line:
            continue
        elif 'predict' in line:
            continue
        elif 'matrix' in line:
            continue
        else:
            new_lines.append(line)
    lines = new_lines
    print('lines[2] = {}'.format(len(lines)))
    dup_count = 0
    dup_index_list = []
    dup_index_list_double = []
    for i, line_a in enumerate(lines):
        if i%100==0:
            if i%1000==0:
                if i%10000==0:
                    print('@', end='')
                else:
                    print('*', end='')
            else:
                print('/', end='')
        if i in dup_index_list:
            # print('continue[{}]'.format(i))
            print('.', end='')
            continue
        for j, line_b in enumerate(lines[i:]):
            if i==i+j:
                continue
            if line_a == line_b:
                # flag = (lines[i]==lines[i+j])
                dup_index_list.append(i+j)
                dup_index_list_double.append('{}-{}'.format(i,i+j))
    print()
    diff = datetime.datetime.now() -start_time
    print('======')
    print(datetime.datetime.now())
    print('diff_time = {}'.format(diff))
    import pprint
    print('lines_a = {}'.format(len(lines_a)))
    print('lines[2] = {}'.format(len(lines)))
    #/
    print('len(dup_index_list) = {}'.format(len(dup_index_list)))
    print('dup_index_list = {}'.format(dup_index_list))
    print('======')
    # pprint.pprint(dup_index_list_double)
    wpath = str(Path(__file__).parent.joinpath('__test.txt'))
    dup_index_list_double_str = [str(x) + '\n' for x in dup_index_list_double]
    with open(wpath, 'w')as f:
        f.writelines(dup_index_list_double_str)
    print('wpath = {}'.format(wpath))


if __name__ == '__main__':
    print('\n*****')
    _test_main()

"""
lines = 41944
diff_time = 0:03:57.803488
len(dup_index_list) = 1988

diff_time = 0:02:47.145861
len(dup_index_list) = 1988

240719
diff_time = 0:08:12.167807
len(dup_index_list) = 5473

240721

2024-07-21 22:51:10.042682
diff_time = 0:17:45.984499
lines = 111577
lines[2] = 89299
len(dup_index_list) = 6606
======
2024-07-23 14:09:25.427516
diff_time = 0:18:46.311512
lines_a = 114165
lines[2] = 94090
len(dup_index_list) = 6007
======
2024-07-26 21:45:21.571413
diff_time = 0:19:55.956710
lines_a = 116053
lines[2] = 96625
len(dup_index_list) = 5844
"""