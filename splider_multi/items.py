# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EnameItem(scrapy.Item):
    # define the fields for your item here like:
    ename = scrapy.Field()
    pronunciation = scrapy.Field()
    cname = scrapy.Field()
    cname_ext = scrapy.Field()
    gender = scrapy.Field()
    origin = scrapy.Field()
    moral = scrapy.Field()
    meaning = scrapy.Field()
    impression = scrapy.Field()
    similar = scrapy.Field()

class StarSpidersItem(scrapy.Item):
	url = scrapy.Field()
	img_url = scrapy.Field()
	chinese_name = scrapy.Field()
	english_name = scrapy.Field()
	used_name = scrapy.Field()
	nation = scrapy.Field()
	location = scrapy.Field()
	birthday = scrapy.Field()
	birthplace = scrapy.Field()
	height = scrapy.Field()
	weight = scrapy.Field()
	bloodType = scrapy.Field()
	constellation = scrapy.Field()
	graduateSchool = scrapy.Field()
	profession = scrapy.Field()
	company = scrapy.Field()
	representative = scrapy.Field()
	microblog = scrapy.Field()
	relatedStar = scrapy.Field()
	personal = scrapy.Field()

class XsnvshencomItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    referer = scrapy.Field()
    page = scrapy.Field()
    out_file=scrapy.Field()

class SexMenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    urls = scrapy.Field()
    referer = scrapy.Field()
    title = scrapy.Field()
    user_id = scrapy.Field()
    ename = scrapy.Field()
    pageUrl = scrapy.Field()
    
    
class Jj20Item(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()