from django.test import TestCase, Client
from ..models import Project
from django.contrib.auth import get_user_model

# Create your tests here.

PASSWORD = 'pAs$w0rd!!'

def create_user(username='user@example.com', password=PASSWORD, email='user@example.com'): 
    return get_user_model().objects.create_user(
        username=username, password=password)


def setUp(self):

        user = create_user()
        Project.objects.create(
            user=user, title='One', description='First Project', technology='Flask', goal='Learn', image='default.png')
        Project.objects.create(
            user=user, title='Two', description='Second Project', technology='Django', goal='Learn', image='default.png')


class ProjectsListPageTest(TestCase):
    """ Test module for Projecsts List Page. """

    def test_projects_page_without_projects(self):
        """
         If no projects exist, an appropriate message is displayed.
        """
        c = Client()
        response = c.get("/projects/")
        self.assertEqual(response.status_code, 404)
        


    def test_projects_page_with_projects(self):
        """
        Make Sure projects show on the page.
        """
        setUp(self)
        c = Client()
        response = c.get("/projects/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "* Projects *")
        

        
class ProjectPageTest(TestCase):
    """ Test module for Projecst Page. """

    def test_project_page_without_project(self):
        """
        If no project, then a 404 error.
        """
        c = Client()
        response = c.get("/projects/1/")
        self.assertEqual(response.status_code, 404)
            
            
    def test_project_page_with_project(self):
        """
        Make Sure project shows on the page.
        """
        setUp(self)
        project = Project.objects.get(pk=1)
        c = Client()
        response = c.get("/projects/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "Project # 1")
        self.assertEqual(response.context['project'], project)
        self.assertContains(response, project.title)
    
    