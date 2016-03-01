import scrapy
import sys
from newscrawler.items import NewscrawlerItem
from scrapy.selector import HtmlXPathSelector

class HinduSpider(scrapy.Spider):
    name = "hindu"
    allowed_domains = ["thehindu.com"]
    start_urls = [
         #"http://www.thehindu.com/archive/web/2014/01/03/"#,
         "http://www.thehindu.com/template/1-0-1/widget/archive/archiveWebDayRest.jsp?d=2014-01-07"
    ]

    def parse(self, response):
        #links = response.xpath('//ul[@class="archiveDayList hide"]/*//@href').extract()
        links = response.xpath('//ul[@class="archiveDayRestList hide"]/*//@href').extract()

        for l in links:
            print l
            yield scrapy.Request(l.encode('utf-8'),callback = self.process)

        
    def process(self,response):
        title  = response.xpath('//h1[@class="detail-title"]/text()').extract()
        body = response.xpath('//div[@class="article-text"]/.//p[@class="body"]/text()').extract()
        filename = "07-01-2014.xml"
        f = open(filename, 'a')
        f.write('<title>')
        for t in title:
            f.write(t.encode('utf-8'))
        f.write('</title>\n')
            
            
        f.write('<body>')
        print "body",len(body)
        for b in body:
            #print "body----->",b
            f.write(b.encode('utf-8'))
        f.write('</body>\n')
        f.close()