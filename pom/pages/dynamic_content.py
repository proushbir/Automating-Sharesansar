from selenium.webdriver.common.by import By

class DynamicContent:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def scrape_announcements(self):
        announcements = self.driver.find_elements(By.CLASS_NAME,"featured-news-list")

        for announcement in announcements:
            print(announcement.text)

