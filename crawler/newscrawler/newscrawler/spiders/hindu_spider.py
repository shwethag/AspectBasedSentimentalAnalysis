import scrapy
import sys

class HinduSpider(scrapy.Spider):
    name = "hindu"
    allowed_domains = ["thehindu.com"]
    start_urls = [
        "http://www.thehindu.com/sci-tech/cell-phone-waste-the-next-big-threat-to-environment-deloitte/article41896.ece"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            title  = response.xpath('//h1[@class="detail-title"]').extract()
            #print "TITLE::",title
            for t in title:
                f.write(t)
            body = response.xpath('//div[@class="article-text"]/p[@class="body"]').extract()
            for b in body:
                #print "body----->",b
                f.write(b.encode('utf-8'))
            f.close()
