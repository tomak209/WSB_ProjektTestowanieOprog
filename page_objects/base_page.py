from config import strings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class BasePage:

    def __init__(self, browser):
        self.browser = browser

    @property
    def logo(self):
        return self.browser.find_element_by_class_name("m-logo")

    @property
    def zalogujSie(self):
        return self.browser.find_element_by_class_name("js-header_login")


    def validate_logo_is_visible(self):
        logo = self.browser.find_element_by_class_name("m-logo")
        if logo.is_displayed():
            return True
        else:
            return False

    def validate_zalogujSie_is_visible(self):
        zalogujSie = self.browser.find_element_by_class_name( "js-header_login")
        if zalogujSie.is_displayed():
            return True
        else:
            return False
