"""
"key":"value"の形式になっているか

https://qiita.com/luohao0404/items/7135b2b96f9b0b196bf3

\d	任意の数字	[0-9]			
\D	任意の数字以外	[^0-9]			
\s	任意の空白文字	[\t\n\r\f\v]			
\S	任意の空白文字以外	[^\t\n\r\f\v]			
\w	任意の英数字	[a-zA-Z0-9_]			
\W	任意の英数字以外	[\a-zA-Z0-9_]			
\A	文字列の先頭	^			
\Z	文字列の末尾	$			
.	任意の一文字	-	a.c	abc, acc, aac	abbc, accc
^	文字列の先頭	-	^abc	abcdef	defabc
$	文字列の末尾	-	abc$	defabc	abcdef
*	０回以上の繰り返し	-	ab*	a, ab, abb, abbb	aa, bb
+	１回以上の繰り返し	-	ab+	ab, abb, abbb	a, aa, bb
?	０回または１回	-	ab?	a, ab	abb
{m}	m回の繰り返し	-	a{3}	aaa	a, aa, aaaa
{m,n}	m〜n回の繰り返し	-	a{2, 4}	aa, aaa, aaaa	a, aaaaa
[]	集合	-	[a-c]	a, b, c	d, e, f
縦線	和集合（または）	-	a縦線b	a, b	c, d
()	グループ化	-	(abc)+	abc, abcabc	a, ab, abcd
"""


class JsonValue():

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

def is_json():
    try:
        val = ' "key4":"data4" '
        val = '{ "key4":"data4" }'
        jv = JsonValue(val)
        flag = jv.is_current_format_json_piece()
        print(flag)
        flag = jv.is_current_format_json()
        print(flag)
        
        return
    except:
        import traceback
        traceback.print_exc()

is_json()