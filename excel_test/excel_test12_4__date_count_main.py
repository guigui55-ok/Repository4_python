"""
表Aの日付データの出現回数をカウントして、 表Bに入力していく。
 コードを整理済み

特定の日付を含むエクセル表A（列名：表番号、カテゴリA(日付)、カテゴリB(日付)）の日付をカウントしてdf_aとして読み込む。（データはセル値と番地を紐づけている）
 ある範囲の日付データと結果（columns=日付、結果）をdf_retにする
  日付と結果を列名に持つエクセルの表B（上記ret_dfと同じ）をdf_bとして読み込む。（データはセル値と番地を紐づけている）
    （df_bとdf_ret日付は異なっていてもよい） 
"""



from excel_data import ExcelSheetDataUtil
import excel_data
from pathlib import Path
import pandas as pd


# print('*書き込みシートをすべてクリア')
file_name = 'myworkbook.xlsx'
sheet_name = '日付Count'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=True)


print('*コピー元表Aの範囲を読み込み')
sheet_name = '日付Count'
ex_data.set_sheet(sheet_name)
keyword = '行番号'
ex_data.set_address_by_find(keyword, 'A1', 'I50', debug=False)
print('begin_address = {}'.format(ex_data.cell.coordinate))
ex_data.move_address(0,0)
ex_data.range_address = ex_data.get_range_address()
print('range_address = {}'.format(ex_data.range_address))
df_a = ex_data.get_values_from_range_address_pd(ex_data.range_address, columns=None)
print('df_a = ')
first_row_as_list = df_a.iloc[0].astype(str).tolist()
df_a.columns = first_row_as_list
print(df_a.columns)
print(df_a.shape)

print('*処理する日付のリストを作成（指定の日付から月末まで）')
import datetime
print(datetime.datetime.now().strftime('%Y-%m-%d'))
BEGIN_DATE = '2024-01-15'
begin_datetime = datetime.datetime.strptime(BEGIN_DATE, '%Y-%m-%d')
import calendar
y = begin_datetime.year
m = begin_datetime.month
d = calendar.monthrange(y, m)[1]
END_DATE = '{}-{}-{}'.format(y, m, d)
end_datetime = datetime.datetime.strptime(END_DATE, '%Y-%m-%d')
date_range = pd.date_range(BEGIN_DATE, END_DATE, freq='D')
print('    begin_datetime = {}'.format(begin_datetime))
print('    end_datetime = {}'.format(end_datetime))

print('*エクセルから読み取った日付データリストを文字列に変換する')
from excel_data import cnv_date_str_cell, cnv_date_str, cnv_date_str_yobi_cell
# 表Aの日付の出現回数をカウントする列名
col_name_a = 'カテゴリA'
df_a[col_name_a] = df_a[col_name_a].map(cnv_date_str_cell)

print('*日付カウント格納用リストを用意する')
# 表Bの日付の列名（df_retとdf_bの日付と結果は同じ列名にする）
date_col_name = '日付'
df_ret = pd.DataFrame({date_col_name: date_range})
# 表Bの結果入力の列名（df_retとdf_bの日付と結果は同じ列名にする）
result_col_name = '結果数'
df_ret[result_col_name]=''
print('df_ret.head a')
print(df_ret.head())
print('-------')
print('*日付型を文字列に変換')
df_ret[date_col_name] = df_ret[date_col_name].map(cnv_date_str)


print('*特定の日付の出現回数をカウント')
print('*読み取った表Aから日付のdfに値をコピーする')
for date_val in date_range:
    target_date = date_val.strftime('%y/%m/%d')
    count = (df_a[col_name_a] == target_date).sum()
    # print('    {} [{}] = {}'.format(col_name_a, target_date ,count))
    print(str(count) +',' , end='')
    # buf_df = df_ret[df_ret[date_col_name] == target_date]
    buf_df = df_ret[df_ret[date_col_name].str.contains(target_date)]
    buf_df[result_col_name] = int(count)
    df_ret.update(buf_df)
print('')
# なぜか結果列の値が、float表示になるのでintに変換する（dtypes=object）
df_ret[result_col_name] = df_ret[result_col_name].astype('Int64')
print('df_ret.head b')
print(df_ret.head())
print(df_ret.dtypes)
print('-------')


print('*結果貼り付け用、日付表Bの範囲を読み込み')
# 表Bのシート名
sheet_name = '日付Count'
ex_data.set_sheet(sheet_name)
# 表Bの開始keyword
keyword = '日付'
ex_data.set_address_by_find(keyword, 'H5', 'I50', debug=False)
print('begin_address = {}'.format(ex_data.cell.coordinate))
ex_data.move_address(0,0)
ex_data.range_address = ex_data.get_range_address()
print('range_address = {}'.format(ex_data.range_address))
df_b = ex_data.get_values_from_range_address_pd(ex_data.range_address, columns=None)
print('df_b = ')
first_row_as_list = df_b.iloc[0].astype(str).tolist()
df_b.columns = first_row_as_list
print(df_b.columns)
print(df_b.shape)
print(df_b.head())
print('-------')

print('*日付カウント済みDFから、表Bにデータを入力していく')
print('df_bとdf_retは同じ想定')

from openpyxl.cell import Cell
df_b_str_cell:excel_data.StrCell=None
buf_cell:Cell=None
#結果の日付列をfor文で処理する
for i, df_ret_date in enumerate(df_ret[date_col_name]):
    if df_b_str_cell==date_col_name: continue#1行目はラベル名なので除外
    #日付データの書式などを処理するならここでする（値を処理するときはデバッグ用の別変数にする）（これは未処理）
    target_date = df_ret_date
    # df_retの今の日付の結果データを取得
    buf_df = df_ret[df_ret[date_col_name].str.contains(target_date)]
    count = buf_df[result_col_name]
    count = int(count)
    # 書き込み先の表Bの該当する日付のデータ（とCell）を取得する
    buf_df_b = df_b[df_b[date_col_name].str.contains(target_date)]
    if buf_df_b.shape[0]==0:
        print(' *nothing data(buf_df_b.shape={})'.format(buf_df_b.shape))
        print('[{}] -> {}, date={}'.format(
            None, count, target_date))
        continue
    #buf_df_bはDataFrame型が返る
    for index, row in buf_df_b.iterrows():
        row[result_col_name].cell.value = count
        print('[{}] -> {}, date={}'.format(
            row[result_col_name].cell.coordinate, count, target_date))

try:
    ex_data.save_book()
except PermissionError as e:
    msg = '[!]ERROR: ファイルアクセスエラーです。ファイルが開いていたらファイルを閉じてください。'
    print(msg)
    # raise e