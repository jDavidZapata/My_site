from django.test import TestCase, Client

# Create your tests here.
class MainSiteTestCase(TestCase):

    def test_index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["body"], "Body: HELLO WORLD!!!")
