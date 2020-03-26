import scrapy

class kaoyan(scrapy.Spider):

    name = "kaoyan" #定义蜘蛛名

    def start_requests(self):
        #爬取url
        urls = [
            'http://lab.scrapyd.cn/page/1/',
            'http://lab.scrapyd.cn/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)  #爬取的页面交给parse方法处理

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'kaoyan-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('保存文件: %s ' % filename)    #打日志