import scrapy
from ..items import AlphaItem
from genTags import articleTags

class alphaspider(scrapy.Spider):
    name = 'Bolly_hungama'
    page_no = 2
    start_urls = ['https://www.bollywoodhungama.com/bollywood/page/1/']
    
    def parse(self, response):

        items = AlphaItem()

        res = response.xpath('//article[@class="bh-cm-box bh-box-article hentry"]')
        
        for r in res:
    
            title = r.xpath('h3/a/text()').get()
            link = r.xpath('h3/a/@href').get()  
            img_link =  r.xpath('figure/a/img/@src').get()         

            items['title'] = title
            items['link'] = link
            items['img_link'] = img_link
            items['tags'] = articleTags(title)

            yield items
            
        next_page = 'https://www.bollywoodhungama.com/bollywood/page/'+ str(alphaspider.page_no)
        print(next_page)
        if alphaspider.page_no < 5:
            alphaspider.page_no +=1
            yield response.follow(next_page, callback = self.parse)