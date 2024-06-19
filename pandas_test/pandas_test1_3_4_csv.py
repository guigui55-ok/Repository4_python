

import pandas as pd
from pathlib import Path
import datetime
import numpy as np

TIME_FORMAT = '%Y/%m/%d %H:%M:%S'
NEW_LINE = '\n'
CRLF = NEW_LINE

def get_main_data_frame():
    csv_path_a = str(Path(__file__).parent.joinpath('__sample_data.csv'))
    print('csv_path_a = {}'.format(csv_path_a))
    df = pd.read_csv(csv_path_a)
    return df

def get_time_list_data_frame():
    csv_path_b = str(Path(__file__).parent.joinpath('__sample_non_overlapping_times_data_v4.csv'))
    print('csv_path_b = {}'.format(csv_path_b))
    df = pd.read_csv(csv_path_b)
    return df

def format_timedelta(td):
    """ timedeltaをHH:MM:SSの形式に変換する関数 """
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def parse_timedelta(time_str):
    """ HH:MM:SS形式の文字列をdatetime.timedeltaに変換する """
    hours, minutes, seconds = map(int, time_str.split(':'))
    return datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)


# 案件番号[6桁の数値]
# メインCD[4桁の数値]
# 種類[1桁の数値]
# 開始時刻
# 作業開始時刻
# 作業終了時刻
# 終了時刻
class ConstKeys():
    CASE_NUMBER = '案件番号'
    MAIN_CD = 'メインCD'
    INIT_ROWS = '初期行数'
    KIND_VALUE = '種類'
    START_TIME = '開始時刻'
    ACTIVE_START_TIME = '作業開始時刻'
    ACTIVE_END_TIME = '作業終了時刻'
    END_TIME = '終了時刻'
    #
    ADD_INTERVAL_TIME = '間隔時間'
    ADD_ACTIVITY_TIME = '活動時間'
    ADD_INTERVAL_LONG_FLAG = '間隔大'
    ADD_INTERVAL_NOT_FLAG = '間隔無'
    #
    ACTIVITY_TIME_TOTAL = '活動時間合計'
    ACTIVITY_TIME_TOTAL_VALUE = '活動時間合計_値'
    CONTINUE_TIMES = '連続活動回数'
    CONTINUE_TIMES_VALUE = '連続活動回数_値'
    MATCH_ROWS = '行数'
    ACTIVITY_EXCESS_TIME = '活動合計超過時間'
    # 
    NOW_ACTIVITY_EXCESS_TIME = '現在活動時間'
    NOW_ACTIVITY_EXCESS_TIME_VALUE = '現在活動超過時間_値'
    # 合計回数
    # 合計時間
    MATCH_CONDITIONS = '合致条件名'

class SampleLogger():
    def __init__(self) -> None:
        pass
    def info(self, value):
        print(str(value))

class Setting():
    def __init__(self) -> None:
        begin_time_str = '2022/8/1 00:00:00'
        self.begin_time = datetime.datetime.strptime(begin_time_str, TIME_FORMAT)
        self.end_time = self.begin_time + datetime.timedelta(hours=6)
        self.interval_border = datetime.timedelta(hours=1)
        self.continue_border = datetime.timedelta(minutes=30)
        self.continue_count_border = 3
        self.activity_total_border = datetime.timedelta(hours=4)
        self.activity_now_border = datetime.timedelta(hours=2)
        self.now_time = datetime.datetime.now()
        self.rank_border_b = datetime.timedelta(minutes=30)
        self.rank_border_a = datetime.timedelta(minutes=60)

class TimeFilter():
    """ データを現在時刻より前のみにする、start~now~end のデータは end=now にする"""
    def __init__(self) -> None:
        pass
    def set_values(self, df:pd.DataFrame, now_time:datetime.datetime):
        self.df = df
        self.now_time = now_time
    
    def excute_filter(self):
        self.df = self.df[self.df[ConstKeys.START_TIME] >= self.now_time]
    
    def replace_last_time_if_after_now(self):
        # Filter by start_time < now_time
        df_filtered = self.df[self.df[ConstKeys.START_TIME] < self.now_time].copy()
        # Adjust end_time for records where end_time > now_time
        # df_filtered.loc[df_filtered[ConstKeys.END_TIME] > self.now_time, ConstKeys.END_TIME] = self.now_time
        df_filtered.loc[df_filtered[ConstKeys.END_TIME] > self.now_time, ConstKeys.END_TIME] = np.nan
        # Sort by start_time
        df_sorted = df_filtered.sort_values(by=ConstKeys.START_TIME).reset_index(drop=True)
        self.df = df_sorted
    
    def convert_type_str_to_date(self):
        self.df[ConstKeys.START_TIME] = pd.to_datetime(self.df[ConstKeys.START_TIME])
        self.df[ConstKeys.END_TIME] = pd.to_datetime(self.df[ConstKeys.END_TIME])
        self.df[ConstKeys.ACTIVE_START_TIME] = pd.to_datetime(self.df[ConstKeys.ACTIVE_START_TIME])
        self.df[ConstKeys.ACTIVE_END_TIME] = pd.to_datetime(self.df[ConstKeys.ACTIVE_END_TIME])

class MainTimeFilter():
    def __init__(self, df) -> None:
        self.df:pd.DataFrame = df
        self.init_rows = 0
    
    def convert_type_str_to_date(self):
        self.df[ConstKeys.START_TIME] = pd.to_datetime(self.df[ConstKeys.START_TIME])
        self.df[ConstKeys.END_TIME] = pd.to_datetime(self.df[ConstKeys.END_TIME])
        self.df[ConstKeys.ACTIVE_START_TIME] = pd.to_datetime(self.df[ConstKeys.ACTIVE_START_TIME])
        self.df[ConstKeys.ACTIVE_END_TIME] = pd.to_datetime(self.df[ConstKeys.ACTIVE_END_TIME])

    def exact_main_cd(self, main_cd:int):
        self.df = self.df[self.df[ConstKeys.MAIN_CD] == int(main_cd)]
        self.init_rows = self.df.shape[0]
        last_record_start_time = self.df.iloc[-1][ConstKeys.START_TIME]
        print('last_record_start_time = {}'.format(last_record_start_time))


    def exact_time(self,begin_time, end_time):
        self.df = self.df[self.df[ConstKeys.START_TIME] >= begin_time]
        self.df = self.df[self.df[ConstKeys.END_TIME] < end_time]

    def add_time(self, setting:Setting):
        self.df[ConstKeys.ADD_ACTIVITY_TIME] \
            = self.df[ConstKeys.ACTIVE_END_TIME] - self.df[ConstKeys.ACTIVE_START_TIME]
        self.df[ConstKeys.ADD_INTERVAL_TIME] \
            = self.df[ConstKeys.ACTIVE_START_TIME] - self.df.shift(1)[ConstKeys.ACTIVE_END_TIME]
        # NaTをdatetime.timedelta(0)に変換
        self.df[ConstKeys.ADD_INTERVAL_TIME] = self.df[ConstKeys.ADD_INTERVAL_TIME].apply(
            lambda x: x if pd.notna(x) else datetime.timedelta(0))
        # ADD_INTERVAL_FLAGカラムを設定するロジック
        self.df[ConstKeys.ADD_INTERVAL_LONG_FLAG] = \
            self.df[ConstKeys.ADD_INTERVAL_TIME].apply(lambda x: x.total_seconds() / 60.0 > setting.interval_border.total_seconds() / 60.0)
        # self.df[ConstKeys.ADD_INTERVAL_FLAG] = self.df[ConstKeys.ADD_INTERVAL_TIME].apply(
        #     lambda x: (x if pd.notna(x) else pd.Timedelta(0)).components.minutes > setting.interval_border)
        # self.df[ConstKeys.ADD_INTERVAL_FLAG] = self.df[ConstKeys.ADD_INTERVAL_TIME].apply(
        #     lambda x: (x if pd.notna(x) else pd.Timedelta(0)).seconds / 60.0 > setting.interval_border)    
        self.df[ConstKeys.ADD_INTERVAL_NOT_FLAG] = \
            self.df[ConstKeys.ADD_INTERVAL_TIME].apply(lambda x: x.total_seconds() / 60.0 < setting.continue_border.total_seconds() / 60.0)
        # self.df.iloc[0][ConstKeys.ADD_INTERVAL_NOT_FLAG] = 0
        # self.df[ConstKeys.ADD_INTERVAL_NOT_FLAG].iloc[0]= False
        #  SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame
        if self.df.shape[0] > 0:
            self.df.loc[self.df.index[0], ConstKeys.ADD_INTERVAL_NOT_FLAG] = False
        # print(self.df[ConstKeys.ADD_INTERVAL_NOT_FLAG])
        # 超過時間を計算する
        # 0以下なら0にする
        self.df[ConstKeys.ACTIVITY_EXCESS_TIME] = setting.activity_total_border - self.df[ConstKeys.ADD_ACTIVITY_TIME]
        # print('@@@ = {}'.format(self.df[ConstKeys.ACTIVITY_EXCESS_TIME].dtype))
        # print()

    def check_last_record(self, setting:Setting):
        if self.df.shape[0]>0:
            last_row = self.df.iloc[-1]
            activity_time = setting.now_time - last_row[ConstKeys.START_TIME]
            if activity_time < datetime.timedelta(0):
                activity_time = datetime.timedelta(0)
        else:
            activity_time = datetime.timedelta(0)
        print('activity_time_now = {}'.format(activity_time))


        #/
        now_activity_excess_time = self.df.iloc[-1]
    
    # def is_activity_now(self):
    #     if self.df.shape[0]>0:
    #         last_endt_time = self.df.iloc[-1][ConstKeys.ACTIVE_END_TIME]
    #     else:
    #         return False

    # def get_last_record(self):
    #     if self.df.shape[0]>0:
    #         return self.df.iloc[-1]
    #     else:
    #         return None



class ResultData():
    def __init__(self,df) -> None:
        self.df:pd.DataFrame = df
        self.columns = [
            ConstKeys.MAIN_CD,
            ConstKeys.ACTIVE_START_TIME,
            ConstKeys.ACTIVE_END_TIME,
            ConstKeys.ADD_ACTIVITY_TIME,
            ConstKeys.ADD_INTERVAL_TIME,
            ConstKeys.ADD_INTERVAL_LONG_FLAG,
            ConstKeys.ADD_INTERVAL_NOT_FLAG,
            ConstKeys.ACTIVITY_EXCESS_TIME,
        ]
        self.data_dict = {}
    def get(self, key):
        return self.data_dict.get(key)

    def exact_col(self):
        self.df = self.df[self.columns]
    
    def update(self, key, value=None):
        if isinstance(key, dict):
            self.data_dict.update(key)
        else:
            self.data_dict.update( {key : value} )
    
    def count_data(self, setting:Setting):
        activity_total = self.df[ConstKeys.ADD_ACTIVITY_TIME].sum()
        self.update( {ConstKeys.ACTIVITY_TIME_TOTAL : activity_total} )
        activity_excess_time = setting.activity_total_border - activity_total.to_pytimedelta()
        # activity_total_timedelta = activity_total.to_pytimedelta()
        # activity_excess_count = setting.activity_total_border - activity_total_timedelta
        if activity_excess_time < datetime.timedelta(days=0, hours=0):
            activity_excess_time = datetime.timedelta(hours=0)
        activity_excess_time = format_timedelta(activity_excess_time)
        self.update( {ConstKeys.ACTIVITY_EXCESS_TIME : activity_excess_time} )
        continue_count = (self.df[ConstKeys.ADD_INTERVAL_NOT_FLAG] == True).sum()
        self.update( {ConstKeys.CONTINUE_TIMES : continue_count} )


class ResultFilter():
    def __init__(self, logger:SampleLogger) -> None:
        self.logger = logger
        self.last_ret_list = []
    
    def append(self, ret_data:ResultData):
        self_data:ResultData=None
        for i, self_data in enumerate(self.last_ret_list):
            k = ConstKeys.MAIN_CD
            if self_data.data_dict[k] == ret_data.data_dict[k]:
                self_data.update(ret_data.data_dict)
                break
        else:
            self.last_ret_list.append(ret_data)

    def excute(self,ret_data_list:list[ResultData], setting:Setting):
        match_condition_values = []
        for i, ret_data in enumerate(ret_data_list):
            # if ret_data.data_dict[ConstKeys.MAIN_CD] == '8232':
            #     print()
            match_condition_values = []
            #/
            if ret_data.data_dict[ConstKeys.ACTIVITY_TIME_TOTAL] > setting.activity_total_border:
                ret_data.update(ConstKeys.ACTIVITY_TIME_TOTAL_VALUE, ConstKeys.ACTIVITY_EXCESS_TIME)
                buf_val = int(setting.activity_total_border.total_seconds()/3600)
                buf = '[{}-{}]'.format(ConstKeys.ACTIVITY_TIME_TOTAL, buf_val)
                match_condition_values.append(buf)
            #/
            # print('## {},{}'.format(ret_data.data_dict[ConstKeys.CONTINUE_TIMES] , setting.continue_count_border))
            if ret_data.data_dict[ConstKeys.CONTINUE_TIMES] >= setting.continue_count_border:
                buf_val = ret_data.get(ConstKeys.CONTINUE_TIMES)
                buf = '[{}-{}]'.format(ConstKeys.CONTINUE_TIMES, buf_val)
                match_condition_values.append(buf)
                # ret_data.update(ConstKeys.CONTINUE_TIMES_VALUE, ConstKeys.CONTINUE_TIMES)
            #/
            activity_excess_time = parse_timedelta(ret_data.data_dict[ConstKeys.ACTIVITY_EXCESS_TIME])
            if activity_excess_time > setting.activity_total_border:
                buf_val = int(setting.activity_now_border.total_seconds()/3600)
                buf = '[{}-{}]'.format(ConstKeys.ACTIVITY_EXCESS_TIME, buf_val)
                match_condition_values.append(buf)
            #/
            match_condition_value_all = ''.join(match_condition_values)
            ret_data.update(ConstKeys.MATCH_CONDITIONS, match_condition_value_all)
            self.last_ret_list.append(ret_data)
    
    def debug_print(self):
        ret_data:ResultData=None
        for ret_data in self.last_ret_list:
            print(ret_data.data_dict)
    
    def write_to_file(self, path=None):
        if path==None:
            path = Path(__file__).parent.joinpath('__test_last_result.txt')
        columns = []
        line = []
        is_set_columns = False
        ret_data:ResultData=None
        key_list = [
            ConstKeys.MAIN_CD,
            ConstKeys.MATCH_CONDITIONS,
        ]
        with open(path, 'w', encoding='sjis')as f:
            for ret_data in self.last_ret_list:
                if ret_data.data_dict[ConstKeys.MATCH_CONDITIONS]=='':
                    continue
                line = []
                for key in key_list:
                    line.append(ret_data.data_dict.get(key))
                    if not is_set_columns:
                        columns.append(key)
                if not is_set_columns:
                    w_str = ','.join(columns) + CRLF
                    f.write(w_str)
                    is_set_columns = True
                w_str = ','.join(line) + CRLF
                f.write(w_str)
        self.logger.info('w_path = {}'.format(path))
        
def main():
    logger = SampleLogger()
    setting = Setting()
    df_main = get_main_data_frame()
    main_cd_list = main_cd_list = df_main[ConstKeys.MAIN_CD].astype(str).tolist()
    logger.info('main_cd_list = {}'.format(main_cd_list))

    df = get_time_list_data_frame()
    # logger.info(df)
    logger.info('rows = {}'.format(df.shape[0]))

    setting.now_time = datetime.datetime.strptime('2022/8/1 15:00:00', TIME_FORMAT)
    setting.end_time = setting.now_time
    setting.begin_time = setting.now_time - datetime.timedelta(hours=6)
    time_filter = TimeFilter()
    time_filter.set_values(df, setting.begin_time)
    time_filter.convert_type_str_to_date()
    time_filter.excute_filter()
    logger.info('now_time = {}'.format(setting.now_time))
    logger.info('df.rows={},  time_filter.df.rows={}'.format(df.shape[0], time_filter.df.shape[0]))
    df = time_filter.df

    last_ret_data = ResultFilter(logger)
    main_cd_list = main_cd_list[:1]
    logger.info('begin_time, end_time = {}  ~  {}'.format(
        setting.begin_time, setting.end_time))
    ret_data_list = []
    for main_cd in main_cd_list:
        filter = MainTimeFilter(df)
        filter.convert_type_str_to_date()
        filter.exact_main_cd(main_cd)
        # filter.df.to_csv('__test_csv.csv', encoding='sjis')
        filter.exact_time(setting.begin_time, setting.end_time)
        filter.add_time(setting)
        filter.check_last_record(setting)
        # logger.info(filter.df)
        # logger.info('filter.df.rows={}'.format(filter.df.shape[0]))
        # logger.info(filter.df.dtypes)
        ret_data = ResultData(filter.df)
        ret_data.exact_col()
        # logger.info(ret_data.df)
        ret_data.data_dict.update({ConstKeys.MAIN_CD:main_cd})
        ret_data.data_dict.update({ConstKeys.INIT_ROWS:filter.init_rows})
        ret_data.data_dict.update({ConstKeys.MATCH_ROWS:filter.df.shape[0]})
        ret_data.count_data(setting)
        ret_data_list.append(ret_data)
        logger.info(ret_data.data_dict)

    logger.info('##########')
    last_ret_data.excute(ret_data_list, setting)
    last_ret_data.debug_print()
    last_ret_data.write_to_file()


if __name__ == '__main__':
    main()