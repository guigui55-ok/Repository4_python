from lib2to3.pgen2.token import NEWLINE
import traceback
import keyboard
import time

NEW_LINE = '\n'

class KeyState():
    def __init__(self) -> None:
        self.key_down:str = ''
        self.down_state:dict = {}
        self.now_ch:str = ''
        self.input:str = ''
    def read_key(self):
        self.now = keyboard.read_key()
    def check_value(self):
        if len(self.now_ch)<2:
            if self.is_key_down():
                self.input += self.now_ch
                self.key_down += self.now_ch
                print(self.now_ch,end='')
            else:
                self.key_down = self.key_down.replace(self.now_ch,'')
        else:
            if self.now_ch == 'enter':
                print()
                self.input = ''
            else:
                pass
    def is_key_down(self):
        if self.key_down.find(self.now_ch)>=0:
            return False
        return True
def input_recieve():
    try:
        ch = ''
        input_value = ''
        while True:
            # input_value = input('>> ')
            ## keydown、keyup時両方、受け取っている
            ch = keyboard.read_key()
            # if len(ch) == 2:
            #     if ch[0] == ch[1]:
            #         ch = ch[0]
            print_ch(ch)
            time.sleep(0.01)
            if len(ch) > 1:
                if ch == 'enter':
                    ch = NEW_LINE
                    print()
                    print(input_value)
                    print('---')
                    input_value = ''
                    ch = ''
                else:
                    pass
            elif len(ch) == 1:
                input_value += ch

            # if keyboard.is_pressed("enter"):
            #     print()
            #     print(input_value)
            #     print('---')
            #     input_value = ''
            #     ch = ''
            # else:
            #     input_value += ch

            if ch == "p":
                print_ch(ch)
            
            if keyboard.is_pressed("q"):
                print_ch(ch)
            
            if input_value == 'exit()':
                break
        
        return
    except:
        traceback.print_exc()
        return

def print_ch(value:str):
    print(value,end='')

if __name__ == '__main__':
    input_recieve()

