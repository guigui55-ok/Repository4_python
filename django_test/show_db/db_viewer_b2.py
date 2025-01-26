
"""
dJangoプロジェクト内のsqliteのファイルから、DBの内容を参照する

-----
djangoプロジェクト読み込み
プロジェクト内のmodelモジュール読み込み
djangoプロジェクト内のvenvのactivate実行
が必要

"""

import os
import django
import sys
from pathlib import Path

print("\n ****** ")
# プロジェクトのルートフォルダをパスに追加
BASE_DIR = Path(__file__).resolve().parent.parent  # プロジェクトルート
sys.path.append(str(BASE_DIR))
print(f"sys.path.append = {BASE_DIR}")


PROJECT_DIR = Path(__file__).resolve().parent.parent.joinpath("login_sys_a")  # プロジェクトルート
sys.path.append(str(PROJECT_DIR))
print(f"sys.path.append = {PROJECT_DIR}")

# Djangoプロジェクトの設定を読み込む
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  # プロジェクト名を適宜変更

# Djangoを初期化
django.setup()

# モデルをインポート
from accounts.models import User  # アプリ名とモデル名を適宜変更

def display_all_data():
    """データベースの全データを表示"""
    try:
        # モデルから全データを取得
        objects = User.objects.all()
        for object in objects:
            print(f"ID: {object.account_id}, mail: {object.email}, fName: {object.first_name}, lName: {object.last_name}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    display_all_data()


'''
実行方法
仮想環境をアクティブ化します。

bash
コピーする
編集する
path\to\venv\Scripts\activate
スクリプトを実行します。

bash
コピーする
編集する
python path\to\db_viewer.py
'''