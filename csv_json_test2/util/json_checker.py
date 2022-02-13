"""
"key":"value"の形式になっているか

https://qiita.com/luohao0404/items/7135b2b96f9b0b196bf3
"""


class JsonValueChecker():

    def __init__(self,value:str='') -> None:
        class ReservedWords():
            def __init__(self) -> None:
                self.space = ' '
                self.brackets_left = '{'
                self.brackets_right = '}'
                self.double_quotation = '"'
                self.colon = ':'

        self.reserved_words = ReservedWords()
        self.json_piece_format_value = '"":""'
        self.json_format_value = '{' + self.json_piece_format_value + '}'
        self.value:str = value
            
    def set_value(self,value):
        self.value = value

    def is_reserved_words(self,c):
        words_dict = vars(self.reserved_words)
        words = words_dict.values()
        for word in words:
            if word != ' ':
                if c == word:
                    return True
        return False
    
    def get_format(self,value:str)->str:
        reserved_words_exacted:str = ''
        for c in value:
            if self.is_reserved_words(c):
                reserved_words_exacted += c
        return reserved_words_exacted

    def is_current_format_json_piece(self,value:str=''):
        if value == '': value = self.value
        reserved_words_exacted:str = self.get_format(value)
        if self.json_piece_format_value == reserved_words_exacted:
            return True
        else:
            return False
    
    def is_current_format_json(self,value:str=''):
        if value == '': value = self.value
        reserved_words_exacted:str = self.get_format(value)
        if self.json_format_value == reserved_words_exacted:
            return True
        else:
            return False

def json_checker_sample():
    try:
        val = ' "key4":"data4" '
        val = '{ "key4":"data4" }'
        val = """
{
    "key4":"data4"
}
"""
        jv = JsonValueChecker(val)
        flag = jv.is_current_format_json_piece()
        print(flag)
        flag = jv.is_current_format_json()
        print(flag)
        
        return
    except:
        import traceback
        traceback.print_exc()

json_checker_sample()