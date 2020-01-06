import pytest

def test_logger(logger):
    logger.info("Logowanie z poziomu testów")


def test_home_page(prestashop_app):
    assert prestashop_app.title in prestashop_app.get_title()


def test_user_login(prestashop_app_user_logged_in):
    assert prestashop_app_user_logged_in is not None


def test_user_logout(prestashop_app_user_logged_in):
    assert prestashop_app_user_logged_in.sign_out() is not None
