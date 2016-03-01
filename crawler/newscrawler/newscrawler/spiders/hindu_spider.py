import scrapy
import sys
from newscrawler.items import NewscrawlerItem

class HinduSpider(scrapy.Spider):
    name = "hindu"
    allowed_domains = ["thehindu.com"]
    start_urls = [
        "http://www.thehindu.com/archive/web/2014/01/01/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        #links = response.xpath('//div[@class="archiveWebListHolder"]/ul[@class="archiveDayList"]/li/a/@href').extract()
        links = response.xpath('//div[@class="archiveWebListHolder"]/ul/li/a/@href').extract()

        print "LINKS",links,len(links)
            #print "TITLE::",title
        # content = response.body
        # print content
        # title  = response.xpath('//h1[@class="detail-title"]/text()').extract()
        # body = response.xpath('//div[@class="article-text"]/p[@class="body"]/text()').extract()
        # if(len(title) != 0 or len(body) != 0):
        #     f = open(filename, 'wb')
        #     f.write('<title>')
        #     for t in title:
        #         f.write(t)
        #     f.write('</title>\n')
            
            
        #     f.write('<body>')
        #     print "body",len(body)
        #     for b in body:
        #             #print "body----->",b
        #         f.write(b.encode('utf-8'))
        #     f.write('</body>\n')
        #     f.close()
        #for l in links:
        #    print l
            #yield scrapy.Request(l,callback = self.parse)
        
