from prestashop_app.pages.page_home import PageHome
from prestashop_app.pages.page_login import LoginPage


class PrestashopApp:
    def __init__(self, driver):
        self.driver = driver
        self.home_page = PageHome(driver)
        self.login_page = LoginPage(driver)
