import zipfile

def _test():
    # ZIPファイルを開く
    with zipfile.ZipFile('path_to_zip_file.zip', 'r') as zip_ref:
        # ZIPファイル内のファイル名リストを取得
        for file_name in zip_ref.namelist():
            # ファイルをバイナリモードで開く
            with zip_ref.open(file_name, 'r') as file:
                # ファイル内容をバイナリデータとして読み込む
                binary_data = file.read()
                # バイナリデータを適切に扱う（保存や処理）
                with open('output_directory/' + file_name, 'wb') as out_file:
                    out_file.write(binary_data)


def unzip_file(read_zip_file_path, save_file_dir_path):
    import zipfile
    # ZIPファイルを開く
    with zipfile.ZipFile(read_zip_file_path, 'r') as zip_ref:
        # ZIPファイル内のファイル名リストを取得
        for file_name in zip_ref.namelist():
            # ファイルをバイナリモードで開く
            with zip_ref.open(file_name, 'r') as file:
                # ファイル内容をバイナリデータとして読み込む
                binary_data = file.read()
                # バイナリデータを適切に扱う（保存や処理）
                with open(save_file_dir_path + file_name, 'wb') as out_file:
                    out_file.write(binary_data)