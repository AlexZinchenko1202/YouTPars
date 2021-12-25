import scrapy
from urllib.parse import urljoin

'''
def op(adr):
    with open(adr) as file:
        return file.read()


class YoutubeSpider(scrapy.Spider):
    #name = 'youtube_tablets'
    name = 'pwspider'
    #allowed_domains = ['youtube.com']
    start_urls = ['http://www.youtube.com/channel/UCZF6XvqkFb9lURwIPePFU5w/about']

    def start_requests(self):
    	yield scrapy.Request('http://www.youtube.com/channel/UCZF6XvqkFb9lURwIPePFU5w/about')
            #'https://shoppable-campaign-demo.netlify.app/#/',meta = {'playwright':True})

    async def parse(self, response):
        for post_link in response.xpath('//*[@id="description"]').extract():
            url = urljoin(response.url, post_link)
            yield {'1':url}

        # print(response)
        # yield {'1':responce}
        #yield {'descr':response.css('#description-container').extract()} # .css('yt-formatted-string:nth-child(2)').extract()
        
        for _, cont in enumerate(response.css('#link-list-container > a:nth-child')):
            yield {str(_):cont.css('yt-formatted-string:nth-child(1)').get()}
        
        # yield {
        #     'descr':response.css('#link-list-container > a:nth-child(1) > yt-formatted-string:nth-child(1)').extract()
        # 	'text':response.text
        # 	}
        
        #print(response.css('#link-list-container > a:nth-child(1)').extract())

# start_urls = ['http://www.youtube.com/channel/UCZF6XvqkFb9lURwIPePFU5w/about']
# spider = YoutubeSpider()
# for url in start_urls:
#     spider.parse()

# spiders$ scrapy crawl pwspider -o output2.json

code = eval(op('output3.jsonlines'))['text']
from bs4 import BeautifulSoup as bs

soup = bs(code, 'lxml')
print([i for i in soup.find_all('div') if 'yt' in str(i)]) #, class_='style-scope ytd-channel-about-metadata-renderer'))
'''
class MySpider(scrapy.Spider):
    name = "jsscraper"
    start_urls = ["http://quotes.toscrape.com/js/"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
            url=url, callback=self.parse, endpoint='render.html'
        )

    def parse(self, response):
        for q in response.css("div.quote"):
            quote = QuoteItem()
            quote["author"] = q.css(".author::text").extract_first()
            quote["quote"] = q.css(".text::text").extract_first()
            yield quote
