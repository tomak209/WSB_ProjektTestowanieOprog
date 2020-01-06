import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from prestashop_app.pages.page_base import PageBase


class PageCreateAccount(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self._logger = logging.getLogger(__name__)

    @property
    def radio_button_social_title_mr(self):
        return self.driver.find_element_by_css_selector('label.radio-inline:nth-child(1) > span:nth-child(1) > input:nth-child(1)')

    @property
    def radio_button_social_title_mrs(self):
        return self.driver.find_element_by_css_selector('label.radio-inline:nth-child(2) > span:nth-child(1) > input:nth-child(1)')

    @property
    def input_first_name(self):
        return self.driver.find_element_by_css_selector("div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)")

    @property
    def input_last_name(self):
        return self.driver.find_element_by_css_selector("div.form-group:nth-child(4) > div:nth-child(2) > input:nth-child(1)")

    @property
    def input_email(self):
        return self.driver.find_element_by_css_selector("div.form-group:nth-child(5) > div:nth-child(2) > input:nth-child(1)")

    @property
    def input_password(self):
        return self.driver.find_element_by_xpath("/html/body/main/section/div/div/section/section/section/form/section/div[5]/div[1]/div/input")

    @property
    def checkbox_terms_and_conditions(self):
        return self.driver.find_element_by_css_selector("div.form-group:nth-child(10) > div:nth-child(2) > span:nth-child(1) > label:nth-child(1) > input:nth-child(1)")

    @property
    def button_save(self):
        return self.driver.find_element_by_css_selector('button.btn:nth-child(2)')

    def is_open(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.page-header > h1:nth-child(1)'), "Create an account"))

            return True
        except Exception as e:
            self._logger.exception(e)
            return False

    def _fill_data(self, user_data):
        self.radio_button_social_title_mr.click() if user_data["title"] == "Mr." else self.radio_button_social_title_mrs.click()
        self.input_first_name.send_keys(user_data["first_name"])
        self.input_last_name.send_keys(user_data["last_name"])
        self.input_email.send_keys(user_data["email"])
        self.input_password.send_keys(user_data["password"])
        self.checkbox_terms_and_conditions.click()

    def create_account(self, user_data):
        self._fill_data(user_data)
        import time
        time.sleep(60)
        self.button_save.click()
        from prestashop_app.pages.page_home_user_logged_in import PageHomeUserLoggedIn
        page_user_logged_in = PageHomeUserLoggedIn(self.driver)
        return page_user_logged_in if page_user_logged_in.is_open() else None
