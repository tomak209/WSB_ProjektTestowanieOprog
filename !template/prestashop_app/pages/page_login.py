import logging
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from prestashop_app.pages.page_create_account import PageCreateAccount
from prestashop_app.pages.page_base import PageBase
from prestashop_app.pages.page_home_user_logged_in import PageHomeUserLoggedIn


class LoginPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self._logger = logging.getLogger(__name__)

    @property
    def header_logo(self):
        """
        :rtype: WebElement
        """
        return self.driver.find_element_by_css_selector('.m-logo') #.logo

    @property
    def label_subpage_title(self):
        return self.driver.find_element_by_css_selector('.page-header > h1:nth-child(1)')

    @property
    def input_email(self):
        return self.driver.find_element_by_xpath("//input[@name='email']")

    @property
    def input_password(self):
        return self.driver.find_element_by_xpath("//input[@name='password']")

    @property
    def button_submit(self):
        return self.driver.find_element_by_xpath('//*[@id="submit-login"]')

    @property
    def url_create_account(self):
        return self.driver.find_element_by_css_selector(".no-account > a:nth-child(1)")

    def is_open(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, '//*[@id="main"]/header/h1'), "Log in to your account"))

            return True
        except Exception as e:
            self._logger.exception(e)
            return False

    def log_in_using_credentials(self, username, password):
        self.input_email.send_keys(username)
        self.input_password.send_keys(password)
        self.button_submit.click()
        home_page_user_logged_in = PageHomeUserLoggedIn(self.driver)
        return home_page_user_logged_in if home_page_user_logged_in.is_open() else None

    def go_to_page_create_account(self):
        self.url_create_account.click()
        page_create_account = PageCreateAccount(self.driver)
        return page_create_account if page_create_account.is_open() else None
