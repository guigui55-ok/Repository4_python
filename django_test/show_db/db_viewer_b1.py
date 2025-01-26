
"""
dJangoプロジェクト内のsqliteのファイルから、DBの内容を参照する

b2を参照
"""

# db_viewer.py
import os
import django

from pathlib import Path
import sys
# プロジェクトのルートフォルダをパスに追加
# path = os.path.dirname(os.path.abspath(__file__))
target_path = Path(r"C:\Users\OK\source\repos\Repository4_python\django_test")
sys.path.append(str(target_path))  # このスクリプトのフォルダ
print("sys.path.append = {}".format(target_path))

target_path = target_path.joinpath("login_sys_a")
sys.path.append(str(target_path))  # このスクリプトのフォルダ
print("sys.path.append = {}".format(target_path))


# Djangoプロジェクトの設定を読み込む
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  # プロジェクト名を適宜置き換え

# Djangoを初期化
django.setup()

from login_sys_a.accounts.models import Book  # アプリ名とモデル名を適宜置き換え

def display_all_data():
    """データベースの全データを表示"""
    try:
        # モデルから全データを取得
        books = Book.objects.all()
        for book in books:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Published Date: {book.published_date}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    display_all_data()
