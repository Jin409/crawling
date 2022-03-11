from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve
import time

# url을 이용하여 이미지를 다운로드 받는 라이브러리인 urllib 을 사용해라
# 확장자를 일치시켜야 하기 때문에 확장자가 중요\
    # .split(".")[-1] 하면 이미지의 확장자를 알 수 있다. 
# 셀레니움으로 태그 객체를 가져온 뒤 src 속성을 가져오면 이가 이미지의 링크가 된다.

chromedriver = '/Users/jinseunghee/Documents/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("https://davelee-fun.github.io/ ")

elems= driver.find_elements_by_css_selector("div.wrapthumbnail img")
images = []

for elem in elems:
    images.append(elem.get_attribute('src'))

for index,image in enumerate(images):
    # image 를 url 로 바꿔줌
    # image 라는 폴더에 어떤 이름으로 저장할지 지정해줌. 
    
    urlretrieve(image,"../image/"+str(index)+"."+image.split('.')[-1])

driver.quit()