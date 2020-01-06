import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from prestashop_app.pages.page_base import PageBase
from prestashop_app.pages.page_login import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageHome(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.title = "Media Markt - Sklep internetowy mediamarkt.pl" #"PrestaShop Live Demo"
        self._logger = logging.getLogger(__name__)
        self._logger.info("Created Home Page Object")

    def is_open(self):
        try:
            element = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="js-accountInfo"]/span/a')))  # //*[@id="_desktop_user_info"]/div/a/span
            return True
        except Exception as e:
            self._logger.exception(e)
            return False

    def go_to_page_login(self):
        self.button_sign_in.click()
        login_page = LoginPage(self.driver)
        return login_page if login_page.is_open() else None

    def go_to_page_create_account(self):
        login_page = self.go_to_page_login()
        if login_page is not None:
            return login_page.go_to_page_create_account()
        else:
            return None
