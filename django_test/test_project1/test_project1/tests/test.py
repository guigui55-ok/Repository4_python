from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class SimpleLoginTests(TestCase):

    def setUp(self):
        # テスト用ユーザーを作成
        self.username = 'testuser'
        self.password = 'TestPass123!'
        self.user = User.objects.create_user(username=self.username, email='test@example.com', password=self.password)
        self.client = Client()

    def test_index_page_not_logged_in(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ログイン')
        self.assertContains(response, 'サインイン')

    def test_index_page_logged_in(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.username)
        self.assertContains(response, 'メンバー専用ページへ')
        self.assertContains(response, 'ログアウト')

    def test_login_success(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertRedirects(response, reverse('members'))

    def test_login_failure(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ログイン失敗')

    def test_logout(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('index'))
        # ログアウト後は未ログイン状態になる
        response2 = self.client.get(reverse('index'))
        self.assertContains(response2, 'ログイン')

    def test_signin_success(self):
        new_email = 'newuser@example.com'
        new_username = 'newuser'
        response = self.client.post(reverse('signin'), {
            'username': new_username,
            'email': new_email,
            'password1': 'NewPass123!',
            'password2': 'NewPass123!',
        })
        self.assertRedirects(response, reverse('members'))
        # ユーザーが作成されていること
        self.assertTrue(User.objects.filter(username=new_username).exists())

    def test_signin_password_mismatch(self):
        response = self.client.post(reverse('signin'), {
            'username': 'anotheruser',
            'email': 'another@example.com',
            'password1': 'Pass123!',
            'password2': 'Mismatch123!',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'パスワード')

    def test_members_page_requires_login(self):
        response = self.client.get(reverse('members'))
        # 未ログイン時はリダイレクトされる想定
        self.assertNotEqual(response.status_code, 200)

        # ログインしたらアクセス可能
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('members'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.username)