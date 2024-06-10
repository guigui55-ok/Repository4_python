

import pandas as pd
from pathlib import Path

import datetime

def get_main_data_frame():
    csv_path_a = str(Path(__file__).parent.joinpath('__sample_data.csv'))
    df = pd.read_csv(csv_path_a)
    return df

def get_time_list_data_frame():
    csv_path_b = str(Path(__file__).parent.joinpath('__sample_non_overlapping_times_data_v4.csv'))
    df = pd.read_csv(csv_path_b)
    return df

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
    CONTINUE_TIMES = '連続活動回数'
    MATCH_ROWS = '行数'
    # 合計回数
    # 合計時間

class SampleLogger():
    def __init__(self) -> None:
        pass
    def info(self, value):
        print(str(value))

class Setting():
    def __init__(self) -> None:
        self.begin_time = datetime.datetime(2022,8,1,0,0,0)
        self.end_time = self.begin_time + datetime.timedelta(hours=6)
        self.interval_border = datetime.timedelta(hours=1)
        self.continue_border = datetime.timedelta(minutes=30)

class MainTimeFilter():
    def __init__(self, df) -> None:
        self.df:pd.DataFrame = df
    
    def convert_type_str_to_date(self):
        self.df[ConstKeys.START_TIME] = pd.to_datetime(self.df[ConstKeys.START_TIME])
        self.df[ConstKeys.END_TIME] = pd.to_datetime(self.df[ConstKeys.END_TIME])
        self.df[ConstKeys.ACTIVE_START_TIME] = pd.to_datetime(self.df[ConstKeys.ACTIVE_START_TIME])
        self.df[ConstKeys.ACTIVE_END_TIME] = pd.to_datetime(self.df[ConstKeys.ACTIVE_END_TIME])

    def exact_main_cd(self, main_cd:int):
        self.df = self.df[self.df[ConstKeys.MAIN_CD] == int(main_cd)]

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
        self.df.loc[self.df.index[0], ConstKeys.ADD_INTERVAL_NOT_FLAG] = False
        # print(self.df[ConstKeys.ADD_INTERVAL_NOT_FLAG])

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
            ConstKeys.ADD_INTERVAL_NOT_FLAG
        ]
        self.data_dict = {}
    
    def exact_col(self):
        self.df = self.df[self.columns]
    
    def count_data(self):
        activity_total = self.df[ConstKeys.ADD_ACTIVITY_TIME].sum()
        self.data_dict.update( {ConstKeys.ACTIVITY_TIME_TOTAL : activity_total} )
        continue_count = (self.df[ConstKeys.ADD_INTERVAL_NOT_FLAG] == True).sum()
        self.data_dict.update( {ConstKeys.CONTINUE_TIMES : continue_count} )

def main():
    logger = SampleLogger()
    setting = Setting()
    df_main = get_main_data_frame()
    main_cd_list = main_cd_list = df_main[ConstKeys.MAIN_CD].astype(str).tolist()
    logger.info('main_cd_list = {}'.format(main_cd_list))

    df = get_time_list_data_frame()
    # logger.info(df)
    logger.info('rows = {}'.format(df.shape[0]))

    # main_cd_list = main_cd_list[:1]
    for main_cd in main_cd_list:
        filter = MainTimeFilter(df)
        filter.convert_type_str_to_date()
        filter.exact_main_cd(main_cd)
        filter.exact_time(setting.begin_time, setting.end_time)
        filter.add_time(setting)
        # logger.info(filter.df)
        # logger.info('filter.df.rows={}'.format(filter.df.shape[0]))
        ret_data = ResultData(filter.df)
        ret_data.exact_col()
        # logger.info(ret_data.df)
        ret_data.data_dict.update({ConstKeys.MAIN_CD:main_cd})
        ret_data.data_dict.update({ConstKeys.MATCH_ROWS:filter.df.shape[0]})
        ret_data.count_data()
        logger.info(ret_data.data_dict)


if __name__ == '__main__':
    main()