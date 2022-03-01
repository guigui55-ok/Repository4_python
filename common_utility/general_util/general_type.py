import traceback
def cnv_hex_str_to_int(value:str):
    """
    0001 -> 1 -> 1
    014a -> 14a -> 330
    """
    try:
        hex_str = ''
        for c in value:
            if c != '0':
                hex_str += c
        ret:int = 0
        for i in range(len(hex_str)):
            n = len(hex_str)-i-1
            c = hex_str[n:n+1]
            ret += cnv_hex_char_to_int(c,i)
        return ret
    except:
        traceback.print_exc()
        return 0

        
def cnv_hex_char_to_int(char:str,digit)->int:
    """
    16進数のcharをintに変換する
    digitで桁数を指定する
    """
    try:
        import re
        if re.match('[0-9]',char): n = int(char)
        elif re.match('[aA]',char): n = 10
        elif re.match('[bB]',char): n = 11
        elif re.match('[cC]',char): n = 12
        elif re.match('[dD]',char): n = 13
        elif re.match('[eE]',char): n = 14
        elif re.match('[fF]',char): n = 15
        else: n = 0
        n = n * pow(16,digit)
        return n
    except:
        traceback.print_exc()
        return 0
