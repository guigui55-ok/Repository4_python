from input.input import input,input_init
input_init()

init_val = input()
print(init_val)
init_val = input()
print(init_val)
init_val = input()
print(init_val)

class ComaAbs:
    move_enable = []
    def __init__(self):
        self.move_enable.append([0,0,0])