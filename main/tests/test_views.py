from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

PASSWORD = 'pAs$w0rd!!'


def create_user(username='user@example.com', password=PASSWORD): # new
    return get_user_model().objects.create_user(
        username=username, password=password)



class MainPageTest(TestCase):
    """ Test module for Main Page. """
    def test_index_page(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["body"], "Body: HELLO WORLD!!!")


class ContactPageTest(TestCase):
    """ Test module for Contact Page. """
    def test_contact_page(self):
        c = Client()
        response = c.get("/contact/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "Contact")
        self.assertEqual(response.context["body"], "Body: How to Contact ME")
        self.assertEqual(response.context["content"], "732 or 201")


class AboutPageTest(TestCase):
    """ Test module for About Page. """
    def test_about_page(self):
        c = Client()
        response = c.get("/about/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "About")
        self.assertEqual(response.context["body"], "Body: About ME!!!")
        

class ResumePageTest(TestCase):
    """ Test module for Resume Page. """
    def test_resume_page(self):
        c = Client()
        response = c.get("/resume/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "Resume")
        self.assertEqual(response.context["body"], "Body: My resume")
        

class PersonalPageTest(TestCase):
    """ Test module for Personal Page. """
    def test_personal_page(self):
        c = Client()
        response = c.get("/personal/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "Temporary")
        self.assertEqual(response.context["body"], "Body: Temp Page")
        

class AuthenticationTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_user_can_sign_up(self):

        data={
            'username': 'user@example.com',
            'password1': PASSWORD,
            'password2': PASSWORD,
        }
        c = Client()
        response = c.post(reverse('main:registerpage'), data={
            'username': 'user@example.com',
            'password1': PASSWORD,
            'password2': PASSWORD,
        })
        user = get_user_model().objects.last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(data['username'], user.username)
        #self.assertEqual(data['first_name'], user.first_name)
        #self.assertEqual(data['last_name'], user.last_name)


    def test_user_can_log_in(self): 
        data={
            'username': 'user@example.com',
            'password1': PASSWORD,
            'password2': PASSWORD,
        }
        user = create_user()
        response = self.client.post(reverse('main:loginpage'), data={
            'username': user.username,
            'password': PASSWORD,
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['username'], user.username)


    def test_user_can_log_out(self): 
        user = create_user()
        self.client.login(username=user.username, password=PASSWORD)
        response = self.client.post(reverse('main:logoutpage'))
        self.assertEqual(response.status_code, 302)