
import tkinter
from tkinter import ttk

from tkinter import StringVar



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

class FormCutMovie():
    logger = None
    called_function =None
    # パラメータ
    input_text1 :StringVar
    input_text2 :StringVar
    result_path = ''

    main_win : tkinter.Tk

    def __init__(self,logger,excute_function,result_path) -> None:
        self.logger = logger
        self.called_function = excute_function
        self.result_path = result_path

    def get_text1(self):
        return self.input_text1.get()
    def get_text2(self):
        return self.input_text2.get()

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
            self.main_win.destroy()
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False


    def show_input(self):
        try:           

            # メインウィンドウ
            self.main_win = tkinter.Tk()
            self.main_win.title("cut_movie")
            self.main_win.geometry("350x80")
            
            self.input_text1 :StringVar = tkinter.StringVar()
            self.input_text2 :StringVar = tkinter.StringVar()
            # メインフレーム
            main_frm = ttk.Frame(self.main_win)
            # 位置揃えはstickyを用いて「N＝上、S＝下、E＝右、W＝左」で指定
            # sticky=tkinter.EWと左右両方を指定すると水平方向に引き延ばすことができます
            # 余白はpadxとpadyで指定します。padxは左右、padyは上下の余白になります。
            main_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)
            
            # ウィジェット作成（実行ボタン）
            app_btn = ttk.Button(main_frm, text="done" , command=self.excute_function )
            label1 = ttk.Label(main_frm,text='begin_frame')
            input_box1 = ttk.Entry(main_frm, textvariable=self.input_text1 ,width=10)
            label2 = ttk.Label(main_frm,text='end_frame')
            input_box2 = ttk.Entry(main_frm, textvariable=self.input_text2, width=10)
            
            # ウィジェットの配置
            label1.grid(column=0,row=0)
            input_box1.grid(column=0,row=1)
            label2.grid(column=1,row=0)
            input_box2.grid(column=1,row=1)
            app_btn.grid(column=2, row=1)

            # 配置設定
            self.main_win.columnconfigure(0, weight=1)
            self.main_win.rowconfigure(0, weight=1)
            gridindex = 1
            main_frm.columnconfigure(1, weight=1)
            
            self.main_win.mainloop()
            return True
            
        except Exception as e:
            import traceback
            print(traceback.print_exc())
            self.logger.exp.error(e)
            return False

    

if __name__ == '__main__':
    import sys
    import pathlib 
    path = str(pathlib.Path(__file__).parent.parent)
    sys.path.append(path)
    import logger_init
    logger = logger_init.initialize_logger()
    form = FormCutMovie(logger,arg_excute_function,'./result.mp4')
    form.show_input_form()