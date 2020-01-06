import time
from config import strings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from page_objects.base_page import BasePage

class RegistrationPage(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(strings.registration_url)
        self.browser.implicitly_wait(strings.timeout)

    def page_opened(self):
        text = self.browser.find_element_by_xpath('//*[@id="js-register"]/section/div/div/form/div/div[2]/div/p').text
        if text == 'Załóż konto':
            return True
        else:
            return False

    @property
    def radio_button_mrs(self):
        return self.browser.find_element_by_id(
            'js-salutation_misses')
    @property
    def radio_button_mr(self):
        return self.browser.find_element_by_id(
            'js-salutation_mister')

    @property
    def input_firstname(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_address_firstName")

    @property
    def input_lastname(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_address_lastName")

    @property
    def input_email(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_email")

    @property
    def input_password(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_plainPassword")

    @property
    def input_phone(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_mobileNumber_number")

    @property
    def input_zipcode(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_address_postcode")

    @property
    def checkbox_terms_and_conditions(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_consentForm_consent_686_0")

    @property
    def button_save(self):
        return self.browser.find_element_by_xpath('//*[@id="js-checkboxesRegister"]/div[1]/div[2]/div[2]/button')


    def verification_db_data_exists(self):
        self.browser.execute_script("arguments[0].click();", self.radio_button_mr)
        self.input_firstname.send_keys(strings.registration_data["first_name"])
        self.input_lastname.send_keys(strings.registration_data["last_name"])
        self.input_email.send_keys(strings.registration_data["email"])
        self.input_password.send_keys(strings.registration_data["password"])
        self.input_phone.send_keys(strings.registration_data["phone"])
        self.input_zipcode.send_keys(strings.registration_data["zipcode"])
        self.browser.execute_script("arguments[0].click();", self.checkbox_terms_and_conditions)
        self.browser.execute_script("arguments[0].click();", self.button_save)
        self.browser.implicitly_wait(strings.timeout)
        text_phone = self.browser.find_element_by_xpath('/html/body/div[3]/main/div[3]/div')
        text_email = self.browser.find_element_by_xpath('/html/body/div[3]/main/div[4]/div')
        time.sleep(60)
        if text_phone.text == 'Podany numer telefonu istnieje już w bazie':
            return True
        if text_email.text == 'Email '+strings.registration_data["email"]+' jest zajęty':
            return True
        else:
            return False

