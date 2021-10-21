import time


def test_unix_time():
    # UNIX時間（エポック秒）を取得する
    ut = time.time()
    print(ut)
    # float型で取得されている
    print(type(ut))

test_unix_time()

import datetime
def test_datetime():
    # 現在日時（日付と時刻）を取得する
    dt_now = datetime.datetime.now()
    # 2019-02-04 21:04:15.412854
    print(dt_now)
    # <class 'datetime.datetime'>
    print(type(dt_now))
    # 2019年02月04日 21:04:15
    print(dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
    # 2019-02-04T21:04:15.412854
    print(dt_now.isoformat())
    print(dt_now.year)
    print(dt_now.month)
    print(dt_now.day)
    print(dt_now.hour)
    print(dt_now.minute)
    print(dt_now.second)
    print(dt_now.microsecond)

test_datetime()