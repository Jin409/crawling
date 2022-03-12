from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chromedriver = '/Users/jinseunghee/Documents/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("https://comic.naver.com/webtoon/weekday")

#DeprecationWarning: find_elements_by_css_selector is deprecated. 오류가 떠서 아래와 같이 수정!
days = driver.find_elements(By.CSS_SELECTOR, "div.col_inner > h4")

for i in range(7):
    print(days[i].text)
    titles = driver.find_elements(By.CSS_SELECTOR,"div.col_inner > ul")
    print(titles[i].text)
    print("==========")

driver.quit()
