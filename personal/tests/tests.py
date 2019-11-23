from django.test import TestCase, Client

# Create your tests here.

class PersonalPageTest(TestCase):
    """ Test module for Personal Page. """
    def test_personal_page(self):
        c = Client()
        response = c.get("/personal/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "Temporary")
        self.assertEqual(response.context["body"], "Body: Temp Page")