from page_objects.login_page import LoginPage
from page_objects.save_box_page import SaveBox

def test_logger(logger):
    logger.info("Logowanie z poziomu testów")

def test_9_1_add_products_to_save_box(browser):
    save_box = LoginPage(browser)
    assert save_box.add_cubby is True

def test_9_2_sub_products_from_save_box(browser):
    save_box = LoginPage(browser)
    assert save_box.sub_cubby is True
