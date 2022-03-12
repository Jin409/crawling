from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chromedriver = '/Users/jinseunghee/Documents/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("https://www.naver.com/")
elem = driver.find_element_by_tag_name("search")
elem.clear()
elem.send_keys("hello")
elem.send_keys(Keys.RETURN)
driver.quit()