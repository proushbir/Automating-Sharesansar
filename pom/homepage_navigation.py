from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set the chromedriver manager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#get the website url:
website_url="https://www.sharesansar.com/"

#open the website url
driver.get(website_url)

#maximize the window
driver.maximize_window()

time.sleep(2)

achains = ActionChains(driver)

#Hover on the News Section
news_link = driver.find_element(By.XPATH, "//a[contains(text(),'News')]")
achains.move_to_element(news_link).perform()
time.sleep(2)
#Click on All News Section
driver.find_element(By.XPATH, "//a[normalize-space()='All News']").click()
time.sleep(2)

website_title = driver.title
print(f"Website title: {website_title}")

#Hover on the Training Section
news_link = driver.find_element(By.XPATH, "//a[normalize-space()='Training']")
achains.move_to_element(news_link).perform()
time.sleep(2)
#Click on Technical Analysis Section
driver.find_element(By.XPATH, "//a[@href='/technical-analysis-training']").click()
time.sleep(2)

website_title = driver.title
print(f"Website title: {website_title}")

#Hover on the Company Section
news_link = driver.find_element(By.XPATH, "//a[normalize-space()='Company']")
achains.move_to_element(news_link).perform()
time.sleep(2)
#Click on Merged Companies Section
driver.find_element(By.XPATH, "//a[normalize-space()='Merged Companies']").click()
time.sleep(2)

website_title = driver.title
print(f"Website title: {website_title}")
#close the webdriver
driver.quit()