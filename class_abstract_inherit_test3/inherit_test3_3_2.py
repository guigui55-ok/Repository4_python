#多重継承テスト



# NoChangeMain に NoChangeExtends_b両方を加えた NoChangeMain_New
# これをNoChangeMainインスタンス（オブジェクト）置き換えて使う
#  ＞＞既存コードには影響なし
# 新たに NoChangeExtends_b　クラスメソッドも組み込みやすい

from inherit_test3_3 import NoChangeMain_New as NoChangeMain
"""
さらにこれをas句で名前を置き換え連と、既存コードには影響なし

*****
ただ、既存のコーダーには、周知が必要
以前のNoChangeMainのままだと思って、作業を進める可能性がある
"""

def main():
    cl = NoChangeMain()
    cl.print_extends()
    cl.print_base()
    cl.print_extends_b()

main()