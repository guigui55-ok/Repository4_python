"""
https://stackoverflow.com/questions/46045834/pyodbc-data-source-name-not-found-and-no-default-driver-specified



"""
from sqlite3 import Row
import pyodbc 

constr = 'Driver = {SQL Server};Server=SIWSQL43A\SIMSSPROD43A;Database=CSM_reporting;Trusted_Connection=yes;'
# connection = pyodbc.connect(constr)

constr = '"DRIVER={{SQL Server}};"'
constr = 'DRIVER={{SQL Server}};'
constr = 'DRIVER={SQL Server};'

constr = (
    'DRIVER={SQL Server};'
    r'SERVER=(LocalDB)\MSSQLLocalDB;'
    r'Trusted_Connection=yes;'
    r'AttachDbFileName=C:\ZMyFolder\after to base\database\URLShortCut.mdf;'
)


def print_rows(rows:Row):
    # for key in rows.keys():
    #     print(key)
    # AttributeError: 'pyodbc.Row' object has no attribute 'keys'
    for buf in rows:
        print(buf)

"""
https://resanaplaza.com/2021/09/07/%E3%80%90-python-%E3%80%91pyodbc%E3%81%A7sqlserver%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%97%E3%82%88%E3%81%86%EF%BC%81/#SQLServer

https://memo.morelents.com/table-list-sql/
sql server
"""

import pprint
from sqlite3.dbapi2 import Row  

# C:\Users\OK\.vscode\extensions\ms-python.vscode-pylance-2022.6.10\dist\typeshed-fallback\stdlib\sqlite3\dbapi2.pyi

constr = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=(LocalDB)\MSSQLLocalDB;'
    r'Trusted_Connection=yes;'
    r'AttachDbFileName=C:\ZMyFolder\after to base\database\URLShortCut.mdf;'
)
print()
print(constr)
print()
print('###########')
# DBに接続
connection = pyodbc.connect(constr)
# カーソルの取得
cursor = connection.cursor()
# SQLの実行
# sql = r'SHOW TABLES' #ERR
# sql = r'SELECT *' #ERR
# sql = 'SELECT * FROM DBA_TABLES ORDER BY OWNER,TABLE_NAME' #ERR
sql = 'select * from sys.objects;'
# ユーザーテーブル一覧を取得 
# rows = ('MainTable', )
sql = "SELECT NAME FROM SYS.SYSOBJECTS WHERE XTYPE = 'U' ORDER BY NAME;" 
# テーブル名を指定して列の一覧を取得する
sql = """SELECT *
FROM   sys.columns
WHERE  object_id = (SELECT object_id
                    FROM   sys.tables
                    WHERE  name = 'MainTable'
                    )"""
# カタログテーブル（sys.columns）から取得する
# sql = "SELECT * FROM   sys.columns"
import sql_util.sql_const as const
# テーブルの列情報 Table
# sql = const.TABLE_COLUMN_BASIC_INFOS.replace(const.REPLACE_TABLE_NAMES,"('Table')")
# テーブルの列情報 MainTable
sql = const.TABLE_COLUMN_BASIC_INFOS.replace(const.REPLACE_TABLE_NAMES,"('MainTable')")


# データベースのテーブル情報を取得する
# sql = const.GET_ALL_INDEX_FROM_DB
# table_name = "('Table')"
# table_name = "Table" #pyodbc.ProgrammingError: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Incorrect syntax near the keyword 'Table'. (156) (SQLExecDirectW)")

#レコード数を取得する
# table_name = "MainTable"
# sql = const.GET_RECORD_COUNT_WITH_COLUMN_NAME.replace(const.REPLACE_TABLE_NAME,table_name)
# sql = sql.replace(const.REPLACE_COLUMN_NAME,'Id')
# ### sql = const.GET_RECORD_COUNT.replace(const.REPLACE_TABLE_NAME,"Table") #例外が発生しました: ProgrammingError ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Incorrect syntax near the keyword 'Table'. (156) (SQLExecDirectW)")

# 日付以降を取得
# date = '2022-06-10 14:00:00'
# date = '2022-05-20'
# table_name = "MainTable"
# columna_name = "Date"
# sql = const.GET_AFTER_DATE.replace(const.REPLACE_TABLE_NAME,table_name)
# sql = sql.replace(const.REPLACE_COLUMN_NAME,columna_name)
# sql = sql.replace(const.REPLACE_DATE_VALUE,date)

# 値に合致したものを取得
# url = r'https://www.youtube.com/watch?v='
# # col_name_url = 'URL'
# # sql = "SELECT * FROM {} WHERE {} = '{}';".format(table_name,col_name_url,url)
# columna_name = "URL"
# sql = const.GET_MATCH_VALUE.replace(const.REPLACE_TABLE_NAME,table_name)
# sql = sql.replace(const.REPLACE_COLUMN_NAME,columna_name)
# sql = sql.replace(const.REPLACE_DATE_VALUE,url)

print('sql='+sql)

# sql = "SELECT * FROM MainTable WHERE MainTable." + columna_name + " LIKE '{}'".format(url)
cursor.execute(sql)
# 結果の取得
# ret = cursor.fetchall()
rows = cursor.fetchall()
# output
# print(ret)
# c:\Users\OK\source\repos\Repository4_python\sql_test\sql_test7.py:50: DeprecationWarning: PyUnicode_FromUnicode(NULL, size) is deprecated; use PyUnicode_New() instead
# print だとエラーが出る
for row in rows:
    pprint.pprint(row)
# for row in rows:
#     # pprint.pprint( row )
#     print(type(rows))
#     for data in row:
#         print(data)
#         print(type(data))
#         # for buf in data:
#         #     print(buf)

print()
print('sql='+sql)
print('len(rows) = {}'.format(len(rows)))
# print_rows(rows)
# カーソルを閉じる
cursor.close()
# print(connection)
# 接続を閉じる
connection.close()
