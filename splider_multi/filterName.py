# import sys
# sys.path.append("./db")
# from myDb import getDB,writeDB
# from pypinyin import pinyin, lazy_pinyin
# import re
# import time

# FILTER_WORDS=[
#     '/','/','\\','-',' ','《','》','.','·', '：',
# '男性','女性','壁纸','首页','桌面','时尚','写真','小姐','甜美','美女','性感',
# '迷人','优雅','性感','明星','高清','可爱','歌手','演员','体育','帅哥','欧美','温柔',
# '韩国','巴西','德国','英国','美国','日本','澳大利亚','香港','法国','埃及','俄罗斯','台湾',
# '小鲜肉','清新','小清新','气质','魅力','女神','女生','名模','女星','图片','影视','帅气','大腕','球星',
# '电影','表演','大腕','篮球','艺人','模特','风情','组合','摩登','时装','人气','偶像','男神','宝贝',
# '车模','古装','最新','男星','韩星','经典','足球','运动员','足球宝贝','巨星','动作','少女','世界杯',
# '唯美','可人','娇俏','灵动','女孩','美丽','抽烟','个性','的','漂亮','韩剧','国家','男子','队员','球员'
# ]

# def listToString(s):  
#     # initialize an empty string 
#     str1 = ""  
#     # traverse in the string   
#     for ele in s:  
#         str1 += ele   
#     # return string   
#     return str1  

# def getName():
#     sql = "select urlSign,tags,category,url from tbl_content"
#     ret = getDB(sql, 'crawler_img')
#     urlSignLst=[]
#     tagsLst=[]
#     categoryLst=[]
#     urlLst=[]
#     for row in ret:
#       urlSignLst.append(row[0]) 
#       tagsLst.append(row[1]) 
#       categoryLst.append(row[2]) 
#       urlLst.append(row[3]) 
#     print(len(tagsLst))
#     return tagsLst,categoryLst

# def filterNameMethod():
#     tagsLst,categoryLst=getName()
#     filterNameLst=[]
#     for category in categoryLst:
#         namePinyinLst=[]
#         for word in FILTER_WORDS:
#             if word in category:
#                 category=category.replace(word,'')
#         filterName=str(category)
#         '''
#         delete [],(),{}
#         '''
#         filterName = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", filterName)
#         filterName=filterName.lower()
#         filterNameLst.append(filterName)
#     print("*********************")
#     filterNameLst=list(set(filterNameLst)) 
#     print(len(filterNameLst))
#     i=0
#     # for filterName in filterNameLst:
#     #     ''' 
#     #     transfor pinyin
#     #     '''
#     #     namePinyinLst=lazy_pinyin(filterName)
#     #     namePinyinStr=listToString(namePinyinLst)
#     #     writeName2DB(filterName,namePinyinStr)
#     #     print("***********\n")
#     #     print(f'{i}\n')
#     #     i=i+1



# if __name__ == "__main__":
#     filterNameMethod()