from django.test import TestCase, Client

# Create your tests here.
class ProjectsListPageTest(TestCase):
    """ Test module for Projecsts List Page. """
    def test_projects_page(self):
        c = Client()
        response = c.get("/projects/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "Projects")

