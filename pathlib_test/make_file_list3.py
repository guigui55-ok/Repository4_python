
from pathlib import Path
import glob
import datetime
import os
import pandas as pd


# 列データを作成する関数
def extract_info(path):
    if os.path.isfile(path):
        name = os.path.basename(path)
        size = os.path.getsize(path)
        dir_path = os.path.dirname(path)
    elif os.path.isdir(path):
        name = ""
        # size = sum(os.path.getsize(os.path.join(dirpath, filename)) 
        #            for dirpath, _, filenames in os.walk(path) 
        #            for filename in filenames)
        size = 0
        dir_path = ''
        try:
            for dirpath, _, filenames in os.walk(path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    try:
                        size += os.path.getsize(file_path)
                    except FileNotFoundError:
                        print(f"File not found: {file_path}")
                    except OSError as e:
                        print(f"OS error: {e}")
        except Exception as e:
            print(f"Error walking directory {path}: {e}")
    else:
        name = ""
        size = 0
        dir_path = ""

    return pd.Series([name, size, dir_path], index=['name', 'size', 'dir'])


def calc_byte(value):
    byte_str = ['','K','M','G','T']
    for i in range(5):
        if value < 1000:
            return str(value) + byte_str[i]
        value = value//1000
    else:
        print('max count')
        return str(value) + byte_str[i]


def _test_main():
    device_name = 'BACKUP5'
    start_time = datetime.datetime.now()
    print('start_time = {}'.format(start_time))
    path = r'I:'
    # Windowsパスのリスト
    paths = glob.glob(str(path) + '/**/*', recursive=True)
    
    # DataFrameに変換
    df = pd.DataFrame(paths, columns=['path'])

    # 各pathに対して情報を抽出
    df[['name', 'size', 'dir']] = df['path'].apply(extract_info)

    print('base  df.shape={}'.format(df.shape[0]))
    #/
    ignore_end_list = [
        '.JPG', '.jpg', '.jepg','.url', '.txt', '.dll', '.xml', '.exe'
        ,'.htm', '.html', '.lnk', '.eml', '.ini', '.dat', '.DAT'
    ]
    ignore_folder_list = [
        r'\Utility', r'\ZProgram', r'\Bkup', r'\bkup',]
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

    # 結果を表示
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

if __name__ == '__main__':
    print('\n*****')
    _test_main()