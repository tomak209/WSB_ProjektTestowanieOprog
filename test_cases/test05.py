from page_objects.login_page import LoginPage
from page_objects.address_list_page import AddressListPage

def test_logger(logger):
    logger.info("Logowanie z poziomu testów")

def test_prerequisites_check_address_list_page_components(browser):
    address_list_page = AddressListPage(browser)
    assert address_list_page.validate_logo_is_visible() is not None
    assert address_list_page.validate_zalogujSie_is_visible() is not None
    assert address_list_page.page_opened() is not None

def test_5_1_new_address_field_validation(browser):
    address_list_page = AddressListPage(browser)
    assert address_list_page.empty_fields()
    assert address_list_page.street_check()
    assert address_list_page.street_number_check()
    assert address_list_page.email_check()
    assert address_list_page.phone_check()
    assert address_list_page.zipcode_check()
    assert address_list_page.save_data()