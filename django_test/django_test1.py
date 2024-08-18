

"""

https://qiita.com/pythonista/items/19613663ef7bb3c57d4f
 pip install django

 djangoプロジェクトの作成
 django-admin startproject test_project1

一階層目の ディレクトリに移動して以降の各種設定を行います。
cd test_project1


 プロジェクト設定
config/settings.py 変更

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ja'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tokyo'



migrate Postgre
https://qiita.com/honda28/items/d5bf743c3c244791f559


https://qiita.com/prg_mt/items/c5c8edbf45dfe87b54ef



SQLiteの場合
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

PostgreSQLの場合
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': [database_name],
        'USER': [user_name],
        'PASSWORD': [password],
        'HOST': ***.amazonaws.com,
        'PORT': '5432'
    }
}

cd test_project1
python manage.py dbshell

*****
PS C:\Users\OK\source\repos\Repository4_python\django_test\test_project1> python manage.py dbshell
psql (16.3)
"help"でヘルプを表示します。

sampledb=# exit

******

pip install psycopg2

python manage.py makemigrations


"""

def _test_main():
    pass


if __name__ == '__main__':
    _test_main()