from django.test import TestCase, Client
from ..models import Project

# Create your tests here.

class ProjectModelTest(TestCase):
    """ Test module for Project model """

    def setUp(self):
        Project.objects.create(
            title='One', description='First Project', technology='Flask', goal='Learn', image='default.png')
        Project.objects.create(
            title='Two', description='Second Project', technology='Django', goal='Learn', image='default.png')


    def test_database(self):
        project_one = Project.objects.get(title='One')
        project_two = Project.objects.get(title='Two')
        self.assertEqual(
            project_one.description, "First Project")
        self.assertEqual(
            project_two.goal, "Learn")
        self.assertEqual(
            project_one.goal, project_two.goal)
        


class ProjectsListPageTest(TestCase):
    """ Test module for Projecsts List Page. """

    def setUp(self):
        Project.objects.create(
            title='One', description='First Project', technology='Flask', goal='Learn', image='default.png')
        Project.objects.create(
            title='Two', description='Second Project', technology='Django', goal='Learn', image='default.png')



    def test_projects_page(self):
        c = Client()
        response = c.get("/projects/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "Projects")


class ProjectPageTest(TestCase):
    """ Test module for Projecst Page. """

    def setUp(self):
        Project.objects.create(
            title='One', description='First Project', technology='Flask', goal='Learn', image='default.png')
        Project.objects.create(
            title='Two', description='Second Project', technology='Django', goal='Learn', image='default.png')



    def test_project_page(self):
        c = Client()
        response = c.get("/projects/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "Project # 1")

