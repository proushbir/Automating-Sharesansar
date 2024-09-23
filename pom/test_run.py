from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from pom.pages.search_next_page import SearchPage
from pom.pages.scrape_data import NewsPage
from pom.pages.login_page import LoginPage
from pom.pages.logout_page import LogoutPage
from pom.pages.register_page import RegistrationPage
from pom.pages.dynamic_content import DynamicContent

@pytest.fixture()
def driver():
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(1)
    #yield the driver
    yield driver
    #close the driver
    driver.quit()

def test_search_next_page(driver):
    search_page=SearchPage(driver)
    search_page.open_page("https://www.sharesansar.com/")
    driver.maximize_window()
    time.sleep(1)
    search_page.do_search("NIBLACE")
    time.sleep(1)
    search_page.submit_search()
    time.sleep(1)
    search_page.click_news()
    time.sleep(1)
    search_page.next_page()
    time.sleep(1)

def test_scrape_latest_news(driver):
    news_page=NewsPage(driver)
    news_page.open_page("https://www.sharesansar.com/")
    driver.maximize_window()
    time.sleep(2)
    news_page.click_news_title()
    title = news_page.get_latest_news_title()
    content = news_page.get_latest_news_content()
    date = news_page.get_latest_news_date()

    # Optionally print the scraped data
    print(f"Title: {title}")
    print(f"Content: {content}")
    print(f"Date: {date}")

#Testing the different login credentials using Parameterization
@pytest.mark.parametrize("useremail,userpassword",[
    ("ramshrestha16@gmail.com","Nepali@123"),
    ("johnny02@gmail.com","Nepali@123"),
    ("haribahadur@gmail.com","Newone31"),
    ("","")
])
def test_login_sharesansar(driver, useremail,userpassword):
    sharesansar_login = LoginPage(driver)
    sharesansar_login.open_page("https://www.sharesansar.com/")
    driver.maximize_window()
    sharesansar_login.open_login_url()
    time.sleep(1)
    sharesansar_login.enter_email(useremail)
    time.sleep(1)
    sharesansar_login.enter_password(userpassword)
    time.sleep(1)
    sharesansar_login.click_login()
    time.sleep(3)

    # check if the username and password is correct
    page_source = driver.page_source
    if "Account Details" in page_source:
        print(f"Valid Username or Password for user: {useremail}")
    else:
        print(f"Invalid Username or Password for user: {useremail}")

def test_logout_sharesansar(driver):
    sharesansar_logout = LogoutPage(driver)
    sharesansar_logout.open_page("https://www.sharesansar.com/")
    driver.maximize_window()
    sharesansar_logout.open_login_url()
    time.sleep(1)
    sharesansar_logout.enter_email("ramshrestha16@gmail.com")
    time.sleep(1)
    sharesansar_logout.enter_password("Nepali@123")
    time.sleep(1)
    sharesansar_logout.click_login()
    time.sleep(1)
    sharesansar_logout.click_name_url()
    time.sleep(1)
    sharesansar_logout.click_logout_url()
    time.sleep(2)

def test_registration(driver):
    email = "ramshrestha16@gmail.com"
    phone = "9810123456"
    sharesansar_registration = RegistrationPage(driver)
    sharesansar_registration.open_page("https://www.sharesansar.com/")
    driver.maximize_window()
    sharesansar_registration.open_register_page()
    time.sleep(1)
    sharesansar_registration.enter_name("Ram Shrestha")
    time.sleep(1)
    sharesansar_registration.enter_email(email)
    time.sleep(1)
    sharesansar_registration.enter_mobile_number(phone)
    time.sleep(1)
    sharesansar_registration.enter_password("Nepali@123")
    time.sleep(1)
    sharesansar_registration.enter_confirm_password("Nepali@123")
    time.sleep(1)

    # check the validity of the email
    if sharesansar_registration.is_valid_email(email):
        print(f"The given email: {email} is valid")
    else:
        print(f"The given email: {email} is invalid")

    # check the validity of the mobile number
    if sharesansar_registration.is_valid_phone(phone):
        print(f"The given mobile number: {phone} is valid")
    else:
        print(f"The given mobile number: {phone} is invalid")

def test_dynamic_content(driver):
    scrape_content = DynamicContent(driver)
    scrape_content.open_page("https://www.sharesansar.com/announcement")
    driver.maximize_window()
    time.sleep(1)
    scrape_content.scrape_announcements()
    time.sleep(1)