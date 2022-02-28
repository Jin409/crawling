from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chromedriver = '/Users/jinseunghee/Documents/chromedriver'
driver = webdriver.Chrome(chromedriver)

#내 티스토리 제목 전부 프린트하기 

driver.get("https://heethehope.tistory.com/")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
elem = driver.find_elements_by_class_name("title") #리스트로 저장됨. 
for i in range(len(elem)):
    print(elem[i].text)
    print("========")
driver.quit()