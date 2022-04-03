class BaseClass():
    def __init__(self) -> None:
        self.value = 'BaseClass'
    def excute_methods(self,called_file_path:str,called_method_name:str,indent:str=''):
        print('BaseClass.excute_methods')
        print('    * ' + __file__)
        indent += '    '
        print(indent + 'called')
        print(indent + 'path  > '+ called_file_path)
        print(indent + 'metod > '+ called_method_name)