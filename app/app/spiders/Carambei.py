import scrapy


class CarambeiSpider(scrapy.Spider):
    name = 'Carambei'
    allowed_domains = ['carambei.pr.gov.br']
    start_urls = ['https://carambei.atende.net/?pg=transparencia#!/']

    def parse(self, response):
        print("response")
        print(response)
        pass
