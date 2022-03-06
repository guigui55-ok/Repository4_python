
import traceback
from googletrans import Translator


def transration_word(value:str)->str:
    try:
        translator = Translator()
        message = translator.translate(value, src='en', dest='ja')
        return str(message.text)
    except Exception as e:
        return str(e)

def input_recieve():
    try:
        while True:
            input_value = input('>> ')
            if input_value == 'exit()':
                break
            print('---')
            trans_value = transration_word(input_value)
            print(trans_value)
            print('---')        
        return
    except:
        traceback.print_exc()

if __name__ == '__main__':
    input_recieve()


