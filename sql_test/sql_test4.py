import pyodbc
import contextlib

con_str = r'Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename="C:\ZMyFolder\after to base\database\URLShortCut.mdf";Integrated Security=True;Connect Timeout=30'
with contextlib.closing(pyodbc.connect(
    f"DRIVER={{SQL Server}};"+con_str)) as cnxn:
    with contextlib.closing(cnxn.cursor()) as cursor:
        print(cursor.execute("select @@version;").fetchone())