# -*- coding: utf-8 -*-
import scrapy
from splider_multi.items import XsnvshencomItem
from loguru import logger
import time
END_PAGE=400
# out_file='/content/drive/My Drive/nvshen'
out_file= 'E:/nvshen'
# out_file='/content/drive/My Drive/nvshen'



class XsnvshenSpider(scrapy.Spider):
    name = 'xsnvshen'
    allowed_domains = ['xsnvshen.com']
    start_urls = ['https://triplegangers.com/search-products/female']

    # def __init__(self, **kwargs):
    #     super(XsnvshenSpider, self).__init__(**kwargs)
    #     if isinstance(self.start_urls, str):
    #         self.start_urls = self.start_urls.split(',')

    def parse(self, response):
        # logger.info(f"headers: {response.headers},status:{response.status},request:{response.request}")
        # return
        try:
            tities = response.xpath('//div[@class="camLiCon"]/div/p/a/text()').getall()
            urls = response.xpath('//div[@class="camLiCon"]/div/p/a/@href').getall()
            next_page = response.xpath('//div[@id="pageNum"]/a[last()]/@data-page').get()
            now_page = response.url.split('=')[-1]

            end_page=END_PAGcam
            for title, raw_url in zip(tities, urls):
                detail_url = 'https://www.xsnvshen.com' + raw_url
                item = XsnvshencomItem()
                item['title'] = title
                item['page'] = now_page
                yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'item': item})

            if next_page is not now_page or None:
                if next_page is None:
                    next_page=str(int(now_page)+1)
                    # next_page = response.xpath('//div[@id="pageNum"]/a[last()]/@data-page').get()
                    logger.info(f"try again,{response},,, {response.body} ,{next_page}")
                new_url = response.url.split('=')[0] + '=' +  next_page
                yield scrapy.Request(new_url, callback=self.parse)
        except Exception as e:
            logger.error(f"parse error {e}")

        # if next_page is not now_page or next_page is not None:
        #     new_url=response.url.split('=')[0] + '=' +  now_page
        #     if next_page is  None:
        #         # new_url = response.url.split('=')[0] + '=' +  now_page
        #         next_page=str(int(now_page)+1)
        #     new_url = response.url.split('=')[0] + '=' +  next_page
            
        #     # if int(now_page)>=end_page:
        #     #     logger.info("IT'S END")
        #     #     return
        #     yield scrapy.Request(new_url, callback=self.parse)
        # else:
        #     logger.error(f"now_page:{now_page},next_page:{next_page}")

    def parse_detail(self,response):
        item = response.meta['item']
        url = []
        raw_download_urls = response.xpath('//ul[contains(@class,"clearfix") and contains(@class, "gallery")]//li/div/img/@src').getall()
        for raw_download_url in raw_download_urls:
            download_url = response.urljoin(raw_download_url).split('/')
            raw_url = 'https://img.xsnvshen.com/' + '/'.join(download_url[-4:])
            url.append(raw_url)
        item['url'] = url
        referer = response.url
        item['referer'] = referer
        item['out_file']=f"{out_file}/{END_PAGE}.h5"
        yield item