from django.test import TestCase, Client
from ..models import Category, Post, Comment
from django.contrib.auth import get_user_model
from django.urls import reverse

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

    def test_categorys_page_without_categorys(self):
        """ If no categorys exist, an appropriate message is displayed. """
        
        c = Client()
        response = c.get("/category/")
        #self.assertEqual(response.status_code, 404)
        self.assertEqual(response.status_code, 200)
        


    def test_categorys_page_with_categorys(self):
        """ Make Sure categorys show on the page. """

        setUp(self)
        c = Client()
        response = c.get("/category/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], "* categorys *")
        

        
class CategoryPageTest(TestCase):
    """ Test module for Category Page. """

    def test_category_page_without_category(self):
        """ If no category, then a 404 error. """

        c = Client()
        response = c.get("/category-main/")
        self.assertEqual(response.status_code, 404)
        #self.assertEqual(response.status_code, 200)
            
            
    def test_category_page_with_category(self):
        """ Make Sure category shows on the page. """

        setUp(self)
        category = Category.objects.get(slug='main')
        c = Client()
        response = c.get("/category-main/")
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.context["title"], "category # 1")
        self.assertEqual(response.context['category'], category)
        self.assertContains(response, category.title)
    