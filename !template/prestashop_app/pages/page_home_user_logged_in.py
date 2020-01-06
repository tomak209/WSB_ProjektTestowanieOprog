import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from prestashop_app.pages.page_base import PageBase


class PageHomeUserLoggedIn(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self._logger = logging.getLogger(__name__)

    def is_open(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="_desktop_user_info"]/div/a[1]/i')))
            return True
        except Exception as e:
            self._logger.exception(e)
            return False

    def sign_out(self):
        self.button_sign_out.click()
        from prestashop_app.pages.page_home import PageHome
        home_page = PageHome(self.driver)
        return home_page if home_page.is_open() else None