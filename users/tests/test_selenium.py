from django.contrib.staticfiles.testing import StaticLiveServerTestCase
#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver


USER = 'user@example.com'
USER2 = 'oteruser@example.com'
PASSWORD = 'pAs$w0rd!!'
EMAIL = 'user@example.com'


def create_user(username=USER, password=PASSWORD, email=EMAIL): 
    return get_user_model().objects.create_user(
        username=username, password=password, email=email)
        

class MySeleniumTests(StaticLiveServerTestCase):
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

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(USER)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(PASSWORD)
        #self.selenium.find_element_by_xpath('//input[@value="login"]').click()
        self.selenium.find_element_by_id("login").click()