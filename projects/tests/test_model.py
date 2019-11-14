from django.test import TestCase, Client
from ..models import Project
from django.contrib.auth import get_user_model

# Create your tests here.

USER = 'user@example.com'
PASSWORD = 'pAs$w0rd!!'
EMAIL = 'user@example.com'

def create_user(username=USER, password=PASSWORD, email=EMAIL): 
    return get_user_model().objects.create_user(
        username=username, password=password, email=email)


class ProjectModelTest(TestCase):
    """ Test module for Project model. """

    def setUp(self):
        
        user = create_user()
        Project.objects.create(
            user=user, title='One', description='First Project', technology='Flask', goal='Learn', image='default.png')
        Project.objects.create(
            user=user, title='Two', description='Second Project', technology='Django', goal='Learn', image='default.png')


    def test_database(self):
        """ Test module for Project database. """

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
            project_two.user_id, 1)
        self.assertEqual(
            project_one.goal, project_two.goal)
        