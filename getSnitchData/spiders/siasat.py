import scrapy
from ..items import AlphaItem
from genTags import articleTags

class alphaspider(scrapy.Spider):
    name = 'Siasat'
    page_no = 2
    start_urls = ['https://www.siasat.com/category/technology-1/']
    
    def parse(self, response):

        items = AlphaItem()

        res = response.xpath('//article[@class="item-list"]')
        
        for r in res:
            title = r.xpath('div[2]/h2/a/text()').get()
            discription = r.xpath('div[2]/div/p/text()').get()
            link = r.xpath('div[1]/a/@href').get()  
            img_link =  r.xpath('div[1]/a/img/@src').get()         

            items['title'] = title
            items['discription'] = discription
            items['link'] = link
            items['img_link'] = img_link
            items['tags'] = articleTags(title)

            yield items
            
        next_page = 'https://www.siasat.com/category/technology-'+ str(alphaspider.page_no)
        print(next_page)
        if alphaspider.page_no < 5:
            alphaspider.page_no +=1
            yield response.follow(next_page, callback = self.parse)