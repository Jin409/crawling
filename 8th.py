# 셀레니움에서만 xpath 활용 가능. bs4 활용 불가능
# find_element_by_xpath

# 문법 //tagname[@Attribute='value']
# / 절대경로 나타냄
# // 상대경로
# *[@href] href 인 태그 모두 선택
# div[@*] 속성이 하나라도 있는 경우의 div 태그
# 특정 행 선택 (//tr)[last()] 마지막 행 (//tr)[position()=2] 두번쨰 행
# 아무 속성이나 //p[@*] p 태그인데 어떤 속성이든 가진 경우

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chromedriver = '/Users/jinseunghee/Documents/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("https://heethehope.tistory.com/")
# driver.get("https://heethehope.tistory.com/entry/TIL-002-2022-02-28")

title = driver.find_elements_by_xpath("//*[@class='title']")
print(title[0].text)

# table = driver.find_element_by_xpath("(//tr)[last()]")
# print(table.text)

driver.quit()