"""
https://docs.microsoft.com/ja-jp/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver16

"""


import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
# server = 'tcp:myserver.database.windows.net' 
# database = 'mydb' 
# username = 'myusername' 
# password = 'mypassword' 
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()

con_str = r'Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename="C:\ZMyFolder\after to base\database\URLShortCut.mdf";Integrated Security=True;Connect Timeout=30'
 
con_str = r'Data Source=(LocalDB)\SQLEXPRESS;AttachDbFilename="C:\ZMyFolder\after to base\database\URLShortCut.mdf";Integrated Security=True;Connect Timeout=30'
con_str = r"Data Source=(LocalDb)\MSSQLLocalDB;"
cnxn = pyodbc.connect(con_str)
cursor = cnxn.cursor()