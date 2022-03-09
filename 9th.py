from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = '/Users/jinseunghee/Documents/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("https://davelee-fun.github.io/blog/TEST/index.html")

#클래스가 두개인 경우 css selector 에서는 .클래스1.클래스2
#xpath의 경우에는 //*[contains(@class,'클래스1')and contains(@class,'클래스2')]

id_text = driver.find_element_by_xpath("//input[@id='username']")
id_text.clear()
id_text.send_keys("error@error.com")
time.sleep(3)

password = driver.find_element_by_xpath("//input[@id='password']")
password.clear()
password.send_keys("1234")
time.sleep(3)

login = driver.find_element_by_xpath("//input[@type='submit']")
login.click()
time.sleep(3)

driver.quit()