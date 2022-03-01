# def count_up_file_name(file_name:str,delimita='_'):
#     import os
#     # 拡張子
#     ext = os.path.splitext(file_name)[1]
#     # 拡張子なしのファイル名
#     basename_without_ext = os.path.splitext(os.path.basename(file_name))[0]
#     # get digit
#     pos = basename_without_ext.rfind(delimita)
#     if pos > 0:
#         digit = len(basename_without_ext) - pos + 1
#     else:
#         # digit = 0
#         ret_file_name = basename_without_ext + delimita + str(1) + ext
#         return ret_file_name
#     # get number
#     n_str = basename_without_ext[pos+1:]
#     num:int = int(n_str)+1
#     if len(str(num)) < digit:
#         ret_num_str = ''
#         for i in range(digit):
#             ret_num_str += '0'
#         ret_num_str += str(num)
#     # create file name
#     ret_file_name = basename_without_ext[:pos+1] + ret_num_str + ext
#     return ret_file_name

def get_count_up_number_str_keep_digit(num_str:str):
    """
    数字のみの文字列をカウントアップする、桁数を維持したまま
    ex)
    3 => 4
    9 => 10
    0012 => 0013
    0099 => 0100
    0000 -> 0001
    """
    # get number
    n_str = num_str # 数字
    digit = len(num_str) # 桁数
    # 1加えておく、999→1000の繰り上がりに対処するため
    num:int = int(n_str)+1
    # 桁数以下ならゼロを加える 00056 : 57=>00057
    if len(str(num)) < digit:
        ret_num_str = ''
        for i in range(digit-len(str(num))):
            ret_num_str += '0'
        ret_num_str += str(num)
    return ret_num_str
    
def is_number(value:str):
    try:
        n = int(value)
        return True
    except:
        return False

def count_up_if_last_name_is_number(file_name,delimita='_'):
    """
    ファイル名の末尾が 「_数値」 かつ、すでに存在する場合、末尾の数値部をカウントアップする
    ファイル名が file_name_003.ext の時、file_name_004.ext にする
    ex) file_name_9.ext > file_name_10.ext
    拡張子がない場合はおそらくエラー
    同名がある場合はさらにカウントアップする
    * recommended
    戻り値：
    成功時はファイル名を返す
    　　ファイル名が存在しない場合はそのまま file_name を返す
    失敗時は空文字''を返す
    """
    try:
        import os
        if os.path.exists(file_name):
            new_name = count_up_if_last_name_is_number_main(
                file_name,delimita)
            if os.path.exists(new_name):
                # リネーム後さらに存在する場合、再帰的に実行する
                new_name = count_up_if_last_name_is_number(
                    new_name,delimita)
            
            return new_name
        else:
            return file_name
    except:
        import traceback
        traceback.print_exc()
        return ''

def count_up_if_last_name_is_number_main(file_name,delimita='_'):
    """
    ファイル名が file_name_003.ext の時、file_name_004.ext にする
    ex) file_name_9.ext > file_name_10.ext
    file_name.ext > file_name_1.ext
    拡張子がない場合はエラー
    """
    import os
    # 拡張子
    ext = os.path.splitext(file_name)[1]
    # 拡張子なしのファイル名
    basename_without_ext:str = os.path.splitext(os.path.basename(file_name))[0]
    # find
    pos = basename_without_ext.rfind(delimita)
    if pos < 0:
        # 最後が _1 形式ではないときは、数字を付加して終了
        ret_file_name = basename_without_ext + delimita + '1' + ext
        return ret_file_name
    # pos >= 0
    after_delimita_str = basename_without_ext[pos+1:]
    if not is_number(after_delimita_str):
        # 最後が _1 形式ではないときは、数字を付加して終了
        ret_file_name = basename_without_ext + delimita + '1' + ext
        return ret_file_name
    ret_num = get_count_up_number_str_keep_digit(after_delimita_str)
    ret_file_name = basename_without_ext[:pos+1] + ret_num + ext
    return ret_file_name

