# -*- coding: utf-8 -*-
import scrapy
from splider_multi.items import SexMenItem
import re
import sys
sys.path.append("././splider_multi/db")
from do_sqlalchemy import addEnglishName,initDb2,buildInsertSQL

class SexMenSpider(scrapy.Spider):
    name = 'sexmen'
    allowed_domain = ['http://www.happyjuzi.com']
   
    start_urls = \
        ['http://www.happyjuzi.com/star-ku-3-1-0-0-0-0-0/p{}.html'.format(i) for i in range(1, 106)]
        # ['http://www.happyjuzi.com/star-ku-5-1-0-0-0-0-0/p{}.html'.format(i) for i in range(1, 187)] 
    # ['http://www.happyjuzi.com/star-ku-4-1-0-0-0-0-0/p{}.html'.format(i) for i in range(1, 114)] 
    
    

    def parse(self, response):
        ids = response.xpath('//div[@class="star_hotstar"]//a[@class="name_hotstar"]/@href').extract()
        with open('log.txt', 'a') as a_writer:
            for id in ids:
                try:
                    item = SexMenItem()
                    star_id = re.findall("\d+", id)[0]
                    albumUrl= 'http://www.happyjuzi.com/star-picture-'+star_id
                    item['user_id'] = star_id
                    item['referer'] = albumUrl
                    item['title'] = albumUrl
                    
                    a_writer.write(f'{star_id}\n')
                    print('id:{}'.format(star_id))
                    # try:
                    #     conn=initDb2('CrawlerImg.db')
                    #     rukuDic = {
                    #         'user_id':str(star_id),
                    #         'tag':3
                    #         }
                    #     executeSql=buildInsertSQL(conn,'tbl_sexmen_name', rukuDic)
                    #     conn.execute(executeSql)
                    # except Exception as e:
                    #     print(f'\n*******{e} \n')
                except Exception as e:
                    print(f'error is {e}')
    
        
        
    # def parse_detail(self,response):
    #     url = []
    #     item = response.meta['item']
    #     raw_download_urls = response.xpath('//div[@class="star-pic load-img"]/@data-src').getall()
    #     nameLst = response.xpath('//strong[@class="name_starindex"]/text()').extract()
    #     print(f'姓名：{nameLst[0]}')
    #     item['title'] = nameLst[0]
    #     for raw_download_url in raw_download_urls:
    #         url.append(raw_download_url)
    #     item['url'] = url
    #     yield item