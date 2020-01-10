import time
from config import strings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from page_objects.base_page import BasePage

class SearchPage(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(strings.home_url)
        self.browser.implicitly_wait(strings.timeout)

    @property
    def input_inner(self):
        return self.browser.find_element_by_id("query_querystring")

    @property
    def icon_search(self):
        return self.browser.find_element_by_class("beheader-search")

    def correct_search(self):
        self.browser.input_inner.send_key(strings.search_data("1"))
        self.browser.execute_script("arguments[0].click();", self.icon_search)

    def incorrect_search_1(self):
        self.browser.input_inner.send_key(strings.search_data("2"))
        self.browser.execute_script("arguments[0].click();", self.icon_search)

    def incorrect_search_2(self):
        self.browser.input_inner.send_key(strings.search_data("3"))
        self.browser.execute_script("arguments[0].click();", self.icon_search)

    def incorrect_search_3(self):
        self.browser.input_inner.send_key(strings.search_data("4"))
        self.browser.execute_script("arguments[0].click();", self.icon_search)

