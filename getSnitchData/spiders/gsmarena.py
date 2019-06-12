import scrapy
from ..items import AlphaItem
from genTags import articleTags

class alphaspider(scrapy.Spider):
    name = 'GSMArena'
    page_no = 2
    start_urls = ['https://www.gsmarena.com/news.php3?iPage=1']
    
    def parse(self, response):

        items = AlphaItem()

        res = response.xpath('//div[@class="news-item"]')
        
        for r in res:
            title = r.xpath('a/h3/text()').get()
            discription = r.xpath('p/text()').get()
            link = r.xpath('div[1]/a/@href').get()  
            img_link =  r.xpath('div[1]/a/img/@src').get()         

            items['title'] = title
            items['discription'] = discription
            items['link'] = 'https://www.gsmarena.com/'+link
            items['img_link'] = img_link
            items['tags'] = articleTags(title)

            yield items
            
        next_page = 'https://www.gsmarena.com/news.php3?iPage='+ str(alphaspider.page_no)
        print(next_page)
        if alphaspider.page_no < 4:
            alphaspider.page_no +=1
            yield response.follow(next_page, callback = self.parse)