#Search and next page for Share Sansar
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self,driver):
        self.driver=driver
        self.search_field = By.XPATH, "//input[@id='company_search']"
        self.news = By.XPATH, "//a[@id='btn_cnews']"

    def open_page(self,url):
        self.driver.get(url)

    def do_search(self,search):
        self.driver.find_element(*self.search_field).send_keys(search)

    def submit_search(self):
        self.driver.find_element(*self.search_field).submit()

    def click_news(self):
        self.driver.find_element(*self.news).click()

    def website_title(self):
        return self.driver.title

    def next_page(self):
        while True:
            # Check if 'Next' button is available and click it
            try:
                next_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "Next"))  # Adjust selector based on the website
                )
                next_button.click()  # Click the "Next" button
                time.sleep(3)  # Wait for the next page to load
            except:
                print("No more pages.")
                break
