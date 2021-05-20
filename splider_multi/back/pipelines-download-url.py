# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib
import os
import sys
import time
from pathlib import Path
from pypinyin import pinyin, lazy_pinyin
sys.path.append("./splider_multi/db")
# from myDb import writeDB
from do_sqlalchemy import addEnglishName,initDb2,buildInsertSQL
import scrapy
import random
import shutil
from config import USER_AGENTS_LIST
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from scrapy.exceptions import DropItem
# 导入项目设置
from scrapy.utils.project import get_project_settings

def listToString(s):  
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    # return string   
    return str1  
class IvskyPipeline(object):
    #图片保存目录
    basePath = '/content/drive/My Drive/spiderIvskyCode/spider_ivsky-master/myface/'
    def process_item(self, item, spider):
        #header参数
        user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        referer = item['referer']
        header = {
            'user_agent':user_agent,
            'Referer':referer
        }
        #图片地址
        url = item['url']
        #图片名字
        name = item['name']
        #图片保存地址
        path = self.basePath + item['pos']
        resolution=item['resolution']
        referer=item['referer']
        category=item['pos']
        filterName=category.replace('/','').replace('\\','').replace('-','').replace(' ','').replace('《','').replace('》','') \
        .replace('女性','').replace('壁纸','').replace('首页','').replace('桌面','').replace('时尚','').replace('写真','').replace('性感','') \
        .replace('小姐','').replace('甜美','').replace('美女','').replace('性感','').replace('迷人','').replace('优雅','') \
        .replace('明星','').replace('高清','').replace('可爱','').replace('歌手','').replace('演员','') \
        .replace('性感','')
        filterName=str(filterName)
        namePinyinLst=lazy_pinyin(filterName)
        namePinyin=listToString(namePinyinLst)
        if not os.path.exists( path = path + '/{name}.jpg'.format(name=name) ):
            #如果不存在图片文件
            if not os.path.exists(path):
                #如果不存在图片位置的目录，则创建目录
                os.makedirs(path)
            print('\n### 正在保存{name} ###\n'.format(name=name))
            print(f'\n*******{path} \n')
            x = time.localtime(time.time())
            nowTime = time.strftime('%Y-%m-%d %H:%M:%S',x)
            rukuDic = {
                'urlSign': str(name), 
                'url': str(url), 
                'sourceUrl': str(referer), 
                'domain': str(name), 
                'isAlbum': 0, 
                'category': str(category),
                'images':'',
                'text':str(resolution),
                'crawlTime': nowTime,
                'status': 0,
                'tags':str(namePinyin),
                'title':'',
                }
            try:
                # ...
                print("***********000000000***************")
                # writeDB('tbl_content', rukuDic)
                print("***********1111111111***************")

            except Exception as e:
                print(f'\n*******{e} \n')
        else:
            #如果已经存在图片文件
            print('\n### {name} 已经存在  ###\n'.format(name=name))
        
        return item

class ZolPipeline(object):
    #图片保存目录
    basePath = '/content/drive/My Drive/spiderIvskyCode/spider_ivsky-master/myface/'
    def process_item(self, item, spider):
        #header参数
        user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        referer = item['referer']
        header = {
            'user_agent':user_agent,
            'Referer':referer
        }
        #图片地址
        url = item['url']
        #图片名字
        name = item['name']
        #图片保存地址
        path = self.basePath + item['pos']
        resolution=item['resolution']
        category=item['pos']
        sourceUrl=item['sourceUrl']
        filterName=category.replace('/','').replace('\\','').replace('-','').replace(' ','').replace('《','').replace('》','') \
        .replace('女性','').replace('壁纸','').replace('首页','').replace('桌面','').replace('时尚','').replace('写真','').replace('性感','') \
        .replace('小姐','').replace('甜美','').replace('美女','').replace('性感','').replace('迷人','').replace('优雅','') \
        .replace('明星','').replace('高清','').replace('可爱','').replace('歌手','').replace('演员','') \
        .replace('性感','')
        filterName=str(filterName)
        namePinyinLst=lazy_pinyin(filterName)
        namePinyin=listToString(namePinyinLst)
        if not os.path.exists( path = path + '/{name}.jpg'.format(name=name) ):
            #如果不存在图片文件
            if not os.path.exists(path):
                #如果不存在图片位置的目录，则创建目录
                os.makedirs(path)
            # print('\n### 正在保存{name} ###\n'.format(name=name))
            # print(f'\n*******{path} \n')
            x = time.localtime(time.time())
            nowTime = time.strftime('%Y-%m-%d %H:%M:%S',x)
            rukuDic = {
                'urlSign': str(name), 
                'url': str(url), 
                'sourceUrl': str(sourceUrl), 
                'domain': str(name), 
                'isAlbum': 0, 
                'category': str(category),
                'images':'',
                'text':str(resolution),
                'crawlTime': nowTime,
                'status': 0,
                'tags':str(namePinyin),
                'title':'',
                }
            try:
                conn=initDb2()
                executeSql=buildInsertSQL(conn,'tbl_content', rukuDic)
                # print("\n**********\n",executeSql)
                conn.execute(executeSql)
            except Exception as e:
                print(f'\n*******{e} \n')
        else:
            #如果已经存在图片文件
            print('\n### {name} 已经存在  ###\n'.format(name=name))
        
        return item

class StarPipeline(object):
    def process_item(self, item, spider):
        url=item['url']
        #地址
        url = item['url']
        img_url = item['img_url']
        #名字
        chinese_name = item['chinese_name']
        english_name = item['english_name']
        used_name = item['used_name']
        nation = item['nation']
        representative = item['representative']
        relatedStar = item['relatedStar']
        personal = item['personal']
        microblog = item['microblog']
        x = time.localtime(time.time())
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S',x)
        rukuDic = {
            'url': str(url), 
            'img_url':str(img_url),
            'chinese_name': str(chinese_name), 
            'english_name': str(english_name), 
            'used_name': str(used_name), 
            'nation': str(nation),
            'representative':str(representative),
            'relatedStar':str(relatedStar),
            'personal': str(personal),
            'microblog':str(microblog),
            'crawlTime': nowTime,
            }
        try:
            conn=initDb2()
            executeSql=buildInsertSQL(conn,'tbl_star2', rukuDic)
            conn.execute(executeSql)
        except Exception as e:
            print(f'\n*******{e} \n')

        return item

class XsnvshencomPipeline(ImagesPipeline):
    # 从项目设置文件中导入图片下载路径
    img_store = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        print("1111111111")
        # for download in item['url']:
        download=item['url']
        print(download)
        yield scrapy.Request(download, meta={'item': item})


    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        folder_name = item['title'].replace(r'/', '').rstrip()
        img_guid = request.url.split('/')[-1]
        img_name = img_guid
        filename = u'{0}/{1}'.format(folder_name, img_name)
        return filename

    # def item_completed(self, results, item, info):
    #     print("456132")
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     if not image_paths:
    #         raise DropItem('IMG download Failed')
    #     return item

class sexMenPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        ...
    #     for download in item['url']:
    #         yield scrapy.Request(download, meta={'item': item})

    # def file_path(self, request, response=None, info=None):
    #     item = request.meta['item']
    #     user_id = item['user_id']
    #     print(f'用户ID: {user_id}\n')

    #     folder_name = item['title'].replace(r'/', '').rstrip()
    #     print(folder_name,'\n')

    #     referer=item['referer']
    #     print(referer,'\n')

    #     url=request.url
    #     print('\n',url,'\n')
    #     img_guid = request.url.split('/')[-1]
    #     img_name = img_guid
    #     filename = u'{0}/{1}'.format(folder_name, img_name)
    #     try:
    #         conn=initDb2()
    #         x = time.localtime(time.time())
    #         nowTime = time.strftime('%Y-%m-%d %H:%M:%S',x)
    #         rukuDic = {
    #             'url': str(referer), 
    #             'img_url':str(url),
    #             'folder_name':str(folder_name),
    #             'crawlTime': nowTime,
    #             'remark1':str(user_id)
    #             }
    #         executeSql=buildInsertSQL(conn,'tbl_sexmen', rukuDic)
    #         conn.execute(executeSql)
    #     except Exception as e:
    #         print(f'\n*******{e} \n')
        

    #     return filename

    # def item_completed(self, results, item, info):
    #     print("456132")
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     if not image_paths:
    #         raise DropItem('IMG download Failed')
    #     return item