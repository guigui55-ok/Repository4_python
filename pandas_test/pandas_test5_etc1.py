"""
pandas その他いろいろ
"""
# https://www.yutaka-note.com/entry/pandas_index_setting

print('インデックス・カラムについて')

from pathlib import Path
dir_path = r'C:\Users\OK\source\repos\Repository4_python\excel_test'
excel_path = Path(dir_path).joinpath('FileIO.xlsm')
excel_path_str = str(excel_path)

import pandas as pd
# Excel、CSVデータ読み込み時に指定
df = pd.read_excel(excel_path_str, header=0, index_col=0)  # header=0は省略可能


## 生成後のdfのインデックス名、カラム名の変更

df.index=["i0", "i1"]
df.columns=["c0", "c1", "c2"]

df.set_axis(["i0", "i1"], axis="index", inplace=True)
df.set_axis(["c0", "c1", "c2"], axis="columns", inplace=True)

# dfのラベル名を一部変更｜df.rename()
# ラベル名の前後に文字列追加｜df.prefix (), df.suffix()
# インデックスのリセット｜df.reset_index()





