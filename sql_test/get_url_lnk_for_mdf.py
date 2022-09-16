
NEW_LINE = '\n'

import datetime
from lib2to3.pgen2.token import NEWLINE

from matplotlib.pyplot import table
class MovieLinkInfo():
    """
    MovieInfoをmdf(sql serverへ)登録するためのクラス、（データはdictで扱って汎用性を高めたほうがよい[修正予定]）
    """
    def __init__(self,regist_list:'list[str]'=None) -> None:
        if regist_list!=None:
            if len(regist_list)==9:
                for i in range(len(regist_list)):
                    buf = regist_list[i]
                    if i==0: self.id = int(buf)
                    elif i==1: self.url = buf
                    elif i==2: self.movie_name = buf
                    elif i==3: self.file_name = buf
                    elif i==4: self.date = buf
                    elif i==5: self.regist_times = int(buf)
                    elif i==6: self.folder = buf
                    elif i==7: self.movie_id = buf
                    elif i==8: self.time = buf
        else:
            self.file_name = ''
            self.url = ''
            self.id = 0
            self.movie_name = ''
            now =  str(datetime.datetime.now())[:19]
            now =  str(datetime.datetime.now())[:10]
            self.date:datetime.date = now
            self.regist_times = 1
            self.folder = ''
            self.movie_id = ''
            now_time = str(datetime.datetime.time(datetime.datetime.now()))[:8]
            self.time:datetime.time = now_time
        self.dict = self.get_default_dict()
        
    def get_sql_for_insert(self,table_name:str):
        new_line_ = NEW_LINE
        new_line_ = NEW_LINE + ' '
        sql = 'INSERT INTO ' + table_name + new_line_
        sql += self.get_col_names(table_name='') + new_line_
        sql += 'VALUES' + new_line_
        sql += self.get_values()

        # sql = 'INSERT INTO ' + table_name + NEW_LINE
        # values = self.get_values()
        # sql += 'VALUES' + '{}'.format(values)

        sql = 'INSERT INTO [{}]{}'.format(table_name,new_line_)
        values = '({},{})'.format(self.id,self.url)
        # sql += 'VALUES' + '{}'.format(values)
        sql += 'VALUES '
        sql += self.get_values()
        print()
        print('==========')
        print(sql)
        print()
        return sql

        return
    def get_values(self):
        vals = '('
        vals += '{},'.format(self.id)
        vals += "'{}',".format(self.url)
        vals += "'{}',".format(self.movie_name)
        vals += "'{}',".format(self.file_name)
        # vals += '{},'.format(self.date)
        vals += "'{}',".format(self.date)
        vals += '{},'.format(self.regist_times)
        vals += "'{}',".format(self.folder)
        vals += "'{}',".format(self.movie_id)
        # vals += '{}'.format(self.time)
        vals += "'{}'".format(self.time)
        vals += ')'
        return vals

    def get_col_names(self,table_name:str=''):
        if table_name!='': table_name +='.'
        d:dict = self.get_default_dict()
        cols = d.keys()
        names = '('
        for col in cols:
            names += table_name + col + ','
        names = names[:-1] + ')'
        return names
    def get_default_dict(self):
        d = {
            'Id':0,
            'URL':'',
            'MovieName':'',
            'FileName':'',
            'Date':'1981-01-01',
            'RegistTimes':0,
            'Folder':'',
            'MovieID':'',
            'Time':'00:00:00.000000'
        }
        return d


    def get_date_str(self):
        return str(self.date) # 2018-02-01
    def get_time_str(self):
        return str(self.time) # 12:15:30.002000
        return self.time.strftime('%H%m%d.%s')
    def print_data(self):
        print('*****')
        print('file_name = '+ self.file_name)
        print('url = '+ self.url)
        print('movie_name = ' + self.movie_name)
        print('movie_id = ' + self.movie_id)
        print('regist_times = ' + self.regist_times)
        print('folder = ' + self.folder)
        print('date = '+ str(self.date))
        print('time = ' + str(self.time))
        print('*****')
    
    def remove_invalid_char_or_file_name(self,value:str):
        replace_vals = ["'"]
        for rep_val in replace_vals:
            value = value.replace(rep_val,'')
        return value

    def set_info_from_path(self,path):
        import os 

        print('path = ' + path)
        self.file_name = os.path.basename(path)
        self.file_name = self.remove_invalid_char_or_file_name(self.file_name)
        print('file_name = '+ self.file_name)
        self.url = self.get_url_from_link(path)
        self.url = self.replace_url(self.url)
        print('url = '+ self.url)
        self.movie_name = self.get_last_folder_from_url(self.url)
        print('movie_name = ' + self.movie_name)
        self.movie_id = self.get_movie_id(self.url)
        print('movie_id = ' + self.movie_id)
        self.regist_times = 1
        print('regist_times = ' + str(self.regist_times))
        dir_path = os.path.dirname(path)
        self.folder = os.path.basename(dir_path)
        self.folder = self.remove_invalid_char_or_file_name(self.folder)
        print('folder = ' + self.folder)
        print('date = '+ str(self.date))
        print('time = ' + str(self.time))
        return
    def replace_url(self,url:str):
        path = r'C:\Users\OK\source\repos\Test\movie_data\vtest_rep_bef.txt'
        with open(path,'r',encoding='utf-8')as f:
            bef = f.read()
        path = r'C:\Users\OK\source\repos\Test\movie_data\vtest_rep_aft.txt'
        with open(path,'r',encoding='utf-8')as f:
            aft = f.read()
        url = url.replace(bef,aft)
        return url
    def get_movie_id(self,url:str):
        ###
        path = r'C:\Users\OK\source\repos\Test\movie_data\vtest.txt'
        with open(path,'r',encoding='utf-8')as f:
            buf = f.read()
        ###
        n = url.find(buf)
        if n>0:
            ary = url.split('/')
            count = 0
            for el in ary:
                if count>=3:
                    if el.find('video')>=0:
                        return el
                count+=1
        else:
            #以外はとりあえずMovieNameとMovieIDは同じにする
            return self.get_last_folder_from_url(url)
    def get_last_folder_from_url(self,url:str):
        if url=='': return ''
        #最後のスラッシュはカウントしない
        if url[-1] == '/':
            url = url[:-1]
        pos = url.rfind('/')
        if pos >= 0:
            return url[pos+1:]

    def get_url_from_link(self,lnk_path:str):
        """lnkからURLを取得する"""
        with open(lnk_path, 'r',encoding='utf-8')as f:
            buf = f.read()
        buf = buf.replace(NEW_LINE,'')
        buf = buf.replace('[InternetShortcut]URL=','')
        return buf


def get_info_from_path(path):
    info = MovieLinkInfo()
    info.set_info_from_path(path)

if __name__ == '__main__':
    path = r'C:\ZMyFolder\newDoc\新しいfiles\0528 you\sumi\.url'
    get_info_from_path(path)

# import glob
# for path in glob.glob(r'C:\ZMyFolder\newDoc\新しいfiles\0528 you\sumi'+'\**'):
#     print(path)