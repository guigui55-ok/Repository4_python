"""
pythonで新しいファイル名を作成する関数を出力してください。
引数はpath（ファイルパス）,sepaletor（区切り文字）とします。
処理は、以下の通りです。
まずpathが存在しないときはそのままpathをreturnします。
次に、pathからファイル名のみを取得してfile_nameに代入します。
file_nameの拡張子を除く最後の文字が「sepaletor ＋ 番号」となっていないときは、
引数pathのディレクトリ＋ファイル名「file_name + sepaletor + 番号 + 元拡張子」としてreturnします。
file_nameの拡張子を除く最後の文字が「sepaletor ＋ 番号」となっているときは、
最後の番号に＋１をしてfile_nameに代入し、引数pathのディレクトリ＋file_nameとしてreturnします。
*****
「最後の番号に＋１をしてfile_nameに代入し、引数pathのディレクトリ＋file_nameとしてreturnします。」
上記の最後の処理について、以下の処理に変更してください。
「最後の番号に＋１をしてfile_nameに代入し、new_file_name とします。
「pathのディレクトリ＋new_file_name +元拡張子」が存在しなければ、そのpathをreturnします。
「pathのディレクトリ＋new_file_name +元拡張子」が存在するときは、再帰的にcreate_new_filenameを呼び出して取得したpathをreturnします。
」
---
最後の数字を判定する処理ですが、上記では数字1文字しか対応していません。
1桁以上（複数桁）の数字「23012」、また、ゼロから始まる数字「0012」などにも対応させてください。
"""

import os
import re

def create_new_filename(path, separator='_'):
    if not os.path.exists(path):
        return path

    directory, file_with_extension = os.path.split(path)
    file_name, extension = os.path.splitext(file_with_extension)

    # Check if the last character of file_name (excluding extension) is separator + number
    last_char = file_name[-1]
    if last_char.isdigit() and separator in file_name[:-1]:
        separator_index = file_name.rfind(separator)
        number_str = file_name[separator_index+1:]
        # Use regular expression to match any number of digits (1 or more) at the end of the string
        match = re.search(r'\d+$', number_str)
        if match:
            number_str = match.group()
            number = int(number_str)
            new_file_name = file_name[:separator_index] + separator + str(number + 1).zfill(len(number_str))
        else:
            new_file_name = file_name + separator + '1'
    else:
        new_file_name = file_name + separator + '1'

    new_file_name_with_extension = new_file_name + extension
    new_path = os.path.join(directory, new_file_name_with_extension)

    if not os.path.exists(new_path):
        return new_path
    else:
        return create_new_filename(new_path, separator)



def _test_main():
    # assert create_new_filename('./pathto/file.txt', '_') == './pathto/file_1.txt'
    # assert create_new_filename('./pathto/file_1.txt', '_') == './pathto/file_2.txt'
    # assert create_new_filename('./pathto/another_file.jpg', '-') == './pathto/another_file-1.jpg'
    # assert create_new_filename('./pathto/nonexistent_file.png', '_') == './pathto/nonexistent_file.png'
    asserted_paths = [
        './pathto/file.txt',
        './pathto/file_1.txt', 
        './pathto/file_002.txt', 
        './pathto/another_file.jpg', 
        './pathto/nonexistent_file.png',
    ]

    for path in asserted_paths:
        try:
            new_path = create_new_filename(path, '_')
            assert not os.path.exists(new_path)
            print(f'Path is Valid: {new_path}')
        except AssertionError:
            print(f'AssertionError: {new_path}')
        except Exception as e:
            print(f'Error: {e}')



if __name__ == '__main__':
    _test_main()