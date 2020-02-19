from django.contrib.staticfiles.testing import StaticLiveServerTestCase
#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver


USER = 'user@example.com'
USER2 = 'oteruser@example.com'
PASSWORD = 'pAs$w0rd!!'
EMAIL = 'user@example.com'
NAME = 'main'
SUMMARY = 'main category'
TITLE = 'first post'
CONTENT = 'my first post'


### Set up Data base with fixtures
def create_user(username=USER, password=PASSWORD, email=EMAIL): 
    return get_user_model().objects.create_user(
        username=username, password=password, email=email)
        

class BlogSeleniumTests(StaticLiveServerTestCase):
    #fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        #cls.selenium = WebDriver()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    
    
    def test_category(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/register/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(USER)
        password1_input = self.selenium.find_element_by_name("password1")
        password1_input.send_keys(PASSWORD)
        password2_input = self.selenium.find_element_by_name("password2")
        password2_input.send_keys(PASSWORD)
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys(EMAIL)
        self.selenium.find_element_by_id("signup").click()
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(USER)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(PASSWORD)
        self.selenium.find_element_by_id("login").click()
        self.selenium.implicitly_wait(10)
        self.selenium.find_element_by_id("categories").click()
    


    def test_category_create(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/register/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(USER)
        password1_input = self.selenium.find_element_by_name("password1")
        password1_input.send_keys(PASSWORD)
        password2_input = self.selenium.find_element_by_name("password2")
        password2_input.send_keys(PASSWORD)
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys(EMAIL)
        self.selenium.find_element_by_id("signup").click()
        self.selenium.get('%s%s' % (self.live_server_url, '/personal/blog/create-category/'))
        name_input = self.selenium.find_element_by_name("name")
        name_input.send_keys(NAME)
        summary_input = self.selenium.find_element_by_name("summary")
        summary_input.send_keys(SUMMARY)
        self.selenium.find_element_by_class_name("btn").click()
        


    
    def test_post(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/register/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(USER)
        password1_input = self.selenium.find_element_by_name("password1")
        password1_input.send_keys(PASSWORD)
        password2_input = self.selenium.find_element_by_name("password2")
        password2_input.send_keys(PASSWORD)
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys(EMAIL)
        self.selenium.find_element_by_id("signup").click()
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(USER)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(PASSWORD)
        self.selenium.find_element_by_id("login").click()
        self.selenium.implicitly_wait(10)
        #self.selenium.get('%s%s' % (self.live_server_url, '/personal/blog/'))
        #self.selenium.find_element_by_id("blog").click()



    def test_post_create(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/register/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(USER)
        password1_input = self.selenium.find_element_by_name("password1")
        password1_input.send_keys(PASSWORD)
        password2_input = self.selenium.find_element_by_name("password2")
        password2_input.send_keys(PASSWORD)
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys(EMAIL)
        self.selenium.find_element_by_id("signup").click()
        self.selenium.get('%s%s' % (self.live_server_url, '/personal/blog/create-category/'))
        name_input = self.selenium.find_element_by_name("name")
        name_input.send_keys(NAME)
        summary_input = self.selenium.find_element_by_name("summary")
        summary_input.send_keys(SUMMARY)
        self.selenium.find_element_by_class_name("btn").click()
        self.selenium.get('%s%s' % (self.live_server_url, '/personal/blog-post/'))
        title_input = self.selenium.find_element_by_name("title")
        title_input.send_keys(TITLE)
        content_input = self.selenium.find_element_by_name("content")
        content_input.send_keys(CONTENT)
        self.selenium.find_element_by_class_name("btn").click()