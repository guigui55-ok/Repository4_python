


def main():
    ###
    # https://aiacademy.jp/media/?p=1252
    # 1から10までの数値をそれぞれ2乗した数値のリスト
    result = [x**2 for x in range(1,11)]
    print(result) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    ###
    #アスタリスクを個数分作る
    buf = ['*' for buf in range(10)]
    # リストを文字列に連結
    buf = ''.join(buf)
    print(buf)

    ###
    # https://note.nkmk.me/python-list-comprehension/
    # [式 for 任意の変数名 in イテラブルオブジェクト]
    # [式 for 任意の変数名 in イテラブルオブジェクト if 条件式]
    odds = [i for i in range(10) if i % 2 == 1]
    print(odds)
    # [1, 3, 5, 7, 9]

    # 偶数だけ
    result2 = [num for num in result if num % 2 == 0]
    print(result2)

    # [真のときの値 if 条件式 else 偽のときの値 for 任意の変数名 in イテラブルオブジェクト]
    odd_even = ['odd' if i % 2 == 1 else 'even' for i in range(10)]
    print(odd_even)
    # ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

    # 奇数は0にする
    result2 = [num if num % 2 == 0 else 0 for num in result]
    print(result2)

    # 
    l_str1 = ['a', 'b', 'c']
    l_enu = [(i, s) for i, s in enumerate(l_str1)]
    print(l_enu)
    # [(0, 'a'), (1, 'b'), (2, 'c')]

    # ネストしたリスト内包表記（多重ループ）
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [x for row in matrix for x in row]
    print(flat)
    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # flat = [x for row in matrix for y in row] #NameError: name 'x' is not defined
    # flat = [y for row in matrix for x in row] #NameError: name 'y' is not defined
    flat = [row for row in matrix]
    print(flat)

if __name__ == '__main__':
    main()