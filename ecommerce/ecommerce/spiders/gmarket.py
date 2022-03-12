import scrapy


class GmarketSpider(scrapy.Spider):
    name = 'gmarket'
    allowed_domains = ['www.gmarket.co.kr'] # 다른 사이트들을 크롤링 하는 것을 막겠다.\
        # 해당 사이트 주소가 포함 된 경우에만 크롤링 하겠다.
    start_urls = ['http://www.gmarket.co.kr/']

    def parse(self, response):
        print(response.text)
