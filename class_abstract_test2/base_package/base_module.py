from os import device_encoding


class DeiviceInfo():
    def __init__(self,platform,model,os_ver) -> None:
        self.model = model
        self.os_ver = os_ver
        self.platform_name = platform


class BaseClass():
    def __init__(self,platform,model,os_ver) -> None:
        self.value = 'BaseClass'
        self.dev_info:DeiviceInfo = DeiviceInfo(platform,model,os_ver)
        
    def excute_methods(self,called_file_path:str,called_method_name:str,indent:str=''):
        print('BaseClass.excute_methods')
        print('    * ' + __file__)
        indent += '    '
        print(indent + 'called')
        print(indent + 'path  > '+ called_file_path)
        print(indent + 'metod > '+ called_method_name)