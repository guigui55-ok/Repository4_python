



def arg_excute_function(logger,value1,value2):
    try:
        print('arg_excute_function')
        print(value1,value2)
        logger.info('value1,value2')
        logger.info([str(value1),str(value2)])
        return True
    except Exception as e:
        import traceback
        print(traceback.print_exc())
        logger.exp.error(e)
        return False

class ConsoleCutMovie():
    logger = None
    called_function =None
    # パラメータ
    input_text1 :str
    input_text2 :str
    result_path = ''

    def __init__(self,logger,excute_function,result_path) -> None:
        self.logger = logger
        self.called_function = excute_function
        self.result_path = result_path

    def get_text1(self):
        return self.input_text1
    def get_text2(self):
        return self.input_text2

    def excute_function(self):
        try:
            _begin = self.get_text1()
            _end = self.get_text2()
            self.called_function( int(_begin),int(_end),self.result_path)
            # print('excute_function')
            # print(value1,value2)
            self.close_window()
            return True
        except Exception as e:
            import traceback
            print(traceback.print_exc())
            self.logger.exp.error(e)
            return False

    def close_window(self):
        try:
            pass
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def set_text(self,input_value:str):
        try:
            values = input_value.split(',')
            self.input_text1 = values[0]
            self.input_text2 = values[1]
        except Exception as e:
            self.logger.exp.error(e)
            self.logger.exp.error('   input_value=' + input_value)
            return False

    def show_input(self):
        try:           
            print('input cut frame:betin_frame,end_frame')
            input_val = input()
            self.set_text(input_val)
            return True
            
        except Exception as e:
            import traceback
            print(traceback.print_exc())
            self.logger.exp.error(e)
            return False
