import time
from config import strings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from page_objects.base_page import BasePage

class SaveBox(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(strings.save_box_url)
        self.browser.implicitly_wait(strings.timeout)