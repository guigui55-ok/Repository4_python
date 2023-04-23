


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/test_main")
def test_main():
    return render_template("index.html", name="World")

if __name__ == "__main__":
    app.run()
"""
url
http://localhost:5000/test_main


このコードでは、render_template関数を使用して、index.htmlテンプレートをレンダリングし、name変数を World に設定しています。つまり、ページヘッダーに "Hello World!" という文字列が表示されます。

アプリケーションを起動し、http://localhost:5000/test_main にアクセスすると、テンプレートのHTMLが表示され、ページヘッダーに "Hello World!" という文字列が表示されます。name変数の値を変更することで、動的にページのヘッダーを変更できます。

"""