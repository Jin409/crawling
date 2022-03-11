from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = '/Users/jinseunghee/Documents/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("https://davelee-fun.github.io/ ")

pages = driver.find_elements_by_css_selector(".ml-1.mr-1")

for i in range(6):
    
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    elems = driver.find_elements_by_css_selector("div.card-body > h4")
    
    for elem in elems:
        print(elem.text)

    pages = driver.find_elements_by_css_selector(".ml-1.mr-1")
    pages[-1].click()
    
    time.sleep(3)
    

driver.quit()