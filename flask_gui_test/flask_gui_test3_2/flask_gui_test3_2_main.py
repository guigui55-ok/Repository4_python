"""

http://localhost:5000/
http://127.0.0.1:5000/
"""
# C:\Users\Users\source\repos\Repository4_python\flask_gui_test\flask_gui_test2_2\templates
# https://qiita.com/xu1718191411/items/96dda3d6cf2ab11ae1b3
import sys
from pathlib import Path
path_str = str(Path(__file__).parent)
print(path_str)
sys.path.append(path_str)
###
path_str = str(Path(__file__).parent.parent)
print(path_str)
sys.path.append(path_str)
from flask_simple_logger import FlaskSimpleLogger
g_logger = FlaskSimpleLogger()
###

from flask import Flask, render_template, request

app = Flask(__name__)
print(__name__)

# class Mode:
#     TEST = 1
import background
from background import main_method
from background.main_method import ConstBackground

@app.route("/")
def index():
    return render_template("index.html")

import os

@app.route("/execute", methods=["POST"])
def execute():
    ###
    folder_input = request.form["folderInput"]
    mode_input = int(request.form["modeInput"])
    option = {}
    option.update({'folder_input':folder_input})
    option.update({'mode_input':mode_input})
    ###
    global g_logger
    option.update({'logger':g_logger})
    ### Excute Main
    option = main_method.execute_main(option)
    ###
    g_logger = main_method.add_annotation_type_logger(option[
        ConstBackground.KEY_LOGGER])
    log = g_logger.get_log_str()
    app.logger.info(log)

    return render_template("index.html", log=log)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()