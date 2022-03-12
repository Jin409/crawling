# 동적 크롤링
# 정적으로 가져온 데이터가 아닌 경우

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chromedriver = '/Users/jinseunghee/Documents/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chromedriver,options=options)

driver.get("https://davelee-fun.github.io/blog/TEST/index.html")

time.sleep(2)

elem1 = driver.find_element_by_id("username")
elem1.clear()
elem1.send_keys("error@error.com")

time.sleep(1)

elem2 = driver.find_element_by_id("password")
elem2.clear()
elem2.send_keys("1234")

time.sleep(1)

elem3 = driver.find_element_by_css_selector("input[type='submit']")
elem3.click()

time.sleep(10)

message = driver.find_element_by_css_selector("div.message")
print(message.text)

driver.quit()