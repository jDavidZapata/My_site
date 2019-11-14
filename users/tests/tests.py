from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

USER = 'user@example.com'
PASSWORD = 'pAs$w0rd!!'
EMAIL = 'user@example.com'


def create_user(username=USER, password=PASSWORD, email=EMAIL): 
    return get_user_model().objects.create_user(
        username=username, password=password, email=email)


class AuthenticationTest(TestCase):
    """ Test module for Users Authentication. """

    def setUp(self):
        self.client = Client()

    def test_user_can_sign_up(self):
        """ Test users are able to signup. """

        data={
            'username': 'user@example.com',
            'email': 'user@example.com',
            'password1': PASSWORD,
            'password2': PASSWORD,
        }
        response = self.client.post(reverse('users:register'), data={
            'username': 'user@example.com',
            'email': 'user@example.com',
            'password1': PASSWORD,
            'password2': PASSWORD,
        })
        user = get_user_model().objects.last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(data['username'], user.username)


    def test_user_can_log_in(self): 
        """ Test users are able to login. """

        data={
            'username': 'user@example.com',
            'email': 'user@example.com',
            'password1': PASSWORD,
            'password2': PASSWORD,
        }
        user = create_user()
        response = self.client.post(reverse('users:login'), data={
            'username': user.username,
            'password': PASSWORD,
            'email': 'user@example.com',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(data['username'], user.username)


    def test_user_can_log_out(self): 
        """ Test users are able to logout. """

        user = create_user()
        self.client.login(username=user.username, password=PASSWORD)
        response = self.client.post(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)


class ProfileTest(TestCase):
    """ Test module for Users Profile. """

    def setUp(self):
        self.client = Client()

    def test_user_profile(self):
        """ Test users can see profile. """
        
        user = create_user()
        data={
            'username': 'user@example.com',
            'email': 'user@example.com',
            'password1': PASSWORD,
            'password2': PASSWORD,
        }
        response = self.client.post(reverse('users:profile'), data={
            'username': 'user@example.com',
            'email': 'user@example.com',
            'password1': PASSWORD,
            'password2': PASSWORD,
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(data['username'], user.username)
        #self.assertEqual(response.instance.user.username, user.username)
