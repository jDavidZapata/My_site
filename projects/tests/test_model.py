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
            project_one.technology, "Flask")
        self.assertEqual(
            project_one.goal, "Learn")
        self.assertEqual(
            project_one.image, "default.png")
        self.assertEqual(
            project_two.goal, "Learn")
        self.assertEqual(
            project_one.goal, project_two.goal)
        