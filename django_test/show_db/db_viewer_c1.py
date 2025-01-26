import sqlite3

def read_data_from_db(db_path):
    """SQLite データベースからデータを読み込む"""
    try:
        # データベースに接続
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # 任意のテーブル（例: User ）からデータを取得
        query = "SELECT account_id, email, first_name, last_name FROM User"
        cursor.execute(query)

        # データをフェッチして表示
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, row1: {row[1]}, row2: {row[2]}, row3: {row[3]}")

    except sqlite3.Error as e:
        print(f"SQLite エラーが発生しました: {e}")

    finally:
        # 接続を閉じる
        if conn:
            conn.close()

if __name__ == "__main__":
    # データベースファイルのパス（Django プロジェクトの設定などから取得）
    db_path = r"C:\Users\OK\source\repos\Repository4_python\django_test\login_sys_a\db.sqlite3"

    # データベースを直接読み込んで表示
    read_data_from_db(db_path)
