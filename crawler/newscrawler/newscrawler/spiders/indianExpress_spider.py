import scrapy
import sys
from newscrawler.items import NewscrawlerItem
from scrapy.selector import HtmlXPathSelector
#FirstPost - //div[@class="arc_newslist"]/.//a/@href
class HinduSpider(scrapy.Spider):
    name = "indianexpress"
    allowed_domains = ["archive.indianexpress.com"]
    start_urls = [
         #"http://www.thehindu.com/archive/web/2014/01/01/"#,
         "http://archive.indianexpress.com/archive/news/2/1/2014/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        links = response.xpath('//div[@id="box_left"]/*//@href').extract()
        #links = response.xpath('//ul[@class="archiveDayList hide"]/*//@href').extract()

        for l in links:
            print l
            yield scrapy.Request(l.encode('utf-8'),callback = self.process)

        
    def process(self,response):
        title  = response.xpath('//div[@class="mainblock"]/*//h1').extract()
        body = response.xpath('//div[@class="ie2013-contentstory"]/p/text()').extract()
        filename = "IE02-01-2014.txt"
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