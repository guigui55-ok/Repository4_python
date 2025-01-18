from django.urls import path

from . import view

app_name = "accounts"

urlpatterns = [
    path("", view.IndexView.as_view(), name="index"),
    path('signup/', view.SignupView.as_view(), name="signup"),
    path('login/', view.LoginView.as_view(), name="login"),
    path('logout/', view.LogoutView.as_view(), name="logout"), # 追加
]