from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewsPage:
    def __init__(self, driver):
        self.driver = driver
        self.news_title = By.CLASS_NAME, "ipo-news-title"
        self.latest_news_title = By.CSS_SELECTOR, "div[class='col-md-12'] h1"
        self.latest_news_content = By.ID, "newsdetail-content"
        self.latest_news_date = By.CSS_SELECTOR, "div[class='col-lg-8'] h5"

    def open_page(self, url):
        self.driver.get(url)

    # Methods to scrape latest news article details
    def click_news_title(self):
        return self.driver.find_element(*self.news_title).click()

    def get_latest_news_title(self):
        return self.driver.find_element(*self.latest_news_title).text

    def get_latest_news_content(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.latest_news_content)
        )
        return self.driver.find_element(*self.latest_news_content).text

    def get_latest_news_date(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.latest_news_date)
        )
        return self.driver.find_element(*self.latest_news_date).text
