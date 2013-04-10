#coding: utf-8

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/" 
#        "https://www.google.com/#hl=zh-CN&site=&source=hp&q=3&fp=1"
        "http://www.baidu.com/s?wd=3&rsv_bp=0&rsv_spt=3&inputT=370"
        ]
    def __init__(self):
        self.count = 0
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//h3[@class="t"]')
        new_urls = []
        if sites == []:
            #print hxs.extract()
            print 1
            self.count += 1
            print self.count
        else:
            for site in sites:
                p = site.select('a/@href').extract()            
                url = p[0].__str__()
                print 'url: ', url
                new_urls.append(self.make_requests_from_url(url))
        return new_urls
