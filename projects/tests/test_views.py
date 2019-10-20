from django.test import TestCase, Client

# Create your tests here.
class ProjectsListPageTest(TestCase):
    """ Test module for Projecsts List Page. """
    def test_projects_page(self):
        c = Client()
        response = c.get("/projects/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "Projects")


class ProjectPageTest(TestCase):
    """ Test module for Projecst Page. """
    project_id = 1
    def test_project_page(self):
        c = Client()
        response = c.get("/{project_id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "Project # {project_id}")

