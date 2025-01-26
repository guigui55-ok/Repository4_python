"""
dJangoプロジェクト内のsqliteのファイルから、DBの内容を参照する
"""

import sqlite3

class DatabaseHandler:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_all_tables(self):
        """データベース内のテーブル名一覧を取得"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()
            return [table[0] for table in tables]
        except sqlite3.Error as e:
            print(f"SQLite エラーが発生しました: {e}")
            return []
        finally:
            if conn:
                conn.close()

    def get_columns_of_table(self, table_name):
        """指定されたテーブルのカラム名一覧を取得"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            return [column[1] for column in columns]  # カラム名は2番目のフィールド
        except sqlite3.Error as e:
            print(f"SQLite エラーが発生しました: {e}")
            return []
        finally:
            if conn:
                conn.close()

    def get_sample_data(self):
        """例: booksテーブルの全データを取得"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            query = "SELECT account_id, email, first_name, last_name FROM accounts_user"
            cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"SQLite エラーが発生しました: {e}")
            return []
        finally:
            if conn:
                conn.close()

if __name__ == "__main__":
    db_path = r"C:\Users\OK\source\repos\Repository4_python\django_test\login_sys_a\db.sqlite3"
    db_handler = DatabaseHandler(db_path)

    # 1. テーブル名一覧を取得して表示
    print("=== テーブル名一覧 ===")
    tables = db_handler.get_all_tables()
    for table in tables:
        print(table)

    # 2. 各テーブルのカラム名一覧を取得して表示
    print("\n=== カラム名一覧 ===")
    for table in tables:
        print(f"テーブル: {table}")
        columns = db_handler.get_columns_of_table(table)
        print(f"カラム: {', '.join(columns)}")

    # 3. booksテーブルのデータを取得して表示（例）
    print("\n=== Users テーブルのデータ ===")
    row_list = db_handler.get_sample_data()
    for row_val in row_list:
        print(f"ID: {row_val[0]}, r1: {row_val[1]}, r2: {row_val[2]}, r3: {row_val[3]}")
