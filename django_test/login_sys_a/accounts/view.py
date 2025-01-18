from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm

from .forms import SignUpForm, LoginFrom # ログインフォームをimport
#Logout
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView

import logging
from logging import getLogger
logger = getLogger(__name__)
# コンソール出力用のハンドラーを作成
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # ハンドラーのログレベルを設定
# フォーマットを定義
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
# ハンドラーをロガーに追加
logger.addHandler(console_handler)
print("set logger - " + '{}'.format(logger.name))


class IndexView(TemplateView):
    """ ホームビュー """
    template_name = "index.html"

    # index.html表示時に ボタンが表示されずNoneとなるため、以下の処理を追加
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.info(f"User: {self.request.user}, Authenticated: {self.request.user.is_authenticated}")
        print(f"User: {self.request.user}, Authenticated: {self.request.user.is_authenticated}")
        return context


class SignupView(CreateView):
    """ ユーザー登録用ビュー """
    form_class = SignUpForm # 作成した登録用フォームを設定
    template_name = "accounts/signup.html" 
    success_url = reverse_lazy("accounts:index") # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        account_id = form.cleaned_data.get("account_id")
        password = form.cleaned_data.get("password1")
        user = authenticate(account_id=account_id, password=password)
        login(self.request, user)
        return response

# ログインビューを作成
class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = "accounts/login.html"

# LogoutViewを追加
class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("accounts:index")