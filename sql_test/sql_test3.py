
"""
pip install pyodbc


"""

def main():
    import pandas as pd
    import pyodbc
    cnxn_str = r'Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename="C:\ZMyFolder\after to base\database\URLShortCut.mdf";Integrated Security=True;Connect Timeout=30'
    cnxn = pyodbc.connect(cnxn_str)
    df = pd.read_sql("SELECT * FROM *", cnxn)

def main2():
    #https://rnakamine.hatenablog.com/entry/2020/09/20/223424
    import pandas as pd
    path = r'C:\ZMyFolder\after to base\database\URLShortCut.mdf'
    df = pd.read_csv(path)
    print(df)
    #UnicodeDecodeError: 'utf-8' codec can't decode byte 0x99 in position 30: invalid start byte
main()

def main1():
    import pandas as pd
    import pyodbc
    cnxn_str = (
        r'DRIVER=ODBC Driver 11 for SQL Server;'
        r'SERVER=(local)\SQLEXPRESS;'
        r'Trusted_Connection=yes;'
        r'AttachDbFileName=C:\ZMyFolder\after to base\database\URLShortCut.mdf;'
    )
    cnxn = pyodbc.connect(cnxn_str)
    df = pd.read_sql("SELECT * FROM *", cnxn)