from django.test import TestCase, Client
from ..models import Category, Post, Comment
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from ..views import CategoryListView, CategoryDetailListView

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
        #self.assertEqual(response.status_code, 404)
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
        #print(response.context)
    

    
    def test_category_list_url_resolves_category_list_view(self):
        view = resolve('/personal/blog/category/')
        self.assertEquals(view.func.view_class, CategoryListView)

        
class CategoryPageTest(TestCase):
    """ Test module for Category Page. """

    def test_category_detail_page_without_category(self):
        """ If no category, then a 404 error. """

        c = Client()
        response = c.get("/personal/blog/category-main/")
        self.assertEqual(response.status_code, 404)
        #self.assertEqual(response.status_code, 200)
            
            
    def test_category_detail_page_with_category(self):
        """ Make Sure category shows on the page. """

        setUp(self)
        category = Category.objects.get(slug='main')
        c = Client()
        response = c.get("/personal/blog/category-main/")
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.context["title"], "category # 1")
        self.assertEqual(response.context['category'], category)
        #self.assertContains(response, category.name)
        #self.assertContains(response.template_name, ['blog/category_detail.html'])
        self.assertIn('blog/category_detail.html', response.template_name)
    

    def test_category_page_url_resolves_category_detail_view(self):
        view = resolve('/personal/blog/category-main/')
        self.assertEquals(view.func.view_class, CategoryDetailListView)