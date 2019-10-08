from django.test import TestCase, Client

# Create your tests here.
class MainPageTest(TestCase):
    """ Test module for Main Page. """
    def test_index_page(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["body"], "Body: HELLO WORLD!!!")


class ContactPageTest(TestCase):

    def test_contact_page(self):
        c = Client()
        response = c.get("/contact/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "Contact")
        self.assertEqual(response.context["body"], "Body: How to Contact ME")
        self.assertEqual(response.context["content"], "732 or 201")


class AboutPageTest(TestCase):

    def test_about_page(self):
        c = Client()
        response = c.get("/about/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "About")
        self.assertEqual(response.context["body"], "Body: About ME!!!")
        

