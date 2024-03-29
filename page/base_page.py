import time
import unittest
from urllib.parse import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.settings import DEFAULT_LOCATOR_TYPE, EXPLICITLY_WAIT


class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self, url):
        # self.driver.get(url)
        return self.driver.title


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

    def wait_for_element_to_be_clicable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))

    def wait_for_element_to_be_clickable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        time.sleep(3)


    # def read_page_url(self):
    #     return self.driver.current_url

    # def parse_current_url(self):
    #     url = self.read_page_url()
    #     return urlparse(url)
    #
    # def read_page_netloc_from_current_url(self):
    #     parsed_url = self.parse_current_url()
    #     return parsed_url.netloc
    #
    # def waits(self, seconds):
    #     return time.sleep(seconds)
    #
    # def wait_for_url_to_appear(self):
    #     url = ""
    #     while url == "":
    #         url = self.read_page_netloc_from_current_url()
    #         self.waits(3)

