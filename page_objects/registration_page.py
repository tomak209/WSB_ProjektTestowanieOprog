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
    def radio_button_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[5]/div/label[2]/em')

    @property
    def input_firstname(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_address_firstName")

    @property
    def input_firstname_info_empty(self):
        return self.browser.find_element_by_xpath(
            '// *[@id="js-register"]/section/div/div/form/div/div[2]/div/div[6]/div[2]/em')

    @property
    def input_firstname_info_1_letter(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[6]/div[2]/em')

    @property
    def input_firstname_info_numbers(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[6]/div[2]/em')

    @property
    def input_lastname(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_address_lastName")

    @property
    def input_lastname_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[7]/div[2]/em')

    @property
    def input_email(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_email")

    @property
    def input_email_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[10]/div[2]/em')

    @property
    def input_password(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_plainPassword")

    @property
    def input_password_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[11]/div[2]/em')

    @property
    def input_phone(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_mobileNumber_number")

    @property
    def input_phone_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[12]/div[2]/em')

    @property
    def input_zipcode(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_address_postcode")

    @property
    def input_zipcode_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-register"]/section/div/div/form/div/div[2]/div/div[16]/div[2]/em')

    @property
    def checkbox_terms_and_conditions(self):
        return self.browser.find_element_by_id(
            "enp_customer_registration_form_type_consentForm_consent_686_0")

    @property
    def checkbox_terms_and_conditions_info_empty(self):
        return self.browser.find_element_by_xpath(
            '//*[@id="js-checkboxes"]/label[1]/label/em')

    @property
    def button_save(self):
        return self.browser.find_element_by_xpath('//*[@id="js-checkboxesRegister"]/div[1]/div[2]/div[2]/button')

    def empty_fields(self):
        try:
            print()
            print('Test 1.1.1')

            self.browser.execute_script("arguments[0].click();", self.button_save)
            self.browser.implicitly_wait(strings.timeout)

            fields = {self.radio_button_info_empty.text: 'Wybierz zwrot',
                      self.input_firstname_info_empty.text: 'Podaj imię',
                      self.input_lastname_info_empty.text: 'Podaj nazwisko',
                      self.input_email_info_empty.text: 'Podaj adres email',
                      self.input_password_info_empty.text: 'Podaj hasło',
                      self.input_phone_info_empty.text: 'Podaj numer telefonu',
                      self.input_zipcode_info_empty.text: 'Podaj kod pocztowy',
                      self.checkbox_terms_and_conditions_info_empty.text: 'To pole jest wymagane'
                      }

            for field in fields:
                print(field, '=', fields[field], '?', end=" ")
                if field == fields[field]:
                    print('True')
                else:
                    print('False')
                    return False
            return True
        except Exception as error:
            print(error)

    def invalid_data(self):
        try:
            print()
            print('Test 1.1.2')

            self.browser.execute_script("arguments[0].click();", self.radio_button_mr)
            self.input_firstname.send_keys(strings.registration_data["first_name"])
            self.input_lastname.send_keys(strings.registration_data["last_name"])
            self.input_email.send_keys(strings.registration_data["email"])
            self.input_password.send_keys(strings.registration_data["password"])
            self.input_phone.send_keys(strings.registration_data["phone"])
            self.input_zipcode.send_keys(strings.registration_data["zipcode"])
            self.browser.implicitly_wait(strings.timeout)

            fields = {self.input_firstname_info_1_letter.text: 'Wartość wprowadzona w polu Imię nie może mieć mniej znaków niż 2',
                      self.input_firstname_info_numbers.text: 'Pole "Imię" zawiera niedozwolone znaki'
                      }

            for field in fields:
                print(field, '=', fields[field], '?', end=" ")
                if field == fields[field]:
                    print('True')
                else:
                    print('False')
                    return False
            return True
        except Exception as error:
            print(error)

    def db_data_exists(self):
        try:
            print()
            print('Test 1.2.1')

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

            text_phone = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/div[3]/div')
            text_email = self.browser.find_element_by_xpath('//*[@id="js-mainWrapper"]/main/div[4]/div')

            fields = {text_phone.text: ' Podany numer telefonu istnieje już w bazie',
                      text_email.text: ' Email projektautomatyzacjitestowgr1@gmail.com jest zajęty'
                      }

            for field in fields:
                print(field, '=', fields[field], '?', end=" ")
                if field == fields[field]:
                    print('True')
                else:
                    print('False')
                    return False
            return True
        except Exception as error:
            print(error)

