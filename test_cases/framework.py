import os
import unittest

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from page.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class Test(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        # self.driver_service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")

    def test_wait_for_element(self):
        wait_for_element = LoginPage(self.driver)
        wait_for_element.type_in_email('user07@getnada.com')
        wait_for_element.type_in_password('Test-1234')
        wait_for_element.wait_for_button_will_be_clicable()

class TestMediumPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        # self.driver_service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://medium.com/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_check_title(self):
        actual_title = self.get_page_title("https://medium.com/")
        expected_title = "Medium – Where good ideas find you."
        assert actual_title == expected_title

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    @classmethod
    def tearDown(self):
        self.driver.quit()



class TestMediumPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        # self.driver_service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://medium.com/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_check_title(self):
        actual_title = self.get_page_title('https://medium.com/')
        expected_title = 'Medium – Where good ideas find you.'
        # self.assert_title('https://medium.com/', expected_title)
        assert actual_title == expected_title

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_title(self, url, expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(expected_title, actual_title,
                         f'Expected {expected_title} differ from actual title {actual_title} on page: {url}')

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element

            :param driver: webdriver instance
            :param xpath: xpath to element with text to be observed
            :param expected_text: text what we expecting to be found
            :return: None
        """
        element = driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        assert expected_text == element_text


    print("dupa jasia")

    # def test_check_if_the_title_is_correct(self):
    #     check_title = LoginPage(self.driver)
    #     check_title.title_of_page()

    def test_chcek_name_is_name(self):
        check_words = LoginPage(self.driver)
        check_words.check_title_of_header()



