import pickle

def dict_str_test2():
    import pickle
    dict = {'Hello': 60, 'World': 100}
    d_byte = pickle.dumps(dict)
    print('d_byte')
    print(d_byte)
    d_dict = pickle.loads(d_byte)
    print('d_dict')
    print(d_dict)

dict_str_test2()