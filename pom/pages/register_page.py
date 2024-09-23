#IMPORT ALL THE NECESSARY MODULES
from selenium.webdriver.common.by import By
import re

#DEFINE CLASS FOR REGISTRATION PAGE
class RegistrationPage:
    def __init__(self,driver):
        self.driver = driver
        self.register_page = By.XPATH,"//a[normalize-space()='Register']"
        self.name_field = By.XPATH,"//input[@id='name']"
        self.email_field= By.XPATH,"//input[@id='email']"
        self.mobile_number = By.XPATH,"// input[ @ id = 'mobileno']"
        self.password_field = By.XPATH,"//input[@id='password']"
        self.confirm_password_field = By.XPATH,"//input[@id='password-confirm']"

    def open_page(self,url):
        self.driver.get(url)

    def open_register_page(self):
        self.driver.find_element(*self.register_page).click()

    def enter_name(self,name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def enter_email(self,email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_mobile_number(self,mobilenumber):
        self.driver.find_element(*self.mobile_number).send_keys(mobilenumber)

    def enter_password(self,password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*self.confirm_password_field).send_keys(confirm_password)

    def is_valid_email(self, email):
        # check the format using Regular Expression(re)
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None

    def is_valid_phone(self, mobilenumber):
        return bool(re.match(r'^\d{10}$', mobilenumber))