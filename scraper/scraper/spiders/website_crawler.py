from pathlib import Path

import scrapy
from scrapy.crawler import CrawlerProcess

class WebsiteSpider(scrapy.Spider):

    name = "my_downloader"

    def __init__(self, url=None, *args, **kwargs):
        super(WebsiteSpider, self).__init__(*args, **kwargs)
        self.url = url

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"../../../../pages/{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

def run_spider(url):
    process = CrawlerProcess()
    process.crawl(WebsiteSpider, url=url)
    process.start()

if __name__ == '__main__': # tests
    run_spider("https://theuselessweb.com/")