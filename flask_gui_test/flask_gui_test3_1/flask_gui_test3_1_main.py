"""

http://localhost:5000/
http://127.0.0.1:5000/
"""
# https://qiita.com/xu1718191411/items/96dda3d6cf2ab11ae1b3
import sys
from pathlib import Path
path_str = str(Path(__file__).parent)
print(path_str)
sys.path.append(path_str)


from flask import Flask, render_template, request

app = Flask(__name__)
print(__name__)

class Mode:
    TEST = 1

@app.route("/")
def index():
    return render_template("index.html")

import os

@app.route("/execute", methods=["POST"])
def execute():
    folder_input = request.form["folderInput"]
    mode_input = int(request.form["modeInput"])

    if mode_input == Mode.TEST:
        log = f"モード {mode_input} が正常に実行されました。"
    else:
        log = f"エラー：モード {mode_input} が見つかりませんでした。"

    try:
        log += f"\nフォルダパス：{folder_input}"
        # folder_name = folder_input.split("/")[-1]
        folder_name = os.path.basename(folder_input)
        log += f"\nフォルダ名：{folder_name}"
    except Exception as e:
        log += f"\nエラー：{str(e)}"
    
    log += "\n"
    app.logger.info(log)

    return render_template("index.html", log=log)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()