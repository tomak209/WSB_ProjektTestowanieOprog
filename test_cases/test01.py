from page_objects.registration_page import RegistrationPage
from page_objects.login_page import LoginPage


def test_prerequisites_check_registration_page_components(browser):
    registration_page = RegistrationPage(browser)
    assert registration_page.validate_logo_is_visible() is True
    assert registration_page.validate_zalogujSie_is_visible() is True
    assert registration_page.page_opened() is True

def test_1_1_create_account_field_validation(browser):
    registration_page = RegistrationPage(browser)
    assert registration_page.empty_fields()
    assert registration_page.firstname_check()
    assert registration_page.lastname_check()
    assert registration_page.email_check()
    assert registration_page.password_check()
    assert registration_page.phone_check()
    assert registration_page.zipcode_check()

def test_1_2_create_account_customer_already_exists(browser):
    registration_page = RegistrationPage(browser)
    assert registration_page.db_data_exists()

def test_1_4_first_login(browser):
    login_page = LoginPage(browser)
    assert login_page.login() is True