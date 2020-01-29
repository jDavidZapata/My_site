from django.test import TestCase, Client
from ..models import Category, Post, Comment
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from ..views import CommentsListView, CommentDetailView, CommentUpdateView, CommentCreateView, CommentDelete

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
        response = c.get("/personal/blog-create-comment/")
        self.assertEqual(response.status_code, 302)
        #self.assertIn('form.html', response.template_name)    
            
    

    def test_comment_create_page_url_resolves_comment_create_view(self):
        view = resolve('/personal/blog-create-comment/')
        self.assertEquals(view.func.view_class, CommentCreateView)




class CommentsListPageTest(TestCase):
    """ Test module for Comment List Page. """

    def test_comment_list_page_without_comment(self):
        """ If no comment exist, an appropriate message is displayed. """
        
        c = Client()
        response = c.get("/personal/blog-comments/")
        self.assertEqual(response.status_code, 200)
        


    def test_comment_list_page_with_comment(self):
        """ Make Sure comment show on the page. """

        setUp(self)
        c = Client()
        response = c.get("/personal/blog-comments/")
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.template_name, ['blog/comments_list.html'])
        self.assertIn('blog/comments_list.html', response.template_name)
        #self.assertEqual(response.context["comments"], "* Comments *")
    


class CommentDetailPageTest(TestCase):
    """ Test module for comment Detail Page. """

    def test_comment_detail_page_without_comment(self):
        """ If no comment, then a 404 error. """

        c = Client()
        response = c.get("/personal/blog-comment/1")
        self.assertEqual(response.status_code, 404)
            
            
    def test_comment_detail_page_with_comment(self):
        """ Make Sure comment shows on the page. """

        setUp(self)
        comment = Comment.objects.get(slug='1')
        c = Client()
        response = c.get("/personal/blog-comment/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['comment'], comment)
        #self.assertContains(response.template_name, 'blog/comment_detail.html')
        self.assertIn('blog/comment_detail.html', response.template_name)
    

    def test_comment_page_url_resolves_comment_detail_view(self):
        view = resolve('/personal/blog-comment/1')
        self.assertEquals(view.func.view_class, CommentDetailView)



class CommentUpdatePageTest(TestCase):
    """ Test module for Comment Update Page. """

    def test_comment_update_page_without_comment(self):
        """ If no comment, then a 404 error. """

        c = Client()
        response = c.get("/personal/blog-comment-update/1")
        self.assertEqual(response.status_code, 302)
            
            
    def test_comment_update_page_with_comment(self):
        """ Make Sure Comment Can Be Updated. """

        setUp(self)
        comment = Comment.objects.get(slug='1')
        c = Client()
        response = c.get("/personal/blog-comment-update/1")
        self.assertEqual(response.status_code, 302)
        #self.assertContains(response.template_name, ['form.html'])
        #self.assertIn('form.html', response.template_name)
    

    def test_comment_update_page_url_resolves_comment_update_view(self):
        view = resolve('/personal/blog-comment-update/1')
        self.assertEquals(view.func.view_class, CommentUpdateView)