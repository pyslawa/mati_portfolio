import os
import unittest

from selenium.webdriver.chrome.service import Service

from selenium import webdriver

from page.dashboard import Dashboard
from page.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        # self.driver_service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en') #open the website
        self.driver.fullscreen_window() #open a browser window in full size mode
        self.driver.implicitly_wait(IMPLICITLY_WAIT) #wait before you start testing

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page() #check if the title of the opened page is correct
        user_login.type_in_email('user07@getnada.com') #enter "user07@getnada.com" in the email field
        user_login.type_in_password('Test-1234') #enter "Test-1234" in the password field
        user_login.wait_for_button_will_be_clicable() #wait for the button to be clickable
        user_login.click_on_the_sign_in_button() #click on the sign in button
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page() #check if the title of the opened page is correctn

    @classmethod
    def tearDown(self):
        self.driver.quit() #close the browser after the test
