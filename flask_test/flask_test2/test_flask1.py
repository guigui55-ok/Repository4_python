#https://qiita.com/zaburo/items/5091041a5afb2a7dffc8

from flask import Flask, render_template,request,redirect
app = Flask(__name__)

# アップロード先のディレクトリ
UPLOAD_FOLDER = './uploads'
# アップロードされる拡張子の制限
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])
ALLOWED_EXTENSIONS = set([''])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/submit_top2')
def submit_top2():
    name = 'submit_top2.html'
    return render_template('submit_top2.html', title='Submit top', name=name)

@app.route('/submit_top')
def submit_top():
    name = 'submit_top.html'
    return render_template('submit_top.html', title='Submit top', name=name)

@app.route('/submit_result', methods=['POST','GET'])
def submit_result():
    name = 'submit_result.html'
    title = 'Submit Result'

    file_key_name = 'input_file'

    if request.method == 'POST':
        ### ファイルがなかった場合の処理、request からオブジェクト取得前
        if file_key_name not in request.files:
            # flash('ファイルがありません')
            print('ファイルがありません (1) [file not in request.files]')
            return redirect(request.url)
        ### データの取り出し
        # name属性を指定する
        file = request.files[file_key_name]
        # file_path = request.form['file_path'] # 文字列
        ### ファイル名がなかった時の処理、request からオブジェクト取得後
        if file.filename == '':
            # flash('ファイルがありません')
            print('ファイルがありません (2) [file = request.files[file]]')
            return redirect(request.url)

        
        ### ファイルのチェック        
        # ファイル名をチェックする関数
        from werkzeug.utils import secure_filename
        import os
        import test_flask_sub_module
        from flask import url_for

        # アップロードフォルダを設定する
        import pathlib
        # path = pathlib.Path(UPLOAD_FOLDER)
        path = pathlib.Path(__file__).parent
        path = os.path.join(str(path),'templates','uploads')
        save_file_path = path
        file_list_value = []
        try:

            app.config['UPLOAD_FOLDER'] = str(path)
            if file and test_flask_sub_module.allwed_file(file.filename):
                # 危険な文字を削除（サニタイズ処理）
                filename = secure_filename(file.filename)
                # ファイルの保存
                dir = app.config['UPLOAD_FOLDER']
                dst = os.path.join(dir,filename)
                file.save(dst)
                is_success = True
                error_message = ''
            else:
                is_success = False
                error_message = 'allwed_file Failed'
            ##
            import test_flask_sub_module
            # is_success,error_message = test_flask_sub_module.check_value_for_send_file(file_path)
            ### getFile List
            file_list_value = []
            file_list = os.listdir(save_file_path)
            # file_list_value = test_flask_sub_module.create_tag_li_ul(file_list,'')
            file_list_value = test_flask_sub_module.list_to_str(file_list)
            print()
            print('=======================')
            print('save_file_path = {}'.format(save_file_path))
            print('file_list_value = {}'.format(file_list_value))
            print('=======================')
            copy_dist = ''
        except Exception as e:
            is_success = False
            error_message = str(e)
            print('-------------------------')
            import traceback
            traceback.print_exc()
            print('-------------------------')
    else:
        print('not POST')
        is_success = False
        error_message = 'not request.method == POST'
        file_list_value = []


    # アップロード後のページに転送
    # return redirect(url_for('uploaded_file', filename=filename))
    return render_template(
        'submit_result.html',
         title=title,
         name=name,
         result=is_success,
         error_message=error_message,
         file_list_value=file_list_value
         )


@app.route('/')
def hello():
    name = "Hello Flask"
    return name

@app.route('/temp')
def temp():
    name = "temp"
    return render_template('submit_top.html', title='flask test', name=name) 


## 実行部
if __name__ == "__main__":
    # Flaskのマッピング情報を表示
    print(app.url_map)
    # app.run(debug=True,host='0.0.0.0',port=5000)
    app.run(debug=False)
    # 外部からアクセスしたい場合は '0.0.0.0'を指定無ければ、アクセスエラーとなる（flaskはエラーを出さない）