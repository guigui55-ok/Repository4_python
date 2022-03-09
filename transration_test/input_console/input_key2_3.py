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
        self.now_ch = keyboard.read_key()
        self.check_value()

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
                self.input = ''
            else:
                pass
    def is_key_down(self):
        if self.key_down.find(self.now_ch)>=0:
            return False
        return True



def input_recieve():
    try:
        key_input = KeyState()
        ch = ''
        input_value = ''
        while True:
            key_input.read_key()

            if key_input.input == "p":
                print_ch(ch)
            
            if keyboard.is_pressed("q"):
                print_ch(ch)
            
            if key_input.input == 'exit_':
                break
        
        return
    except:
        traceback.print_exc()
        return

def print_ch(value:str):
    print(value,end='')

if __name__ == '__main__':
    input_recieve()

