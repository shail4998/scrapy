import scrapy
from ..items import AlphaItem
from genTags import articleTags

class alphaspider(scrapy.Spider):
    name = 'hindustanTimes'
    page_no = 2
    start_urls = ['https://www.hindustantimes.com/lok-sabha-elections/news/?pageno=1']
    
    def parse(self, response):

        items = AlphaItem()

        res = response.xpath('//div/div[@class="media-heading headingfour"]')
        
        for r in res:
            title = r.xpath('a/text()').get()
            discription = r.xpath('following-sibling::div/text()').get()
            link = r.xpath('a/@href').get()  
            img_link =  r.xpath('parent::div/parent::div/div[1]/div/a/img/@src').get()         

            items['title'] = title
            items['discription'] = discription
            items['link'] = link
            items['img_link'] = img_link
            items['tags'] = articleTags(title)

            yield items
            
        next_page = 'https://www.hindustantimes.com/lok-sabha-elections/news/?pageno='+ str(alphaspider.page_no)
        print(next_page)
        if alphaspider.page_no < 5:
            alphaspider.page_no +=1
            yield response.follow(next_page, callback = self.parse)