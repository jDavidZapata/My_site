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
Cost1 = ''

TITLE2 = 'Post 2'
PCONTENT2 = 'The second post'
IMAGE2 = 'default.jpeg'
Cost2 = ''


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
    


class PostDetailPageTest(TestCase):
    """ Test module for post Detail Page. """

    def test_post_detail_page_without_post(self):
        """ If no post, then a 404 error. """

        c = Client()
        response = c.get("/personal/blog/category/post-1/")
        self.assertEqual(response.status_code, 404)
            
            
    def test_post_detail_page_with_post(self):
        """ Make Sure post shows on the page. """

        setUp(self)
        post = Post.objects.get(slug='post-1')
        c = Client()
        response = c.get("/personal/blog/category/post-1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'], post)
        #self.assertContains(response, post.title)
        #self.assertContains(response.template_name, 'blog/post_detail.html')
        self.assertIn('blog/post_detail.html', response.template_name)
    

    def test_post_page_url_resolves_post_detail_view(self):
        view = resolve('/personal/blog/category/post-1/')
        self.assertEquals(view.func.view_class, PostDetailView)



class PostUpdatePageTest(TestCase):
    """ Test module for Post Update Page. """

    def test_post_update_page_without_post(self):
        """ If no post, then a 404 error. """

        c = Client()
        response = c.get("/personal/blog/category/post-1/update/")
        self.assertEqual(response.status_code, 302)
            
            
    def test_post_update_page_with_post(self):
        """ Make Sure Post Can Be Updated. """

        setUp(self)
        post = Post.objects.get(slug='post-1')
        c = Client()
        response = c.get("/personal/blog/category/post-1/update/")
        self.assertEqual(response.status_code, 302)
        #self.assertContains(response.template_name, ['form.html'])
        #self.assertIn('form.html', response.template_name)
    

    def test_post_update_page_url_resolves_post_update_view(self):
        view = resolve('/personal/blog/category/post-1/update/')
        self.assertEquals(view.func.view_class, PostUpdateView)


class PostCreatePageTest(TestCase):
    """ Test module for Post Create Page. """
    
    def test_post_create_page(self):
        """ Make Sure Post Create Page Shows. """

        c = Client()
        response = c.get("/personal/blog-post/")
        self.assertEqual(response.status_code, 302)
        #self.assertIn('form.html', response.template_name)    
            
    

    def test_post_create_page_url_resolves_post_create_view(self):
        view = resolve('/personal/blog-post/')
        self.assertEquals(view.func.view_class, PostCreateView)

