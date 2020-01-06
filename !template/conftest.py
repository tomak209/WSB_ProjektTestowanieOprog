import sys
# print(sys.path)
# del sys.path[3]
# del sys.path[3]
# print(sys.path)

import logging
import pytest
from time import sleep
from selenium import webdriver
from config.config_local import config
from prestashop_app.pages.page_home import PageHome
from prestashop_app.prestashop_app import PrestashopApp
from prestashop_app.prestashop_app_config import PrestashopAppConfig



LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def config_local():
    return config


@pytest.fixture(scope="session")
def users_data_list(config_local):
    return config_local.users_data


@pytest.fixture(scope="session")
def users_data_first_record(config_local):
    return config_local.users_data[0]


@pytest.fixture(scope="function")
def logger(caplog):
    caplog.set_level(logging.INFO)
    return LOGGER


@pytest.fixture(scope="session")
def selenium_webdriver(config_local, request):
    """
    :type config_local: PrestashopAppConfig
    """
    if config_local.driver_name == 'chrome':
        driver = webdriver.Chrome(executable_path="webdriver\chromedriver.exe")
    elif config_local.driver_name == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception(
            'Driver "{}" is not supported'.format(config_local.driver_name))

    driver.set_window_size(config_local.window_width, config_local.window_height)
    driver.implicitly_wait(config_local.implicitly_wait_time)

    def webdriver_teardown():
        driver.close()
        driver.quit()

    request.addfinalizer(webdriver_teardown)
    return driver


@pytest.fixture(scope="session")
def prestashop_app(selenium_webdriver, config_local):
    """
    :type selenium_webdriver: WebDriver
    :rtype: PageHome
    """
    prestashop = PrestashopApp(selenium_webdriver)
    prestashop.driver.get(config_local.host)
    sleep(60)
    prestashop.driver.switch_to.frame(0)
    return prestashop.home_page


@pytest.fixture(scope="session")
def prestashop_app_with_user_accounts(prestashop_app, users_data_list):
    for user in users_data_list:
        create_account_page = prestashop_app.go_to_page_create_account()
        page_user_logged_in = create_account_page.create_account(user)
        page_user_logged_in.sign_out() if page_user_logged_in is not None else None
    return prestashop_app


@pytest.fixture(scope="session")
def prestashop_app_user_logged_in(prestashop_app_with_user_accounts, users_data_first_record):
    login_page = prestashop_app_with_user_accounts.go_to_page_login()
    home_page_logged_in = login_page.log_in_using_credentials(users_data_first_record["email"],
                                                              users_data_first_record["password"])
    return home_page_logged_in
