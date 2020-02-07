from django.test import TestCase, Client
from ..models import Project
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from ..views import ProjectListView, ProjectDetailView, ProjectUpdateView, ProjectCreateView, ProjectDelete

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
        

    def test_projects_list_url_resolves_projects_list_view(self):
        view = resolve('/projects/')
        self.assertEquals(view.func.view_class, ProjectListView)


        
class ProjectPageTest(TestCase):
    """ Test module for Projecst Page. """

    def test_project_page_without_project(self):
        """ If no project, then a 404 error. """

        c = Client()
        response = c.get("/projects/project-one/")
        self.assertEqual(response.status_code, 404)
        #self.assertEqual(response.status_code, 200)
            
            
    def test_project_page_with_project(self):
        """ Make Sure project shows on the page. """

        setUp(self)
        project = Project.objects.get(slug='one')
        c = Client()
        response = c.get("/projects/project-one/")
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.context["title"], "Project # 1")
        self.assertEqual(response.context['project'], project)
        self.assertContains(response, project.title)
    

    def test_project_page_url_resolves_project_detail_view(self):
        view = resolve('/projects/project-one/')
        self.assertEquals(view.func.view_class, ProjectDetailView)


class ProjectCreatePageTest(TestCase):
    """ Test module for Project Create Page. """

    def test_project_create_page_without_user(self):
        """ If no user, then redirect. """

        c = Client()
        response = c.get("/create/")
        self.assertEqual(response.status_code, 302)
    
    
    def test_project_create_page(self):
        """ Make Sure Project Create Page Shows. """

        setUp(self)
        c = Client()
        # Log the user in
        c.login(username=USER, password=PASSWORD)
        response = c.get("/create/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('form.html', response.template_name)    
                

    def test_project_create_page_url_resolves_project_create_view(self):
        view = resolve('/create/')
        self.assertEquals(view.func.view_class, ProjectCreateView)




class ProjectUpdatePageTest(TestCase):
    """ Test module for Project Update Page. """

    def test_project_update_page_without_user(self):
        """ If no user, then redirect. """

        c = Client()
        response = c.get("/projects/project-one/update/")
        self.assertEqual(response.status_code, 302)


    def test_project_update_page_without_project(self):
        """ If no post, then a 404 error. """

        user = create_user()
        c = Client()
        # Log the user in
        c.login(username=USER, password=PASSWORD)
        response = c.get("/projects/project-one/update/")
        self.assertEqual(response.status_code, 404)
            
            
    def test_project_update_page_with_project(self):
        """ Make Sure Project Can Be Updated. """

        setUp(self)
        project = Project.objects.get(slug='post-1')
        c = Client()
        # Log the user in
        c.login(username=USER, password=PASSWORD)
        response = c.get("/projects/project-one/update/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('form.html', response.template_name)
    

    def test_project_update_page_url_resolves_project_update_view(self):
        view = resolve('/projects/project-one/update/')
        self.assertEquals(view.func.view_class, ProjectUpdateView)




class ProjectDeletePageTest(TestCase):
    """ Test module for Project Delete Page. """
    
    def test_project_delete_page_without_user(self):
        """ If no user, then redirect. """

        c = Client()
        response = c.get("/projects/project-one/delete/")
        self.assertEqual(response.status_code, 302)

    
    def test_project_delete_page_without_project(self):
        """ If no project, then a 404 error. """

        user = create_user()
        c = Client()
        # Log the user in
        c.login(username=USER, password=PASSWORD)
        response = c.get("/projects/project-one/delete/")
        self.assertEqual(response.status_code, 404)
            
            
    def test_project_delete_page_with_project(self):
        """ Make Sure Project Can Be Deleted. """

        setUp(self)
        project = Project.objects.get(slug='post-1')
        c = Client()
         # Log the user in
        c.login(username=USER, password=PASSWORD)
        response = c.get("/projects/project-one/delete/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('projects/project_delete.html', response.template_name)
        self.assertTemplateUsed(response, 'projects/project_delete.html')
    

    def test_project_delete_page_url_resolves_project_delete_view(self):
        view = resolve('/projects/project-one/delete/')
        self.assertEquals(view.func.view_class, ProjectDelete)



    
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