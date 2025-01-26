import os

def print_directory_structure(folder_path, indent=0):
    """
    指定したフォルダの構成をインデント付きで出力する関数。

    :param folder_path: フォルダのパス
    :param indent: 現在のインデントレベル（内部用）
    """
    if not os.path.exists(folder_path):
        print(f"指定されたフォルダが存在しません: {folder_path}")
        return

    # フォルダとファイルを取得
    entries = sorted(os.listdir(folder_path))

    for entry in entries:
        entry_path = os.path.join(folder_path, entry)
        # インデントを作成してエントリを出力
        print("    " * indent + entry)
        # サブディレクトリの場合は再帰呼び出し
        if os.path.isdir(entry_path):
            print_directory_structure(entry_path, indent + 1)

# 使用例
print("\n ****** ")
folder_path = "my_project"  # 出力したいフォルダのパス
folder_path = r"C:\Users\OK\source\repos\Repository4_python\django_test\login_sys_a"
print_directory_structure(folder_path, 1)
