from django.test import TestCase, Client
from ..models import Category, Post, Comment
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from ..views import CommentListView, CommentDetailView, CommentUpdateView, CommentCreateView, CommentDelete

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
Post1 = ''

TITLE2 = 'Post 2'
PCONTENT2 = 'The second post'
IMAGE2 = 'default.jpeg'
Post2 = ''


def create_user(username=USER, password=PASSWORD, email='user@example.com'): 
    return get_user_model().objects.create_user(
        username=username, password=password, email=email)


def setUp(self):

        user = create_user()

        Category1 = Category.objects.create(
            author=user, name=NAME1, summary=SUMMARY1)
        Category2 = Category.objects.create(
            author=user, name=NAME2, summary=SUMMARY2)

        Post.objects.create(
            author=user, title=TITLE1, content=PCONTENT1, category=Category1)
        Post.objects.create(
            author=user, title=TITLE2, content=PCONTENT2, image=IMAGE2, category=Category2)



class CommentCreatePageTest(TestCase):
    """ Test module for Comment Create Page. """
    
    def test_comment_create_page(self):
        """ Make Sure Comment Create Page Shows. """

        c = Client()
        response = c.get("/personal/blog-comment/")
        self.assertEqual(response.status_code, 302)
        #self.assertIn('form.html', response.template_name)    
            
    

    def test_comment_create_page_url_resolves_comment_create_view(self):
        view = resolve('/personal/blog-comment/')
        self.assertEquals(view.func.view_class, CommentCreateView)
