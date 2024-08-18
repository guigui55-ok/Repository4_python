
class ConstPostgreSql:
    KEY_ENGINE = 'ENGINE'
    KEY_NAME = 'NAME'
    KEY_USER = 'USER'
    KEY_PASSWORD = 'PASSWORD'
    KEY_HOST = 'HOST'
    KEY_PORT = 'PORT'
    KEY_DEFAULT = 'default'

def get_database_info_postgre_default():
    DATABASES = {
        ConstPostgreSql.KEY_DEFAULT : {
            ConstPostgreSql.KEY_ENGINE : 'django.db.backends.postgresql',
            ConstPostgreSql.KEY_NAME : 'sampledb',
            ConstPostgreSql.KEY_USER : 'postgres',
            ConstPostgreSql.KEY_PASSWORD : 'Faverz41@',
            ConstPostgreSql.KEY_HOST : 'localhost',
            ConstPostgreSql.KEY_PORT : '5432'
        }
    }
    return DATABASES
"""
pip install psycopg2-binary

"""