import scrapy
from ..items import AlphaItem
from genTags import articleTags

class alphaspider(scrapy.Spider):
    name = 'firstPost'
    page_no = 2
    start_urls = ['https://www.firstpost.com/category/india/page/1']
    
    def parse(self, response):

        items = AlphaItem()

        res = response.xpath('//a[@class="list-item-link"]')
        
        for r in res:
    
            title = r.xpath('div[1]/img/@title').get()
            link = r.xpath('@href').get()  
            img_link =  r.xpath('div[1]/img/@src').get() 
            discription = r.xpath('div[2]/div/text()').get()        

            items['title'] = title
            items['link'] = link
            items['img_link'] = img_link
            items['tags'] = articleTags(title)
            items['discription'] = discription

            yield items
            
        next_page = 'https://www.firstpost.com/category/india/page/'+ str(alphaspider.page_no)
        print(next_page)
        if alphaspider.page_no < 5:
            alphaspider.page_no +=1
            yield response.follow(next_page, callback = self.parse)