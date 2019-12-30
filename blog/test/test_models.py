from django.test import TestCase, Client
from ..models import Category, Post, Comment
from django.contrib.auth import get_user_model

# Create your tests here.

#User
USER = 'user@example.com'
PASSWORD = 'pAs$w0rd!!'
EMAIL = 'user@example.com'

#Categorys
NAME1 = 'MAIN'
NAME2 = 'OTHER'
SUMMARY1 = 'Main Category'
SUMMARY2 = 'Other Category'

#Posts
TITLE1 = 'Post 1'
CONTENT1 = 'The first post'
CATEGORY1 = ''

TITLE2 = 'Post 2'
CONTENT2 = 'The second post'
IMAGE2 = 'default.jpeg'
CATEGORY2 = ''


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
            Category_one.author_id, 1)
        self.assertEqual(
            Category_one.slug, "main")
        self.assertEqual(
            Category_two.author_id, 1)
        self.assertEqual(
            Category_two.name, "OTHER")
        self.assertEqual(
            Category_two.summary, "Other Category")
        self.assertEqual(
            Category_two.slug, "other")




class PostModelTest(TestCase):
    """ Test module for Post model. """

    def setUp(self):
        
        user = create_user()

        CATEGORY1 = Category.objects.create(
            author=user, name=NAME1, summary=SUMMARY1)
        CATEGORY2 = Category.objects.create(
            author=user, name=NAME2, summary=SUMMARY2)

        Post.objects.create(
            author=user, title=TITLE1, content=CONTENT1, category=CATEGORY1)
        Post.objects.create(
            author=user, title=TITLE2, content=CONTENT2, image=IMAGE2, category=CATEGORY2)



    def test_database(self):
        """ Test module for Post database. """

        Post_one = Post.objects.get(title=TITLE1)
        Post_two = Post.objects.get(title=TITLE2)
        self.assertEqual(
            Post_one.title, 'Post 1')
        self.assertEqual(
            Post_one.content, 'The first post')
        self.assertEqual(
            Post_one.category.name, "MAIN")
        self.assertEqual(
            Post_one.category.summary, "Main Category")
        self.assertEqual(
            Post_one.author_id, 1)
        self.assertEqual(
            Post_one.slug, "post-1")
        self.assertEqual(
            Post_two.author_id, 1)
        self.assertEqual(
            Post_two.title, 'Post 2')
        self.assertEqual(
            Post_two.category.name, "OTHER")
        self.assertEqual(
            Post_two.category.summary, "Other Category")
        self.assertEqual(
            Post_two.slug, "post-2")