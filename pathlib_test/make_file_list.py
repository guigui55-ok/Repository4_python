
from pathlib import Path
import glob
import datetime
import os
import pandas as pd

def exact_ignore_values_ends_with(paths, paths_ignore:list, check_end_value:str):
    paths_ret_b = []
    paths_ignore_b = []
    for path in paths:
        if not Path(path).name.endswith(check_end_value):
            paths_ret_b.append(path)
        else:
            paths_ignore_b.append(path)
    paths_ignore.extend(paths_ignore_b)
    return paths_ret_b, paths_ignore

def exact_ignore_values_include(paths, paths_ignore:list, check_value:str):
    paths_ret_b = []
    paths_ignore_b = []
    for path in paths:
        if not check_value in str(path):
            paths_ret_b.append(path)
        else:
            paths_ignore_b.append(path)
    paths_ignore.extend(paths_ignore_b)
    return paths_ret_b, paths_ignore

def file_amount_is_upper(paths, amount:int):
    match_list = []
    checked_dir = []
    checkd_dir_name = []
    upeer_half = False
    for i, path in enumerate(paths):
        if not upeer_half:
            if len(paths)//2 < i:
                print('@@@@ [{} / {}]'.format(i, len(paths)))
                upeer_half = True
        if r'I:\_DISK\ETC\COMIC7__120502\その他\[エミュカタログ][SNES] スーパーファミコンコンプリートカタログ改訂版 Ver.070122\snescatalog\snes\snes\jpg ' in path:
            print()
        if Path(path).is_file():
            continue
            dir_path = str(Path(path).parent)
        else:
            dir_path = str(path)
        if (dir_path in checked_dir):
            if Path(dir_path).name in checkd_dir_name:
                print('.', end='')
                continue
        if r'/System Volume Information' in dir_path:
            continue
        num = sum(os.path.isfile(os.path.join(dir_path, name)) for name in os.listdir(dir_path))
        # buf_path = glob.escape(str(dir_path))
        # buf_paths = glob.glob(buf_path + '/*')
        # num = len(buf_paths)
        if amount <= num:
            match_list.append(dir_path)
        if 1000 <= num:
            print('dir_path = {} [{}]'.format(Path(dir_path).name, num))
            
        if not (dir_path in checked_dir):
            if not (Path(dir_path).name in [Path(x).name for x in checked_dir]):
                checked_dir.append(dir_path)
                checkd_dir_name.append(Path(dir_path).name)
        # print('-', end='')
        if i%10000==0:
            print('-', end='')
    print('\n')
    return match_list




def _test_main():
    start_time = datetime.datetime.now()
    print('start_time = {}'.format(start_time))
    path = r'I:'
    # paths = glob.glob(str(path) + '/*', recursive=True)
    paths = glob.glob(str(path) + '/**/*', recursive=True)
    print('len(paths)={}'.format(len(paths)))
    # #/
    ignore_end_list = [
        '.JPG', '.jpg', '.jepg','.url', '.txt', '.dll', '.xml', '.exe'
        ,'.htm', '.html', '.lnk', '.eml', '.ini', '.dat', '.DAT'
    ]
    # #/
    # paths_ignore = []
    # paths_b = paths
    # #/
    # for ignore_end_val in ignore_end_list:
    #     paths_b, paths_ignore = exact_ignore_values_ends_with(
    #         paths_b, paths_ignore, ignore_end_val)
    #     # print('{} ,{}'.format(len(paths_b), len(paths_ignore)))
    #     print('.', end='')
    #/
    # ignore_folder_list_amount = []
    # ignore_folder_list_amount = file_amount_is_upper(paths_b, 5000)
    #/
    ignore_folder_list = [
        r'\Utility', r'\ZProgram', r'\Bkup', r'\bkup',]
    # ignore_folder_list.extend(ignore_folder_list_amount)
    # for ignore_folder_name in ignore_folder_list:
    #     paths_b, paths_ignore = exact_ignore_values_include(
    #         paths_b, paths_ignore, ignore_folder_name)
    #     print('*', end='')
    # print('\n', end='')
    # print('len(paths_b)={}'.format(len(paths_b)))
    # print('len(paths_ignore)={}'.format(len(paths_ignore)))
    #/
    # TEST
    # paths_file_path = paths_b[:10000]
    # paths_file_path = paths_b
    paths_file_path = paths
    print('---------')
    import pprint
    # pprint.pprint(paths_b[:100])
    #/
    device_name = 'BACKUP5'
    paths_file_name = []
    paths_dir_path = []
    for path in paths_file_path:
        buf_path = Path(path)
        if buf_path.is_file():
            # size = os.path.getsize(path)
            paths_file_name.append(buf_path.name)
            paths_dir_path.append(str(buf_path.parent))
        else:
            paths_file_name.append('')
            paths_dir_path.append(str(buf_path))
    print('name/dir proc end')
    #/
    paths_file_size = []
    for path in paths_file_path:
        buf_path = Path(path)
        if buf_path.is_file():
            # size = os.path.getsize(path)
            buf = os.path.getsize(path)
            paths_file_size.append(buf)
        else:
            paths_file_size.append(0)
    print('size proc end')
    #/
    paths_file_flag = []
    for path in paths_file_path:
        buf_path = Path(path)
        if buf_path.is_file():
            paths_file_flag.append(True)
        else:
            paths_file_flag.append(False)
    print('file flag proc end')
    #/
    data = {
        'name':paths_file_name,
        'size':paths_file_size,
        'path':paths_file_path,
        'is_file':paths_file_flag,
        'dir':paths_dir_path
    }
    df = pd.DataFrame(data)
    print('base  df.shape={}'.format(df.shape[0]))
    # df = pd.DataFrame()
    # df['name'] = paths_file_name
    # df['size'] = paths_file_size
    # df['path'] = paths_file_path
    df = df[df['size']>0]
    df['size_b'] = df['size'].apply(calc_byte)

    #/
    for ignore_end_val in ignore_end_list:
        df = df[not df['path'].str.endswith(ignore_end_val)]
    print('remove ext  df.shape={}'.format(df.shape[0]))
    for ignore_folder_val in ignore_folder_list:
        df = df[not df['path'].str.contains(ignore_folder_val)]
    print('remove folders  df.shape={}'.format(df.shape[0]))
    # 前と同じディレクトリなら、カウントして、5000を超えたら除外リストへ
    #/
    before_dir_path = ''
    same_dir_name_now_count = 0
    max_count = 5000
    delete_dir_list = []
    for row_index in df.index:
        # インデックスラベルを使って行を取得
        row = df.loc[row_index]
        now_dir_path = row['dir']
        if now_dir_path in delete_dir_list:
            continue
        if before_dir_path==now_dir_path:
            same_dir_name_now_count+=1
        else:
            same_dir_name_now_count=0
        if max_count<same_dir_name_now_count:
            delete_dir_list.append(now_dir_path)
    print('len delete_dir_list = {}'.format(len(delete_dir_list)))
    for delete_dir_path in delete_dir_list:
        df = df[df['dir'] != delete_dir_path]
    print('remove many file folder  df.shape={}'.format(df.shape[0]))
    # TEST
    # df_b = df[df['size'] > 0]
    # df_b = df[df['size'] > 1000]
    df_b = df
    # columns = change_column_place_to_col_a_after_col_b(
    #     list(df_b.columns), 'size', 'size_b')

    columns = change_column_place_to_col_a_after_col_b(
        list(df_b.columns), 'path', 'size')
    df_b = df_b[columns]
    print('---------')
    # print(df.head())
    print(df_b.iloc[1])
    #/
    print('---------')
    print(df_b.columns)
    diff_time = datetime.datetime.now() - start_time
    print('diff_time = {}'.format(diff_time))
    print('df.shape={}'.format(df.shape[0]))
    file_name = '__test_list_{}.csv'.format(device_name)
    file_path = str(Path(__file__).parent.joinpath(file_name))
    df_b.to_csv(file_path, encoding='sjis', errors='ignore')
    print('wpath = {}'.format(file_path))



def change_column_place_to_col_a_after_col_b(lst, col_a, col_b):
    result = []
    i = 0
    while i < len(lst):
        if lst[i] == col_b:
            i += 1
            continue
        result.append(lst[i])
        if lst[i] == col_a:
            result.append(col_b)
        i += 1
    return result

def calc_byte(value):
    byte_str = ['','K','M','G','T']
    for i in range(5):
        if value < 1000:
            return str(value) + byte_str[i]
        value = value//1000
    else:
        print('max count')
        return str(value) + byte_str[i]



if __name__ == '__main__':
    print('\n*****')
    _test_main()