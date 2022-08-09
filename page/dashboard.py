import time

import self as self
from selenium.webdriver.support.expected_conditions import title_is
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver
from selenium import webdriver
from page.base_page import BasePage


class Dashboard(BasePage):
    futbol_kolektyw_logo_xpath = '//*[@title="Logo Scouts Panel"]'
    add_player_button_xpath = "//*[text()='Add player']"
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    wait = WebDriverWait(driver, 10)

    def title_of_page(self):
        self.wait_for_element_to_be_clicable(self.futbol_kolektyw_logo_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)
