import scrapy
from ..items import AlphaItem
from genTags import articleTags

class alphaspider(scrapy.Spider):
    name = 'barcablaugranes'
    start_urls = ['https://www.barcablaugranes.com/']
    
    def parse(self, response):

        items = AlphaItem()

        res = response.xpath('//div[@class="c-entry-box--compact c-entry-box--compact--article"]')
        
        for r in res:
            title = r.xpath('div/h2/a/text()').get()
            discription = r.xpath('div/p/text()').get()
            link = r.xpath('div/h2/a/@href').get()  
            img_link =  r.xpath('a[1]/div/img/@src').get()         

            items['title'] = title
            items['discription'] = discription
            items['link'] =link
            items['img_link'] = 'https://www.barcablaugranes.com/'+img_link
            items['tags'] = articleTags(title)

            yield items
            