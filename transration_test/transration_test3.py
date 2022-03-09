"""
https://plog.shinmaiblog.com/python-translator/
バージョンが4.0.0-rc1以上

googletransの動作を確認しました。注意点は以下のとおりです。

テキストは最大15kまで
Google翻訳の制限に依存し、このライブラリはいつでも利用可能とは限らない
安定性が必要な場合は有料のGoogle’s official translate APIを使いましょう

pip install googletrans==4.0.0-rc1
"""

from lib2to3.pgen2.token import NEWLINE
from optparse import Values
from googletrans import Translator

def translation_word(translator:Translator, value:str, dest:str='ja', src:str=''):
    try:
        if src == '':
            ret = translator.translate(value, dest='ja')
        else:
            ret = translator.translate(value, src=src, dest='ja')
        return ret
    except:
        bar='######################################################################'
        print(bar)
        import traceback
        traceback.print_exc()

from googletrans.models import Translated, Detected, TranslatedPart
NEW_LINE = '\n'
class Translations():
    def __init__(self) -> None:
        self.translator:Translator = Translator()
        self.dest:str = 'ja'
        self.src:str = ''
        self.values:'list[str]' = ''
        self.result:Translated = ''
        self.result_list:'list[str]' = []
        self.is_averable = False
    def excute(self,arg_value):
        self.is_averable = False
        ### check type
        if isinstance(arg_value,list):
            if len(arg_value) > 0:
                self.is_averable = True
                self.values = arg_value
        if isinstance(arg_value,str):
            # self.split_str(arg_value)
            self.values = [arg_value]
            self.is_averable = True
        if not self.is_averable:
            print('### value is invalid , translation return.')
            return
        ### excute
        ret_list = []
        for value in self.values:
            ret = self.excute_core(value)
            if ret != None:
                ret_list.append(ret)
        
        for ret in ret_list:
            print(ret)
    
    def split_str(self,value:str):
        val_list = value.split(NEW_LINE)
        self.values = val_list

    def excute_core(self,value:str):
        if value=='':
            self.result = None
            return
        if self.src == '':
            self.result = self.translator.translate(value, dest=self.dest)
        else:
            self.result = self.translator.translate(value, src=self.src, dest=self.dest)
        return self.result.text
    def print_result(self):
        print(self.result.text)


def main():
    word = """Blühe, deutsches Vaterland"""
    word = '''
    '''
    word = 'This is a pen.'
    import input_console.input_key3_4 as input_key
    translations = Translations()
    input_key.input_char_main(translations)

main()
