from django.test import TestCase, Client
from ..models import Category, Post, Comment
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from ..views import PostListView, PostDetailView, PostUpdateView, PostCreateView, PostDelete

# Create your tests here.

#User
USER = 'user@example.com'
PASSWORD = 'pAs$w0rd!!'
EMAIL = 'user@example.com'

#Category
NAME1 = 'MAIN'
NAME2 = 'OTHER'
SUMMARY1 = 'Main Category'
SUMMARY2 = 'Other Category'

#Posts
TITLE1 = 'Post 1'
PCONTENT1 = 'The first post'
CATEGORY1 = ''

TITLE2 = 'Post 2'
PCONTENT2 = 'The second post'
IMAGE2 = 'default.jpeg'
CATEGORY2 = ''


def create_user(username=USER, password=PASSWORD, email='user@example.com'): 
    return get_user_model().objects.create_user(
        username=username, password=password, email=email)


def setUp(self):

        user = create_user()

        CATEGORY1 = Category.objects.create(
            author=user, name=NAME1, summary=SUMMARY1)
        CATEGORY2 = Category.objects.create(
            author=user, name=NAME2, summary=SUMMARY2)

        Post.objects.create(
            author=user, title=TITLE1, content=PCONTENT1, category=CATEGORY1)
        Post.objects.create(
            author=user, title=TITLE2, content=PCONTENT2, image=IMAGE2, category=CATEGORY2)


class PostsListPageTest(TestCase):
    """ Test module for Post List Page. """

    def test_post_list_page_without_Post(self):
        """ If no Posts exist, an appropriate message is displayed. """
        
        c = Client()
        response = c.get("/personal/blog/")
        self.assertEqual(response.status_code, 200)
        


    def test_post_list_page_with_post(self):
        """ Make Sure Posts show on the page. """

        setUp(self)
        c = Client()
        response = c.get("/personal/blog/")
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.template_name, ['blog/posts_list.html'])
        self.assertIn('blog/posts_list.html', response.template_name)
        #self.assertEqual(response.context["posts"], "* Posts *")
    