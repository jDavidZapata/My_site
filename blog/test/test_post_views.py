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


class PostsListPageTest(TestCase):
    """ Test module for Post List Page. """

    def test_post_list_page_without_post(self):
        """ If no Posts exist, an appropriate message is displayed. """
        
        c = Client()
        response = c.get("/personal/blog/")
        self.assertEqual(response.status_code, 200)        


    def test_post_list_page_with_post(self):
        """ Make Sure Posts show on the page. """

        setUp(self)
        post = Post.objects.get(slug='post-1')
        c = Client()
        response = c.get("/personal/blog/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('blog/posts_list.html', response.template_name)
        self.assertIn(post, response.context["posts"])   
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == False)
        self.assertTrue(len(response.context['posts']) == 2) 

    
    def test_post_page_url_resolves_post_list_view(self):
        view = resolve('/personal/blog/')
        self.assertEquals(view.func.view_class, PostListView)


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
        self.assertIn(post.title, response.context['post'].title)
        self.assertIn('blog/post_detail.html', response.template_name)
    

    def test_post_page_url_resolves_post_detail_view(self):
        view = resolve('/personal/blog/category/post-1/')
        self.assertEquals(view.func.view_class, PostDetailView)


class PostUpdatePageTest(TestCase):
    """ Test module for Post Update Page. """

    def test_post_update_page_without_user(self):
        """ If no user, then redirect. """

        c = Client()
        response = c.get("/personal/blog/category/post-1/update/")
        self.assertEqual(response.status_code, 302)


    def test_post_update_page_without_post(self):
        """ If no post, then a 404 error. """

        user = create_user()
        c = Client()
        # Log the user in
        c.login(username=USER, password=PASSWORD)
        response = c.get("/personal/blog/category/post-1/update/")
        self.assertEqual(response.status_code, 404)
            
            
    def test_post_update_page_with_post(self):
        """ Make Sure Post Can Be Updated. """

        setUp(self)
        post = Post.objects.get(slug='post-1')
        c = Client()
        # Log the user in
        c.login(username=USER, password=PASSWORD)
        response = c.get("/personal/blog/category/post-1/update/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('form.html', response.template_name)
    

    def test_post_update_page_url_resolves_post_update_view(self):
        view = resolve('/personal/blog/category/post-1/update/')
        self.assertEquals(view.func.view_class, PostUpdateView)


class PostCreatePageTest(TestCase):
    """ Test module for Post Create Page. """

    def test_post_create_page_without_user(self):
        """ If no user, then redirect. """

        c = Client()
        response = c.get("/personal/blog-post/")
        self.assertEqual(response.status_code, 302)
    
    
    def test_post_create_page(self):
        """ Make Sure Post Create Page Shows. """

        setUp(self)
        c = Client()
        # Log the user in
        c.login(username=USER, password=PASSWORD)
        response = c.get("/personal/blog-post/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('form.html', response.template_name)    
                

    def test_post_create_page_url_resolves_post_create_view(self):
        view = resolve('/personal/blog-post/')
        self.assertEquals(view.func.view_class, PostCreateView)


class PostDeletePageTest(TestCase):
    """ Test module for Post Delete Page. """
    
    def test_post_delete_page_without_user(self):
        """ If no user, then redirect. """

        c = Client()
        response = c.get("/personal/blog/category/post-1/delete/")
        self.assertEqual(response.status_code, 302)

    
    def test_post_delete_page_without_post(self):
        """ If no post, then a 404 error. """

        user = create_user()
        c = Client()
        # Log the user in
        c.login(username=USER, password=PASSWORD)
        response = c.get("/personal/blog/category/post-1/delete/")
        self.assertEqual(response.status_code, 404)
            
            
    def test_post_delete_page_with_post(self):
        """ Make Sure Post Can Be Deleted. """

        setUp(self)
        post = Post.objects.get(slug='post-1')
        c = Client()
         # Log the user in
        c.login(username=USER, password=PASSWORD)
        response = c.get("/personal/blog/category/post-1/delete/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('blog/post_delete.html', response.template_name)
        self.assertTemplateUsed(response, 'blog/post_delete.html')
    

    def test_post_delete_page_url_resolves_post_delete_view(self):
        view = resolve('/personal/blog/category/post-1/delete/')
        self.assertEquals(view.func.view_class, PostDelete)
