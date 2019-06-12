import scrapy
from ..items import AlphaItem
from genTags import articleTags

class alphaspider(scrapy.Spider):
    name = 'ndtv'
    page_no = 2
    start_urls = ['https://www.ndtv.com/world-news/page-1']
    
    def parse(self, response):

        items = AlphaItem()

        res = response.xpath('//div[@class="new_storylising_img"]')
        
        for r in res:
    
            title = r.xpath('a/@title').get()
            discription = r.xpath('following-sibling::div/div[3]/text()').get()
            link = r.xpath('a/@href').get()  
            img_link =  r.xpath('a/img/@src').get()         

            items['title'] = title
            items['discription'] = discription
            items['link'] = link
            items['img_link'] = img_link
            items['tags'] = articleTags(title)

            yield items
            
        next_page = 'https://www.ndtv.com/world-news/page-'+ str(alphaspider.page_no)
        print(next_page)
        if alphaspider.page_no < 5:
            alphaspider.page_no +=1
            yield response.follow(next_page, callback = self.parse)