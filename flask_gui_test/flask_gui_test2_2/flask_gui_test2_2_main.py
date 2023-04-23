"""
上記のHTMLを以下のように変更して、また、ボタンクリックにより以下のバックエンド処理を行うようにソースを変更してください。
****
・HTMLのフロントエンド

Htmlタイトル：Test Flask GUI1

「フォルダ名」とラベルのついた、インプットボックスを１つ（フォルダパスを表示するので、横幅は長め）
フォルダ名にブラウザの外からフォルダをドラッグアンドドロップしたら、フォルダ名が入力されるようにしてください。
「モード」とラベルの付いた、インプットボックスを１つ（1桁、2桁の数値を表示するので、幅は短め）
モードの初期値は「１」としてください。
「実行結果ログ」とラベルの付いた、テキストエリアを1つ（実行結果の詳細を表示するので横幅は長く、縦幅も適度に長くしてください）
「実行」ボタン

****
・HTMLのバックエンド
ボタンクリック後の処理について:
実行をクリックすると、サーバーのバックグラウンドで処理を行います。
実行する関数は test_flask_gui_main です。
上記のフォルダ名とモードをdict形式にして、引数に渡してください。

実行モードを定数クラスにして以下のように定義します。
　テストモード：1

test_flask_gui_main の処理内容は以下の通りです。
*取得したモードを設定して、ログに出力します。
（あらかじめ設定されたモードに合致しない場合はエラーとする）
*ディレクトリパスを設定して、ログに出力します。
*ディレクトリ名のみを取得して、ログに出力します。
*モードの正常終了をログに出力します。
*returnします

ログを記録した場合は、あとで「実行結果ログ」に出力します。
　（出力する順番は新しいものが一番上に表示されるようにします）
「実行結果ログ」に出力した後、保持しているログはすべて消去します。
エラーが発生した場合はその内容をログに残し処理を中断します。

"""
from flask import Flask, render_template, request

app = Flask(__name__)

class Mode:
    TEST = 1

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/execute", methods=["POST"])
def execute():
    folder_input = request.form["folderInput"]
    mode_input = int(request.form["modeInput"])

    if mode_input == Mode.TEST:
        log = f"モード {mode_input} が正常に実行されました。"
    else:
        log = f"エラー：モード {mode_input} が見つかりませんでした。"

    try:
        folder_path = "./" + folder_input
        log += f"\nフォルダパス：{folder_path}"
        folder_name = folder_input.split("/")[-1]
        log += f"\nフォルダ名：{folder_name}"
    except Exception as e:
        log += f"\nエラー：{str(e)}"
    
    log += "\n"
    app.logger.info(log)

    return render_template("index.html", log=log)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()