import os

file_path = 'hello.txt'
dir_path = os.getcwd()

# ファイルの存在チェック ： ファイル＆フォルダ用
is_exists = os.path.exists(file_path)
print('os.path.exists(''hello.txt'') = ' + str(is_exists))

# ファイルの存在チェック ： ファイル＆フォルダ用
is_exists = os.path.exists(dir_path)
print('os.path.exists(''os.getcwd()'') = ' + str(is_exists))

# ファイルの存在チェック ： ファイル用
is_exists = os.path.isfile(file_path)
print('os.path.isfile(''hello.txt'') = ' + str(is_exists))
# ファイルの存在チェック ： ファイル用
is_exists = os.path.isfile(dir_path)
print('os.path.isfile(''os.getcwd()'') = ' + str(is_exists))

# ファイルの存在チェック ： ファイル用
is_exists = os.path.isdir(file_path)
print('os.path.isdir(''hello.txt'') = ' + str(is_exists))
# ファイルの存在チェック ： ファイル用
is_exists = os.path.isdir(dir_path)
print('os.path.isdir(''os.getcwd()'') = ' + str(is_exists))