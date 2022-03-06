
def input_recieve():
    try:
        while True:
            input_value = input('>> ')
            if input_value == 'exit()':
                break
            print('---')
            print(input_value)
            print('---')
        
        return
    except:
        return

if __name__ == '__main__':
    input_recieve()