import scrapy
import time

class tool(scrapy.Spider):

    name = "tool" #定义蜘蛛名

    def start_requests(self):
        #爬取url
        urls = [
            'https://tool.lu/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)  #爬取的页面交给parse方法处理

    def parse(self, response):
        times = time.time()
        filename = 'tool' + str(times) + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('保存文件: %s ' % filename)    #打日志