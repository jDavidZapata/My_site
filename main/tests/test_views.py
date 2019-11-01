from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

PASSWORD = 'pAssw0rd!'


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
        c = Client()
        response = c.post(reverse('sign_up'), data={
            'username': 'user@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': PASSWORD,
            'password2': PASSWORD,
        })
        user = get_user_model().objects.last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['first_name'], user.first_name)
        self.assertEqual(response.data['last_name'], user.last_name)