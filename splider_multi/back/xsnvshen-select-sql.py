# -*- coding: utf-8 -*-
import scrapy
from splider_multi.items import XsnvshencomItem
import sys
sys.path.append("././splider_multi/db")
from do_sqlalchemy import addEnglishName,initDb2,buildInsertSQL

class XsnvshenSpider(scrapy.Spider):
    name = 'xsnvshen'
    allowed_domains = ['xsnvshen.com']
    # start_urls = ['https://www.xsnvshen.com/album/?p=356'] 
    start_urls = ['https://www.xsnvshen.com/album/?p=89']  
    # 54 -- 128  350-355

    def parse(self, response):
        try:
            conn=initDb2()
            result=conn.execute("SELECT t.img_url,t.remark1,SUBSTR(t.img_url,32,5) as person_id from tbl_xsnvshen_test t    order by t.remark1").fetchall()
            result=result[0:10]
            for row in result:
                item = XsnvshencomItem()
                print(row[0])
                item['url']=row[0]
                item['page']=row[1]
                item['title']=row[2]
                yield item
            print(f"\n 当前第{str(item['page'])}页\n")
        except Exception as e:
            print(f'\n*******{e} \n')
