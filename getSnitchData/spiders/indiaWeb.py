import scrapy
from ..items import AlphaItem
from genTags import articleTags

class alphaspider(scrapy.Spider):
    name = 'indiaWeb'
    page_no = 2
    start_urls = ['https://www.indianweb2.com/category/technology/page/2/']
    
    def parse(self, response):

        items = AlphaItem()

        res = response.xpath('//div[@class="list-item"]')
        
        for r in res:
            title = r.xpath('article/div[2]/h3/a/text()').get()
            discription = r.xpath('article/div[2]/div[1]/div/text()').get()
            link = r.xpath('article/div[1]/a/@href').get()  
            img_link =  r.xpath('article/div[1]/a/noscript/img/@src').get()         

            items['title'] = title
            items['discription'] = discription
            items['link'] = link
            items['img_link'] = img_link
            items['tags'] = articleTags(title)

            yield items
            
        next_page = 'https://www.indianweb2.com/category/technology/page/'+ str(alphaspider.page_no)+'/'
        print(next_page)
        if alphaspider.page_no < 5:
            alphaspider.page_no +=1
            yield response.follow(next_page, callback = self.parse)