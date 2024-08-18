"""
特定のフォルダの中のファイルリストを取得、
また、ファイルの情報（サイズ(バイト数、計算したバイト数KB,MB)、パス、ファイル名）などをリストで取得してCSVに出力する
"""
from pathlib import Path
import glob
import datetime
import os
import pandas as pd


def _test_main():
    device_name = 'DISK0__HDD_VIDEO_MEDIA'
    path = r'I:'
    #/
    start_time = datetime.datetime.now()
    print('start_time = {}'.format(start_time))
    
    paths = glob.glob(str(path) + '/**/*', recursive=True)
    print('len(paths)={}'.format(len(paths)))
    # #/
    #/
    # TEST
    # paths_file_path = paths[:10000]
    paths_file_path = paths
    print('---------')
    #/
    paths_file_name = []
    paths_dir_path = []
    paths_file_size = []
    paths_file_flag = []
    len_ten_per = len(paths_file_path)//10
    per_count = 1
    for i, path in enumerate(paths_file_path):
        buf_path = Path(path)
        if buf_path.is_file():
            paths_file_name.append(buf_path.name)
            paths_dir_path.append(str(buf_path.parent))
            buf = os.path.getsize(path)
            paths_file_size.append(buf)
            paths_file_flag.append(True)
        else:
            paths_file_name.append('')
            paths_dir_path.append(str(buf_path))
            paths_file_size.append(0)
            paths_file_flag.append(False)
        if (len_ten_per * per_count)<i:
            per_count += 1
            print('*', end='')
    print()
    print('name/dir proc end')
    print('size proc end')
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
    
    import re
    df['size_b'] = df['size'].apply(calc_byte)
    df_ig = df[df['size']<=0]
    df = df[df['size']>0]
    print('base  df.shape={},  df_ig.shape={}'.format(df.shape[0], df_ig.shape[0]))
    #/
    ignore_end_list = [
        '.JPG', '.jpg', '.jepg','.url', '.txt', '.dll', '.xml', '.exe'
        ,'.htm', '.html', '.lnk', '.eml', '.ini', '.dat', '.DAT'
        ,'.c', '.pl', '.x', '.tmp', '.BMP', '.TMP', '.cpp', '.h'
        ,'.java', '.css', '.C', '.X', '.js'
    ]
    for ignore_end_val in ignore_end_list:
        df_ig = concat_df(
            df_ig, df[df['path'].str.endswith(ignore_end_val)])
        df = df[~df['path'].str.endswith(ignore_end_val)]
    print('remove ext  df.shape={},  df_ig.shape={}'.format(
        df.shape[0], df_ig.shape[0]))
    #/
    ignore_folder_list = [
        r'\Utility', r'\ZProgram', r'\Bkup', r'\bkup', r'BKUP\ZMyFolder']
    for ignore_folder_val in ignore_folder_list:
        df_ig = concat_df(
            df_ig, df[df['path'].str.contains(re.escape(ignore_folder_val))])
        df = df[~df['path'].str.contains(re.escape(ignore_folder_val))]
    print('remove folders  df.shape={},  df_ig.shape={}'.format(
        df.shape[0], df_ig.shape[0]))
    # 前と同じディレクトリなら、カウントして、5000を超えたら除外リストへ
    #/
    before_dir_path = ''
    same_dir_name_now_count = 0
    FILE_AMOUNT_MAX = 5000
    delete_dir_list = []
    is_printed = False
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
            is_printed = False
        if (1000<same_dir_name_now_count) and (not is_printed):
            print('  dir = {}'.format(Path(now_dir_path).name))
            is_printed = True
        if FILE_AMOUNT_MAX<same_dir_name_now_count:
            delete_dir_list.append(now_dir_path)
        before_dir_path = now_dir_path
    print('len delete_dir_list = {}'.format(len(delete_dir_list)))
    for delete_dir_path in delete_dir_list:
        df_ig = concat_df(
            df_ig, df[df['dir'] == delete_dir_path])
        df = df[df['dir'] != delete_dir_path]
    print('remove many file folder  df.shape={},  df_ig.shape={}'.format(
        df.shape[0], df_ig.shape[0]))
    # BODER = 15000
    BODER = 20000
    small_check_ext_list = [
        '.jpg', '.gif', '.png', '.bmp', '.PNG', '.BMP', '.GIF', '.JPG'
    ]
    for small_ext in small_check_ext_list:
        df_ig = concat_df(
            df_ig, df[(df['name'].str.endswith(small_ext) & (df['size'] <= BODER))])
        df = df[~(df['name'].str.endswith(small_ext) & (df['size'] <= BODER))]
    # 'path' 列が 3桁の数字で終わらない行をフィルタリング
    # df = df[~df['name'].str.endswith(r'\d{3}$', na=False, case=False)]
    df_ig = concat_df(
        df_ig, df[df['name'].str.match(r'.*\d{3}$', na=False)])
    df = df[~df['name'].str.match(r'.*\d{3}$', na=False)]
    df_ig = concat_df(
        df_ig, df[~df['name'].str.contains(re.escape('.')) & (df['size'] <= BODER)])
    df = df[~(~df['name'].str.contains(re.escape('.')) & (df['size'] <= BODER))]
    print('remove small file  df.shape={},  df_ig.shape={}'.format(
        df.shape[0], df_ig.shape[0]))
    #/
    df_unique = df.drop_duplicates(subset='dir')
    #/
    df_b = df
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
    print('df.shape={}, df_ig.shape={}'.format(df.shape[0], df_ig.shape[0]))
    #/
    file_name = '__test_list_{}.csv'.format(device_name)
    file_path = str(Path(__file__).parent.joinpath(file_name))
    df_b.to_csv(file_path, encoding='sjis', errors='ignore')
    print('wpath = {}'.format(file_path))
    #/
    file_name_ig = '__test_list_{}_ig.csv'.format(device_name)
    file_path = str(Path(__file__).parent.joinpath(file_name_ig))
    df_ig.to_csv(file_path, encoding='sjis', errors='ignore')
    #/
    file_name_dir = '__test_list_{}_dir.csv'.format(device_name)
    file_path = str(Path(__file__).parent.joinpath(file_name_dir))
    df_unique.to_csv(file_path, encoding='sjis', errors='ignore')


def concat_df(df_ig, df_concat):
    df_ig = pd.concat([df_ig, df_concat], ignore_index=True)
    return df_ig

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
        if value < 1024:
            return str(value) + byte_str[i]
        value = value//1024
    else:
        print('max count')
        return str(value) + byte_str[i]



if __name__ == '__main__':
    print('\n*****')
    _test_main()