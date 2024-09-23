#IMPORT ALL THE NECESSARY MODULES
from selenium.webdriver.common.by import By

#DEFINE CLASS FOR LOGIN PAGE
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_url = By.XPATH,"//a[normalize-space()='Login']"
        self.email_field = By.XPATH,"//input[@id='email']"
        self.password_field = By.XPATH,"//input[@id='password']"
        self.login_button = By.XPATH,"//input[@value='Login']"
    def open_page(self,url):
        self.driver.get(url)

    def open_login_url(self):
        self.driver.find_element(*self.login_url).click()

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_password(self, pwd):
        self.driver.find_element(*self.password_field).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()