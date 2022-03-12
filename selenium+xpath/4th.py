#headless chrome

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("window-size=1920x1080")
options.add_argument('User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36')
options.add_argument("lang=ko_KR")
options.add_argument("disable-gpu")
chromedriver = '/Users/jinseunghee/Documents/chromedriver'
driver = webdriver.Chrome(chromedriver,options=options)
driver.get("https://heethehope.tistory.com/")

elem = driver.find_element_by_tag_name("h1")
print(elem.text)

driver.quit()
