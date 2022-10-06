
import json

def main():
    value : dict ={
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }
    
    with open('./test.json', 'w') as f:
        json.dump(value, f, indent=4)
    return

if __name__ == '__main__':
    main()