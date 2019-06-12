import scrapy
from ..items import AlphaItem
from genTags import articleTags

class alphaspider(scrapy.Spider):
    name = 'news18'
    page_no = 2
    start_urls = ['https://www.news18.com/world/page-1/']
    
    def parse(self, response):

        items = AlphaItem()

        res = response.xpath('//div[@class="blog-list-blog"]')
        
        for r in res:
    
            title = r.xpath('figure/a/img/@title').get()
            link = r.xpath('figure/a/@href').get()  
            img_link =  r.xpath('figure/a/img/@src').get()         

            items['title'] = title
            items['link'] = link
            items['img_link'] = img_link
            items['tags'] = articleTags(title)

            yield items
            
        next_page = 'https://www.news18.com/world/page-'+ str(alphaspider.page_no)
        print(next_page)
        if alphaspider.page_no < 14:
            alphaspider.page_no +=1
            yield response.follow(next_page, callback = self.parse)