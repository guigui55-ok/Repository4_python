"""
pip install MySQL-Python

https://uxmilk.jp/23509
NG


pip install mysqlclient
https://www.sejuku.net/blog/82657

"""


import MySQLdb
 
# DBに接続しカーソルを取得する
connect = MySQLdb.connect(
    host='localhost', 
    port=3306, 
    user='test', 
    passwd='pass' , 
    user='testuser', 
    db='sample', 
    charset='utf8')
cursor = connect.cursor()
 
#レコードの挿入
sql = "insert into fruits values('apple', '100yen')"
cursor.execute(sql) # 1つ目のレコードを挿入
sql = "insert into fruits values('orange', '150yen')"
cursor.execute(sql) # 2つ目のレコードを挿入
 
connect.commit()    # コミットする
 
cursor.close()
connect.close()     # データベースオジェクトを閉じる