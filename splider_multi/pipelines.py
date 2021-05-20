# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib
import os
import sys
import time
sys.path.append("./splider_multi/db")
# from myDb import writeDB
from do_sqlalchemy import addEnglishName,initDb2,buildInsertSQL
import scrapy
import random
from config import USER_AGENTS_LIST
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from scrapy.exceptions import DropItem
import threading
from loguru import logger
import h5py
import time

x = time.localtime(time.time())
nowTime = time.strftime('%Y-%m-%d',x)
logger.add(f"splider_{nowTime}.log", format="{time} {level} {message}", filter="", level="DEBUG")
threadLock = threading.Lock()

def listToString(s):  
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    # return string   
    return str1  

class XsnvshencomPipeline(object):
    def process_item(self, item, spider):
        folder_name = item['title'].replace(r'/', '').rstrip()
        referer=item['referer']
        now_page=item['page']
        urls=item['url']
        logger.info(f"urls:{urls}")
        out_file=item['out_file']
        try:
            x = time.localtime(time.time())
            nowTime = time.strftime('%Y-%m-%d %H:%M:%S',x)
            lst_dic=[]
            for url in urls:
                person_id=str(url).split('/')[-3]
                album=str(url).split('/')[-2]
                img_id=str(url).split('/')[-1].replace('.jpg','')
                dic = {
                'url': str(referer), 
                'img_url':str(url),
                'folder_name':str(folder_name),
                'crawlTime': nowTime,
                # 'remark1':str(now_page),
                'key':f"{str(person_id)}_{str(album)}_{str(img_id)}"
                }
                lst_dic.append(dic)
            logger.info(f"lst_dic:{len(lst_dic)}")
            # self.write_h5(lst_dic,out_file)
            logger.info(f"\n 当前第{now_page}页\n")

        except Exception as e:
            logger.error(f'process_item:the error is:{e} \n')
        return item
    
    def write_h5(self,lst_dic,out_file):
        try:
            if lst_dic is None or len(lst_dic)==0:
                return
            # write new h5 data
            threadLock.acquire()
            with h5py.File(out_file,'a') as f:
                for dic in lst_dic:
                    key=dic['key']
                    url=dic['url']
                    img_url=dic['img_url']
                    folder_name=dic['folder_name']
                    crawlTime=dic['crawlTime']
                    # remark1=dic['remark1']
                    if f.get(key) is  None:
                        ofi = f.create_group(key)
                        ofi.create_dataset('url', data=url)
                        ofi.create_dataset('img_url', data=img_url)
                        ofi.create_dataset('folder_name', data=folder_name)
                        ofi.create_dataset('crawlTime', data=crawlTime)
                        # ofi.create_dataset('remark1', data=remark1)
                threadLock.release()
        except Exception as e:
            logger.error(f"write_h5:the error is {e}")

'''
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from loguru import logger
logger.add(f"splider.log", format="{time} {level} {message}", filter="", level="DEBUG")

class XsnvshencomPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for download in item['url']:
            yield scrapy.Request(download, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        urls=item['url']
        now_page=item['page']
        logger.info(f"\n 当前第{now_page}页\n")
        # print(f"urls:{urls}")
        if(len(urls)>0):
          person_id=str(urls[0]).split('/')[-3]
          folder_name = item['title'].replace(r'/', '').rstrip()
          img_guid = request.url.split('/')[-1]
          img_name = img_guid
          filename = u'{0}/{1}'.format(person_id, img_name)
          # filename = u'{0}/{1}'.format(folder_name, img_name)
          return filename

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('IMG download Failed')
        return item
'''