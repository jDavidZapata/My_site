from django.test import TestCase, Client
from ..models import Project
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

USER = 'user@example.com'
PASSWORD = 'pAs$w0rd!!'
EMAIL = 'user@example.com'

def create_user(username=USER, password=PASSWORD, email='user@example.com'): 
    return get_user_model().objects.create_user(
        username=username, password=password, email=email)


def setUp(self):

        user = create_user()
        Project.objects.create(
            user=user, title='One', description='First Project', technology='Flask', goal='Learn', image='default.png')
        Project.objects.create(
            user=user, title='Two', description='Second Project', technology='Django', goal='Learn', image='default.png')


class ProjectsListPageTest(TestCase):
    """ Test module for Projecsts List Page. """

    def test_projects_page_without_projects(self):
        """ If no projects exist, an appropriate message is displayed. """
        
        c = Client()
        response = c.get("/projects/")
        #self.assertEqual(response.status_code, 404)
        self.assertEqual(response.status_code, 200)
        


    def test_projects_page_with_projects(self):
        """ Make Sure projects show on the page. """

        setUp(self)
        c = Client()
        response = c.get("/projects/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "* Projects *")
        

        
class ProjectPageTest(TestCase):
    """ Test module for Projecst Page. """

    def test_project_page_without_project(self):
        """ If no project, then a 404 error. """

        c = Client()
        response = c.get("/projects/1/")
        self.assertEqual(response.status_code, 404)
        #self.assertEqual(response.status_code, 200)
            
            
    def test_project_page_with_project(self):
        """ Make Sure project shows on the page. """

        setUp(self)
        project = Project.objects.get(pk=1)
        c = Client()
        response = c.get("/projects/1/")
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.context["title"], "Project # 1")
        self.assertEqual(response.context['project'], project)
        self.assertContains(response, project.title)
    
    
'''
class LoginRequiredViewTests(TestCase):

    def test_redirection(self):

        """ Test if only logged in users can edit the posts. """

        setUp(self)

        login_url = reverse('users:login')
        url =  "/projects/1/update/"
        #url = reverse('projects:project_update', kwargs={'pk': self.id})
        response = self.client.get(url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=url))


'''