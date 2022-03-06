# 동적 크롤링
# 정적으로 가져온 데이터가 아닌 경우

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chromedriver = '/Users/jinseunghee/Documents/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chromedriver,options=options)

# 크롤링할 사이트 호출
driver.get("https://davelee-fun.github.io/blog/TEST/index.html")

# 웹페이지가 모두 로드 되기 전, 즉 자바스크립트가 실행되지 않기 전에 크롤링이 실행되게 되면,
# news가 나타나기 전에 크롤링이 되므로 이가 없다고 인지될 수도 있다. 
# 따라서 시간을 지체하는 time.sleep 을 사용함. 

time.sleep(2)

elem = driver.find_element_by_css_selector(".news")
print (elem.text)

driver.quit()