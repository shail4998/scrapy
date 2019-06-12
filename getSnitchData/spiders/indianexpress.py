import scrapy
from ..items import AlphaItem
from genTags import articleTags

class alphaspider(scrapy.Spider):
    name = 'indianExpress'
    start_urls = ['https://indianexpress.com/article/world/']
    
    def parse(self, response):

        items = AlphaItem()

        res = response.xpath('//div[@class="m-article-landing  m-block-link"]')
        
        for r in res:
            title = r.xpath('div[2]/h2/a/@title').get()
            discription = r.xpath('div[2]/h3/text()').get()
            link = r.xpath('div[2]/h2/a/@href').get()  
            img_link =  r.xpath('div[1]/div/a/picture/img/@src').get()         

            items['title'] = title
            items['discription'] = discription
            items['link'] = link    
            items['img_link'] = img_link
            items['tags'] = articleTags(title)

            yield items
        