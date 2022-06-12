"""
https://stackoverflow.com/questions/46045834/pyodbc-data-source-name-not-found-and-no-default-driver-specified
"""

from multiprocessing import connection
import pyodbc
import pprint
from sqlite3.dbapi2 import Row

if __name__ == '__main__':
    from get_url_lnk_for_mdf import MovieLinkInfo
    import sql_util.sql_const as const
else:
    from sql_test.get_url_lnk_for_mdf import MovieLinkInfo
    import sql_test.sql_util.sql_const as const

def print_rows(rows:Row):
    # for key in rows.keys():
    #     print(key)
    # AttributeError: 'pyodbc.Row' object has no attribute 'keys'
    for buf in rows:
        print(buf)

TARGET_TABLE_NAME = 'MainTable'
COLUMN_NAME_DATE = 'Date'
COLUMN_NAME_URL = 'URL'
COLUMN_NAME_REGISTER_TIMES = 'RegistTimes'

class PySqlMode():
    INSERT = 1
    DELETE = 2
    UPDATE = 3

class PySql():
    def __init__(self,connection_str:str='') -> None:

        self.connection_str = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=(LocalDB)\MSSQLLocalDB;'
        r'Trusted_Connection=yes;'
        r'AttachDbFileName=C:\ZMyFolder\after to base\database\URLShortCut.mdf;')
        if connection_str != '':
            self.connection_str = connection_str
        self.cursor = None
        self.rows = None
        self.current_row = 0
        self.sql = ''

    def excute(self,sql:str=''):
        if sql == '': sql = self.sql
        # DBに接続
        # カーソルの取得
        self.connection = pyodbc.connect(self.connection_str)
        self.cursor = self.connection.cursor()
        self.cursor.execute(sql)
        # SQLの実行
        if self.cursor.description != None:
            # 結果の取得
            self.rows = self.cursor.fetchall()
        else:
            self.rows = None
            self.rows = []
        if sql.find('UPDATE')>=0 \
            or sql.find('DELETE')>=0 \
            or sql.find('INSERT')>=0:
            self.connection.commit()
        # カーソルを閉じる
        self.cursor.close()
        # 接続を閉じる
        self.connection.close()
        self.cursor = None
        self.connection = None
    
    def get_record_count(self,table_name:str):
        print()
        print('***** get_record_count')
        # sql = 'EXEC sp_spaceused [{}]'.format(table_name)
        sql = 'EXEC sp_spaceused {}'.format(table_name)
        # sql = 'SELECT count(Id) as [rows_count] FROM [{}]'.format(table_name)
        # sql = 'SELECT count(*) as [rows_count] FROM [{}]'.format(table_name)
        # DBに接続
        connection = pyodbc.connect(self.connection_str)
        # カーソルの取得
        cursor = connection.cursor()
        # SQLの実行
        cursor.execute(sql)
        # 結果の取得
        # if cursor.description != None:
        #     print('* cursor.description')
        #     print(cursor.description)
        rows = cursor.fetchall()
        # 出力
        for row in rows:
            pprint.pprint(row)
            count = int(row[1])
        print('record_count = {}'.format(count))
        # カーソルを閉じる
        cursor.close()
        # 接続を閉じる
        connection.close()
        cursor = None
        connection = None
        print()
        return count

    def get_max_id(self,table_name:str):
        """"
        IDの最大値を取得する。
         列名は「Id」を指定している。
        """
        sql = 'SELECT MAX(Id) FROM {};'.format(table_name)
        rows = self.get_rows(sql)
        for row in rows:
            max = int(row[0])
        return max

    def is_exists_data_single(self,table_name:str,column_name:str,data:str):
        sql = const.GET_MATCH_VALUE
        sql = sql.replace(const.REPLACE_TABLE_NAME,table_name)
        sql = sql.replace(const.REPLACE_COLUMN_NAME,column_name)
        sql = sql.replace(const.REPLACE_DATE_VALUE,data)
        rows = self.get_rows(sql)
        # for row in rows:
        #     max = int(row[0])
        # return max
        if len(rows)>0:
            return True
        return False

    def get_rows(self,sql:str):
        print()
        print('***** get_result')
        # DBに接続
        connection = pyodbc.connect(self.connection_str)
        # カーソルの取得
        cursor = connection.cursor()
        # SQLの実行
        cursor.execute(sql)
        # 結果の取得
        # if cursor.description != None:
        #     print('* cursor.description')
        #     print(cursor.description)
        rows = cursor.fetchall()
        # 出力
        for row in rows:
            pprint.pprint(row)
        # カーソルを閉じる
        cursor.close()
        # 接続を閉じる
        connection.close()
        cursor = None
        connection = None
        return rows
    
    
    def get_row_as_list(self,get_count:int=-1):
        if get_count >= 0: target = get_count
        else: target = self.current_row
        count = 0
        ret_list = []
        for row in self.rows:
            if count == target:
                return self.get_values_from_row(row)
        return ret_list
    
    def get_next_row_as_list(self):
        if self.current_row<0: self.current_row=0
        self.current_row += 1
        return self.get_row_as_list(self.current_row)
    
    def get_values_from_row(self,row:Row):
        ret_list = []
        for buf in row:
            ret_list.append(buf)
            return ret_list
        return ret_list
    
    def close(self):
        if self.cursor!=None:
            # カーソルを閉じる
            self.cursor.close()
            self.cursor = None
        if self.connection!=None:
            # 接続を閉じる
            self.connection.close()
            self.connection = None

################################################################################
################################################################################
################################################################################

def get_info_from_path(path:str):
    info = info_getter.MovieLinkInfo()
    import os
    if not os.path.exists(path):
        print('\npath not exists, path={}'.format(path))
        return
    info.set_info_from_path(path)
    return info

def update_times(info:MovieLinkInfo):
    print()
    print('update_times')
    print('info.regist_times = {} + 1'.format(info.regist_times))
    info.regist_times += 1
    pysql = PySql()
    sql = const.UPDATE_VALUE
    sql = sql.replace(const.REPLACE_TABLE_NAME,TARGET_TABLE_NAME)
    sql = sql.replace(const.REPLACE_SET_COLUMN_NAME,COLUMN_NAME_REGISTER_TIMES)
    sql = sql.replace(const.REPLACE_SET_DATA_VALUE,str(info.regist_times))
    sql = sql.replace(const.REPLACE_WHRER_COLUMN_NAME,COLUMN_NAME_URL)
    sql = sql.replace(const.REPLACE_WHRER_DATA_VALUE,info.url)
    pysql.excute(sql)
    print('update len(rows) =' + str( len(pysql.rows) ))
    return

################################################################################
def insert_data(info:MovieLinkInfo):
    print()
    print('insert_data')
    print('info.file_name = {} + 1'.format(info.file_name))

    pysql = PySql()
    # info.id = pysql.get_record_count(TARGET_TABLE_NAME) + 1
    info.id = pysql.get_max_id(TARGET_TABLE_NAME) + 1
    sql = info.get_sql_for_insert(TARGET_TABLE_NAME)
    pysql.excute(sql)
    print('insert len(rows) =' + str( len(pysql.rows) ))
    return
################################################################################
def is_exists_data_in_db(path):
    pysql = PySql()
    info = get_info_from_path(path)
    flag = pysql.is_exists_data_single(TARGET_TABLE_NAME,COLUMN_NAME_URL,info.url)
    return flag

################################################################################
################################################################################
################################################################################
if __name__ == '___main__':
    import get_url_lnk_for_mdf as info_getter
else:
    import sql_test.get_url_lnk_for_mdf as info_getter
def resist_data_to_mdf_from_url_file(path:str):
    """
    .lnkファイルのURLがmdfに登録されているか確認して
     登録されていたら RegisterTimes を１つ加算してDBを更新
      登録されていなかったら、新たにURLを登録する。
       DBファイルはローカルのものを使用（この関数内で指定している）
    """
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
    import os
    info = info_getter.MovieLinkInfo()
    if not os.path.exists(path):
        print('\npath not exists, path={}'.format(path))
        return
    info.set_info_from_path(path)


    # DBに接続
    connection = pyodbc.connect(constr)
    # カーソルの取得
    cursor = connection.cursor()
    # SQLの実行
    # この日付以降のデータを取得する
    # date = info.get_date_str()
    # table_name = TARGET_TABLE_NAME
    # columna_name = COLUMN_NAME_DATE
    # sql = const.GET_AFTER_DATE.replace(const.REPLACE_TABLE_NAME,table_name)
    # sql = sql.replace(const.REPLACE_COLUMN_NAME,columna_name)
    # sql = sql.replace(const.REPLACE_DATE_VALUE,date)

    # URL列のデータが合致したレコードを取得する
    url = info.url
    table_name = TARGET_TABLE_NAME
    columna_name = COLUMN_NAME_URL
    sql = const.GET_MATCH_VALUE.replace(const.REPLACE_TABLE_NAME,table_name)
    sql = sql.replace(const.REPLACE_COLUMN_NAME,columna_name)
    sql = sql.replace(const.REPLACE_DATE_VALUE,url)
    print('sql='+sql)

    cursor.execute(sql)
    # 結果の取得
    rows = cursor.fetchall()

    # for i in range(len(rows)):
    #     row = rows[i]
        
    # カーソルを閉じる
    cursor.close()
    # 接続を閉じる
    connection.close()

    if len(rows)>0:
        buf_list = []
        for row in rows:
            pprint.pprint(row)
            if len(buf_list)<1:
                for row_el in row:
                    buf_list.append(row_el)
        try:
            info_get = MovieLinkInfo(buf_list)
            info_get.print_data()
        except Exception as e:
            print(str(e))
            print('######## ERROR ########')
            import traceback
            traceback.print_exc()
            print('####################')
    else:
        pass #len(rows)<1

    print()
    print('sql='+sql)
    print('len(rows) = {}'.format(len(rows)))
    is_exists = False
    if len(rows)>0:
        is_exists = True
    
    if is_exists:
        update_times(info_get)
    else:
        # insert_data(info)
        pass
        # ダウンロードが成功した後に登録する
    return is_exists

def regist_url_when_success_download(path:str):
    info = get_info_from_path(path)
    insert_data(info)
    return True


def main():
    path = r'C:\ZMyFolder\newDoc\新しいfiles\0528 you\sumi\.url'
    path = r'C:\ZMyFolder\newDoc\新しいfiles\0528 you\sumi\.url'
    resist_data_to_mdf_from_url_file(path)

if __name__ == '__main__':
    main()

