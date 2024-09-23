#IMPORT ALL THE NECESSARY MODULES
from selenium.webdriver.common.by import By

#DEFINE CLASS FOR LOGOUT PAGE
class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_url = By.XPATH,"//a[normalize-space()='Login']"
        self.email_field = By.XPATH,"//input[@id='email']"
        self.password_field = By.XPATH,"//input[@id='password']"
        self.login_button = By.XPATH,"//input[@value='Login']"
        self.name_url = By.XPATH,"//a[@role='button']"
        self.logout_url = By.XPATH,"//ul[@class='dropdown-menu']//a[normalize-space()='Logout']"

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

    def click_name_url(self):
        self.driver.find_element(*self.name_url).click()

    def click_logout_url(self):
        self.driver.find_element(*self.logout_url).click()