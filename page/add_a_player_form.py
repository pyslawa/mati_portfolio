from page.base_page import BasePage


class AddPlayerForm(BasePage):
    age_field_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input'
    leg_dropdown_xpath = '//*[@id="mui-component-select-leg"]'
    left_leg_xpath = '//*[@id="menu-leg"]/div[3]/ul/li[2]' #"//ul/li[2]"
    district_dropdown_xpath = '//*[@id="mui-component-select-district"]'
    district_name = "//*[text() = 'Lublin']"

    def set_age_field(self, date):
        self.field_send_keys(self.age_field_xpath, date)

    def select_leg(self):
        self.click_on_the_element(self.leg_dropdown_xpath)
        self.click_on_the_element(self.left_leg_xpath)

    def select_district(self):
        self.wait_for_element_to_be_visibility(self.age_field_xpath)
        self.click_on_the_element(self.district_dropdown_xpath)
        self.click_on_the_element(self.district_name)