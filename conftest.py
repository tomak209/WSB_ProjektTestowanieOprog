import logging
import pytest
from selenium import webdriver
from config import strings

@pytest.fixture(scope="session")
def browser():
    if strings.driver_name == 'chrome':
        driver = webdriver.Chrome()
    elif strings.driver_name == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception(
            'Driver "{}" is not supported'.format(strings.driver_name))
    driver.set_window_size(strings.window_width, strings.window_height)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def logger(caplog):
    caplog.set_level(logging.INFO)
    return LOGGER


LOGGER = logging.getLogger(__name__)
