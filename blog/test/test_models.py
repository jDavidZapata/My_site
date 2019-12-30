from django.test import TestCase, Client
from ..models import Category, Post, Comment
from django.contrib.auth import get_user_model

# Create your tests here.

USER = 'user@example.com'
PASSWORD = 'pAs$w0rd!!'
EMAIL = 'user@example.com'

NAME1 = 'MAIN'
NAME2 = 'OTHER'
SUMMARY1 = 'Main Category'
SUMMARY2 = 'Other Category'

def create_user(username=USER, password=PASSWORD, email=EMAIL): 
    return get_user_model().objects.create_user(
        username=username, password=password, email=email)


class CategoryModelTest(TestCase):
    """ Test module for Category model. """

    def setUp(self):
        
        user = create_user()

        Category.objects.create(
            author=user, name=NAME1, summary=SUMMARY1)
        Category.objects.create(
            author=user, name=NAME2, summary=SUMMARY2)


    def test_database(self):
        """ Test module for Category database. """

        Category_one = Category.objects.get(name='MAIN')
        Category_two = Category.objects.get(name='OTHER')
        self.assertEqual(
            Category_one.name, "MAIN")
        self.assertEqual(
            Category_one.summary, "Main Category")
        self.assertEqual(
            Category_one.user_id, 1)
        self.assertEqual(
            Category_one.slug, "main")
        self.assertEqual(
            Category_two.user_id, 1)
        self.assertEqual(
            Category_two.name, "OTHER")
        self.assertEqual(
            Category_two.summary, "Other Category")
        self.assertEqual(
            Category_two.slug, "other")