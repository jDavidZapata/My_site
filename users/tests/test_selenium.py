from django.contrib.staticfiles.testing import StaticLiveServerTestCase
#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver


USER = 'user@example.com'
USER2 = 'oteruser@example.com'
PASSWORD = 'pAs$w0rd!!'
EMAIL = 'user@example.com'

### Set up Data base with fixtures
def create_user(username=USER, password=PASSWORD, email=EMAIL): 
    return get_user_model().objects.create_user(
        username=username, password=password, email=email)
        

class UsersSeleniumTests(StaticLiveServerTestCase):
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

    def test_signup(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/register/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(USER)
        password1_input = self.selenium.find_element_by_name("password1")
        password1_input.send_keys(PASSWORD)
        password2_input = self.selenium.find_element_by_name("password2")
        password2_input.send_keys(PASSWORD)
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys(EMAIL)
        #self.selenium.find_element_by_xpath('//input[@value="login"]').click()
        #self.selenium.find_element_by_tag_name("button").click()
        self.selenium.find_element_by_id("signup").click()



    def test_login(self):
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
        #self.selenium.find_element_by_xpath('//input[@value="login"]').click()
        #self.selenium.find_element_by_tag_name("button").click()
        self.selenium.find_element_by_id("login").click()

    
    def test_logout(self):
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
        self.selenium.implicitly_wait(5)
        self.selenium.find_element_by_class_name('glyphicon-log-out').click()
        self.selenium.implicitly_wait(5)
    