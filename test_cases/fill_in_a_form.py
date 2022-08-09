import os
import time
import unittest

from selenium.webdriver.chrome.service import Service

from selenium import webdriver

from page.add_a_player_form import AddPlayerForm
from page.dashboard import Dashboard
from page.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestFillInaForm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        # self.driver_service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_fill_in_a_form(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.wait_for_button_will_be_clicable()
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_the_add_player_button()
        form_page = AddPlayerForm(self.driver)
        form_page.set_age_field("12.10.1999")
        form_page.select_leg()
        time.sleep(3)


    @classmethod
    def tearDown(self):
        self.driver.quit() #close the browser after the test

