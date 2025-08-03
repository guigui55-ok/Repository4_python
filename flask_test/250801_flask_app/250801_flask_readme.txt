Flask WebAPI 学習用アプリ README

1️⃣ プロジェクト概要
このプロジェクトは、Flaskを使ったWebAPIの学習を目的としたシンプルなアプリケーションです。
以下の機能を提供します。

/test：API接続テスト
/endpoints：提供中のエンドポイント一覧を取得
/echo：POSTしたJSONデータをそのまま返す（エコー）

また、これらのAPIをブラウザから呼び出せる簡易HTMLページ（index.html）を提供しています。

2️⃣ 前提条件
OS: Windows 10 以降 (macOS, Linux でも可)
Python: 3.9以上推奨（3.13まで対応確認済み）
pip が利用可能であること

3️⃣ セットアップ手順
① プロジェクトのフォルダ構成
flask_webapi_test/
├─ flask_test_app_250801.py
├─ templates/
│   └─ index.html
└─ README.md  (このファイル)

② 仮想環境の作成（任意）
Pythonの仮想環境を作成することを推奨します。
python -m venv venv

仮想環境を有効化:
Windows:
venv\Scripts\activate
macOS/Linux:
source venv/bin/activate

③ 必要ライブラリのインストール
以下のコマンドで必要なパッケージをインストールします。
pip install flask flask-cors

4️⃣ アプリの起動
以下のコマンドを実行します。
python flask_test_app_250801.py
起動に成功すると以下のようなメッセージが表示されます。
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

5️⃣ 動作確認方法
ブラウザで以下にアクセスしてください。
http://localhost:5000/
ページが表示されたら、以下を確認できます。

アクセステストAPI
「実行」ボタンを押すと、{"message": "API接続成功"} が表示されます。

エンドポイント一覧取得API
「実行」ボタンを押すと、利用可能なエンドポイントのリストが表示されます。

JSONエコーAPI
テキストエリアにJSONを入力し、「実行」を押すと送信データが返されます。

6️⃣ APIをcurlで確認する場合
コマンドプロンプトまたはターミナルから以下を実行できます。

接続テスト
curl http://localhost:5000/test

エンドポイント一覧取得
curl http://localhost:5000/endpoints

JSONエコー
curl -X POST http://localhost:5000/echo \
-H "Content-Type: application/json" \
-d '{"name":"Taro","age":30}'

7️⃣ 終了方法
サーバーを停止するには、ターミナルで CTRL + C を押してください。

8️⃣ 補足
デバッグモードを有効にすると、ソースコードを変更した際に自動リロードされます。

本アプリは学習用のため、認証機能やデータベースは実装していません。