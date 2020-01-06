from page_objects.registration_page import RegistrationPage


def test_prerequisites_check_registration_page_components(browser):
    registration_page = RegistrationPage(browser)
    assert registration_page.validate_logo_is_visible() is True
    assert registration_page.validate_zalogujSie_is_visible() is True
    assert registration_page.page_opened() is True

def test_1_1_create_account_field_validation(browser):
    registration_page = RegistrationPage(browser)
    pass

def test_1_2_create_account_customer_already_exists(browser):
    registration_page = RegistrationPage(browser)
    assert registration_page.verification_db_data_exists() is True
