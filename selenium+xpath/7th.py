#로그인하고 나서 로그아웃하기

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chromedriver = '/Users/jinseunghee/Documents/chromedriver'
driver = webdriver.Chrome(chromedriver)

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

time.sleep(5)

message = driver.find_element_by_css_selector("div.message")
print(message.text)

message = driver.find_element_by_css_selector(".news")

print(message.text)

logout = driver.find_element_by_css_selector("input[type='submit']")
logout.click()

time.sleep(5)

message = driver.find_element_by_css_selector("div.message")
print(message.text)

message = driver.find_element_by_css_selector(".news")

print(message.text)
driver.quit()