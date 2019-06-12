import scrapy
from ..items import AlphaItem
from genTags import articleTags

class alphaspider(scrapy.Spider):
    name = 'ETimes'
    start_urls = ['https://economictimes.indiatimes.com/news/international/business']
    
    def parse(self, response):

        items = AlphaItem()

        res = response.xpath('//div[@class="eachStory"]')
        
        for r in res:
    
            title = r.xpath('h3/a/text()').get()
            link = r.xpath('a/@href').get()  
            img_link =  r.xpath('a/span/img/@src').get()      
            discription = r.xpath('p/text()').get()   

            items['title'] = title
            items['link'] = 'https://economictimes.indiatimes.com'+link
            items['img_link'] = img_link
            items['discription'] = discription
            items['tags'] = articleTags(title)

            yield items
            
