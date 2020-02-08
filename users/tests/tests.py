from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from ..models import Profile
from django.urls import reverse, resolve
from ..views import UserRegistration

# Create your tests here.

USER = 'user@example.com'
USER2 = 'oteruser@example.com'
PASSWORD = 'pAs$w0rd!!'
EMAIL = 'user@example.com'


def create_user(username=USER, password=PASSWORD, email=EMAIL): 
    return get_user_model().objects.create_user(
        username=username, password=password, email=email)

def create_user2(username=USER2, password=PASSWORD, email=EMAIL): 
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

    def test_user_sign_up_page_url_resolves_user_signup_view(self):
        view = resolve('/register/')
        self.assertEquals(view.func.view_class, register)

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

    def test_user_sign_up_page_url_resolves_user_signup_view(self):
        view = resolve('/register/')
        self.assertEquals(view.func.view_class, UserRegistration)

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
        """ Test users has profile. """
        
        user = create_user()
        self.client.login(username=user.username, password=PASSWORD)

        profile_one = Profile.objects.get(user=user)
            
        data={
            'username': 'user@example.com',
            'email': 'user@example.com',
            'password': PASSWORD,
            'image': 'default.jpg'
        }
        response = self.client.get(reverse('users:profile'), instance=profile_one)

        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['username'], profile_one.user.username)
        self.assertEqual(data['image'], profile_one.user.profile.image)
    

    def test_different_user_profiles(self):
        """ Test users different profile. """
        
        user = create_user()
        user2 =create_user2()
        self.client.login(username=user2.username, password=PASSWORD)

        profile_one = Profile.objects.get(user=user)
        profile_two = Profile.objects.get(user=user2)
            
        data={
            'username': 'user@example.com',
            'email': 'user@example.com',
            'password': PASSWORD,
        }
        response = self.client.post(reverse('users:profile'), data={
            'username': 'user@example.com',
            'password': PASSWORD,
            'image': 'defaul2.jpg'
        })

        print(response.request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['username'], profile_one.user.username)
        self.assertNotEqual(profile_one.user.username, profile_two.user.username)
        #self.assertNotEqual(profile_one.user.profile.image, profile_two.user.profile.image)
        #self.assertEqual(response.request.username, profile_two.user.username)


def test_not_login_user_profile(self):
        """ Test user not log in to view profile. """
        
        user = create_user()
        
        profile_one = Profile.objects.get(user=user)
        
        data={
            'username': 'user@example.com',
            'email': 'user@example.com',
            'password': PASSWORD,
        }
        response = self.client.get(reverse('users:profile'))

        print(response)
        self.assertEqual(response.status_code, 302)
        