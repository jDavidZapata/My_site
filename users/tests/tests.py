from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

PASSWORD = 'pAs$w0rd!!'


def create_user(username='user@example.com', password=PASSWORD): # new
    return get_user_model().objects.create_user(
        username=username, password=password)


class AuthenticationTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_user_can_sign_up(self):

        data={
            'username': 'user@example.com',
            'password1': PASSWORD,
            'password2': PASSWORD,
        }
        response = self.client.post(reverse('register_'), data={
            'username': 'user@example.com',
            'password1': PASSWORD,
            'password2': PASSWORD,
        })
        user = get_user_model().objects.last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(data['username'], user.username)


    def test_user_can_log_in(self): 
        data={
            'username': 'user@example.com',
            'password1': PASSWORD,
            'password2': PASSWORD,
        }
        user = create_user()
        response = self.client.post(reverse('login_'), data={
            'username': user.username,
            'password': PASSWORD,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(data['username'], user.username)


    def test_user_can_log_out(self): 
        user = create_user()
        self.client.login(username=user.username, password=PASSWORD)
        response = self.client.post(reverse('logout_'))
        self.assertEqual(response.status_code, 302)