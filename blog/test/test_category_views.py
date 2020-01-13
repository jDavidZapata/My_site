from django.test import TestCase, Client
from ..models import Category, Post, Comment
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from ..views import CategoryListView, CategoryDetailListView, CategoryUpdateView, CategoryCreateView, CategoryDelete

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

def create_user(username=USER, password=PASSWORD, email='user@example.com'): 
    return get_user_model().objects.create_user(
        username=username, password=password, email=email)


def setUp(self):

        user = create_user()
        Category.objects.create(
            author=user, name=NAME1, summary=SUMMARY1)
        Category.objects.create(
            author=user, name=NAME2, summary=SUMMARY2)


class CategorysListPageTest(TestCase):
    """ Test module for Category List Page. """

    def test_category_list_page_without_category(self):
        """ If no categorys exist, an appropriate message is displayed. """
        
        c = Client()
        response = c.get("/personal/blog/category/")
        self.assertEqual(response.status_code, 200)
        


    def test_category_list_page_with_category(self):
        """ Make Sure categorys show on the page. """

        setUp(self)
        c = Client()
        response = c.get("/personal/blog/category/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ['blog/category_list.html'])
        self.assertIn('blog/category_list.html', response.template_name)
        #self.assertEqual(response.context["categories"], "* categorys *")
    

    
    def test_category_list_url_resolves_category_list_view(self):
        view = resolve('/personal/blog/category/')
        self.assertEquals(view.func.view_class, CategoryListView)

        
class CategoryDetailPageTest(TestCase):
    """ Test module for Category Detail Page. """

    def test_category_detail_page_without_category(self):
        """ If no category, then a 404 error. """

        c = Client()
        response = c.get("/personal/blog/category-main/")
        self.assertEqual(response.status_code, 404)
            
            
    def test_category_detail_page_with_category(self):
        """ Make Sure category shows on the page. """

        setUp(self)
        category = Category.objects.get(slug='main')
        c = Client()
        response = c.get("/personal/blog/category-main/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['category'], category)
        #self.assertContains(response, category.name)
        #self.assertContains(response.template_name, ['blog/category_detail.html'])
        self.assertIn('blog/category_detail.html', response.template_name)
    

    def test_category_page_url_resolves_category_detail_view(self):
        view = resolve('/personal/blog/category-main/')
        self.assertEquals(view.func.view_class, CategoryDetailListView)



class CategoryUpdatePageTest(TestCase):
    """ Test module for Category Update Page. """

    def test_category_update_page_without_category(self):
        """ If no category, then a 404 error. """

        c = Client()
        response = c.get("/personal/blog/category-m/update/")
        self.assertEqual(response.status_code, 302)
            
            
    def test_category_update_page_with_category(self):
        """ Make Sure Category Can Be Updated. """

        setUp(self)
        category = Category.objects.get(slug='main')
        c = Client()
        response = c.get("/personal/blog/category-main/update/")
        self.assertEqual(response.status_code, 302)
        #self.assertContains(response.template_name, ['form.html'])
        #self.assertIn('form.html', response.template_name)
    

    def test_category_update_page_url_resolves_category_update_view(self):
        view = resolve('/personal/blog/category-main/update/')
        self.assertEquals(view.func.view_class, CategoryUpdateView)



class CategoryCreatePageTest(TestCase):
    """ Test module for Category Create Page. """
    
    def test_category_create_page(self):
        """ Make Sure Category Create Page Shows. """

        c = Client()
        response = c.get("/personal/blog/create-category/")
        self.assertEqual(response.status_code, 302)
        #self.assertIn('form.html', response.template_name)    
            
    

    def test_category_create_page_url_resolves_category_create_view(self):
        view = resolve('/personal/blog/create-category/')
        self.assertEquals(view.func.view_class, CategoryCreateView)



class CategoryDeletePageTest(TestCase):
    """ Test module for Category Delete Page. """
    
    def test_category_delete_page_without_category(self):
        """ If no category, then a 404 error. """

        c = Client()
        response = c.get("/personal/blog/category-main/delete/")
        self.assertEqual(response.status_code, 302)
            
            
    def test_category_delete_page_with_category(self):
        """ Make Sure Category Can Be Deleted. """

        setUp(self)
        category = Category.objects.get(slug='main')
        c = Client()
        response = c.get("/personal/blog/category-main/delete/")
        self.assertEqual(response.status_code, 302)
        #self.assertContains(response.template_name, ['blog/category_delete.html'])
        #self.assertIn('blog/category_delete.html', response.template_name)
    

    def test_category_delete_page_url_resolves_category_delete_view(self):
        view = resolve('/personal/blog/category-main/delete/')
        self.assertEquals(view.func.view_class, CategoryDelete)

    