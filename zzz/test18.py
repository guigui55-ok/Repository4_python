#https://teratail.com/questions/52zhtoh0n5fh04
import pandas as pd

df = pd.DataFrame(
    data={'A': ['1_あいうえお 2_かきく 3_さしすせそ 2_かきくけこ', '1_あいうえお 2_かきく 3_さしすせそ 2_かきくけこ 3_さしす'],
          'B': ['1_あいうえお 2_かきくけこ 3_さしすせそ', '1_あいうえお 2_かきく 3_さしす 2_かきくけこ']} 
)

def process_for_str(before_data:str):
    """文字列を処理する関数"""
    # 元データをスペースで区切った配列にする
    list1 = before_data.split(' ')
    print('  proc1 : list1 = {}'.format(list1)) # 確認用
    d:dict={}
    # 上記配列の各要素に対し、
    # アンダースコアで区切った配列を作成して、
    # それを dictに変換して d に追加・上書きしていく
    # ※ dict.update メソッドは同じkeyが存在するときは上書きされる
    for l in list1:
        list2 = l.split('_')
        d.update({list2[0]:list2[1]}) # 確認用
    print('  proc2 : d = {}'.format(d))
    # 上記で処理された dict を str に戻す
    ret = ''
    for k in d.keys():
        ret+='{}_{} '.format(k,d[k])
    ret=ret[:-1]
    return ret

#####
# メイン処理
#####
for data in df.iterrows():
    before_data = data[1]['A']
    print('*******')
    print('before_data= {}'.format(before_data))
    after_data = process_for_str(before_data)
    print('after_data= {}'.format(after_data))
    print('result = {}'.format(after_data == data[1]['B']))
    print()
    

"""

"""

#############
# for k in df.keys():
#     data = df[k]
#     before_data = data.values[1] # 処理前のデータのみ選択しています
#     print('*******')
#     print(data.values)
#     print('before_data= {}'.format(before_data))
#     after_data = process_for_str(before_data)
#     print(' after_data= {}'.format(after_data))
#     print(' compare = {}'.format(data.values[0]))
#     print('result = {}'.format(after_data == data.values[0]))
#     print()

def compare_data(dict:dict, data:dict):
    data_key = data.keys()[0]
    if data_key in dict.keys():
        #比較する処理
        if True:
            dict.update(data)
        else:
            pass
