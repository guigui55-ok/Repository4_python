from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # name = 'accounts'
    name = 'accounts'  # アプリのフルパス
    label = 'accounts'  # 一意のラベルを追加
