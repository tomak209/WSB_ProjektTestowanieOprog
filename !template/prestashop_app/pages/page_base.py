import logging
from selenium.webdriver.remote.webdriver import WebDriver


class PageBase(object):

    def __init__(self, driver):
        self._driver = driver
        self._logger = logging.getLogger(__name__)

    @property
    def driver(self):
        """
        :rtype: WebDriver
        """
        return self._driver

    def get_title(self):
        return self._driver.title

    @property
    def header_logo(self):
        """
        :rtype: WebElement
        """
        return self.driver.find_element_by_css_selector('.m-logo') #.logo

    @property
    def button_sign_in(self):
        return self.driver.find_element_by_xpath('//*[@id="js-accountInfo"]/span/a')  # //*[@id="_desktop_user_info"]/div/a/span

    @property
    def button_sign_out(self):
        return self.driver.find_element_by_xpath('//*[@id="js-accountInfo"]/span[3]/a')  # //*[@id="_desktop_user_info"]/div/a[1]/i
