# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group


from .models import User
from django.contrib.auth.admin import UserAdmin  # UserAdmin をインポート
# Django では、UserAdmin は標準的な User モデルの管理画面を提供するためのクラスとして定義されています。
# このクラスをインポートすることで、Django 管理画面にカスタムユーザーモデルを登録できるようになります。

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    # 管理画面で使用するフィールドのカスタマイズ
    ordering = ['account_id']  # デフォルトの並び順
    list_display = ['account_id', 'email', 'is_staff', 'is_active']  # リストビューのカラム
    search_fields = ['account_id', 'email']  # 検索可能なフィールド

    # # フォームのレイアウトをカスタマイズ
    # fieldsets = (
    #     (None, {'fields': ('account_id', 'email', 'password')}),
    #     ('Personal Info', {'fields': ('first_name', 'last_name', 'birth_date')}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    #     ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('account_id', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
    #     }),
    # )

    # 必要なフィールドのみ指定
    fieldsets = (
        (None, {"fields": ("account_id", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "birth_date")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)}),
    )
    # リストに表示するフィールド
    list_display = ("account_id", "email", "first_name", "last_name", "is_staff")
    search_fields = ("account_id", "email", "first_name", "last_name")
    ordering = ("account_id",)
    
    readonly_fields = ("created_at",)  # 編集不可に設定


admin.site.register(User, UserAdmin)  # Userモデルを登録
admin.site.unregister(Group)  # Groupモデルは不要のため非表示にします
