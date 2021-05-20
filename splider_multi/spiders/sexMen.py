# -*- coding: utf-8 -*-
import scrapy
from splider_multi.items import SexMenItem
import re

class SexMenSpider(scrapy.Spider):
    name = 'sexmen'
    allowed_domain = ['http://www.happyjuzi.com']
   
    start_urls = \
    ['http://www.happyjuzi.com/star-ku-5-1-0-0-0-0-0/p{}.html'.format(i) for i in range(1, 20)]         
    # ['http://www.happyjuzi.com/star-ku-3-1-0-0-0-0-0/p{}.html'.format(i) for i in range(1, 41)]
    # ['http://www.happyjuzi.com/star-ku-4-1-0-0-0-0-0/p{}.html'.format(i) for i in range(1, 41)] 

    # ['http://www.happyjuzi.com/star-ku-5-1-0-0-0-0-0/p{}.html'.format(i) for i in range(1, 187)] 
    # + \
    # ['http://www.happyjuzi.com/star-ku-3-1-0-0-0-0-0/p{}.html'.format(i) for i in range(1, 106)]
    

    def parse(self, response):
        ids = response.xpath('//div[@class="star_hotstar"]//a[@class="name_hotstar"]/@href').extract()
        for id in ids:
            try:
                item = SexMenItem()
                star_id = re.findall("\d+", id)[0]
                for i in range(1,6):
                    albumUrl= 'http://www.happyjuzi.com/star-picture-'+ star_id + f'/p{int(i)}.html'
                    print(f"albumUrl:  {albumUrl}")
                    item['user_id'] = star_id
                    item['referer'] = 'http://www.happyjuzi.com/star-picture-'+ star_id +'/.html'
                    print(f"albumUrl:{albumUrl}")
                    yield scrapy.Request(albumUrl, callback=self.parse_detail,meta={'item': item})
                    print('id:{}'.format(star_id))
            except Exception as e:
            	print(f'error is {e}')
    
    def parse_detail(self,response):
        url = []
        item = response.meta['item']
        raw_download_urls = response.xpath('//div[@class="star-pic load-img"]/@data-src').getall()
        nameLst = response.xpath('//strong[@class="name_starindex"]/text()').extract()
        enameLst = response.xpath('//strong[@class="ename_starindex"]/text()').extract()
        pageUrl = response.xpath('//img[@class="i_starimg_starindex"]/@src').extract()
        # print(f'姓名：{nameLst[0]}')
        item['title'] = nameLst[0]
        item['ename'] = enameLst[0]
        item['pageUrl'] = pageUrl[0]
        for raw_download_url in raw_download_urls:
            url.append(raw_download_url)
        item['urls'] = url
        yield item