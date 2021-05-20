# # encoding=utf8 
# import MySQLdb
# import sys
# import time
# import json
# import imp

# wlcdb = {'user':'root', 'passwd':'123456', 'dhost':'localhost', 'dport':3306}
# rlcdb = {'user':'root', 'passwd':'123456', 'dhost':'localhost', 'dport':3306}

# def parse_sql(filename):
#     data = open(filename, 'r', encoding='UTF-8').readlines()
#     stmts = []
#     DELIMITER = ';'
#     stmt = ''

#     for lineno, line in enumerate(data):
#         if not line.strip():
#             continue

#         if line.startswith('--'):
#             continue

#         if 'DELIMITER' in line:
#             DELIMITER = line.split()[1]
#             continue

#         if (DELIMITER not in line):
#             stmt += line.replace(DELIMITER, ';')
#             continue

#         if stmt:
#             stmt += line
#             stmts.append(stmt.strip())
#             stmt = ''
#         else:
#             stmts.append(line.strip())
#     return stmts
    
# def build_insert_sql(conn, talbe_name, k_v):
#     names=[]
#     values=[]
#     for key in k_v.keys():
#         names.append(key)
#         value = k_v[key]
#         if isinstance(value, str):
#             # values.append("'%s'"% conn.escape_string(value))
#             values.append("'%s'"%value)
#             # values.append(str(value))
#         elif isinstance(value, int):
#             values.append("%d"%value)
#         else:
#             # values.append("%d"%value)
#             values.append("'%s'"%value)
#             # values.append(str(value))
#     return "insert ignore into %s (%s) values (%s);" % (talbe_name, ",".join(names), ",".join(values))

# def writeDB(talbe_name, k_v, dbase='crawler_img'):
#     try:
#         conn=MySQLdb.connect(charset='utf8', init_command='SET NAMES UTF8',host = wlcdb['dhost'], user = wlcdb['user'], passwd = wlcdb['passwd'], db = dbase, port = wlcdb['dport'])
#         executeSql = build_insert_sql(conn, talbe_name, k_v)
#         cur=conn.cursor()
#         cur.execute("SET NAMES utf8mb4")
#         try:
#             print ("*******insert***********")
#             cur.execute(executeSql)

#         except MySQLdb.Error as e:
#             print ("Mysql Error %d: %s" % (e.args[0], e.args[1]))
#         cur.close()
#         conn.commit()
#         conn.close()
#         print ("*******insert close***********")

#     except MySQLdb.Error as e:
#         print ("Mysql Error insertList",e)

# def getDB(executeSql, dbase):
#     try:
#         conn=MySQLdb.connect(host = rlcdb['dhost'], user = rlcdb['user'], passwd = rlcdb['passwd'], db = dbase, port = rlcdb['dport'])
#         print("****************")
#         # print(conn)
#         cur=conn.cursor()
#         cur.execute("SET NAMES utf8mb4")
#         try:
#             cur.execute(executeSql)
#             results=cur.fetchall()
#             return results
#         except MySQLdb.Error as e:
#             print ("Mysql Error %d: %s" % (e.args[0], e.args[1]))
#         cur.close()
#         conn.commit()
#         conn.close()
#     except MySQLdb.Error as e:
#         print (e)
#         print ("Mysql Error selectList")

# def doDB(executeSql, dbase='crawler_img'):
#     ret = 0
#     try:
#         conn=MySQLdb.connect(host = wlcdb['dhost'], user = wlcdb['user'], passwd = wlcdb['passwd'], db = dbase, port = wlcdb['dport'])
#         cur=conn.cursor()
#         try:
#             ret = cur.execute(executeSql)
#         except MySQLdb.Error as e:
#             print ("Mysql Error %d: %s" % (e.args[0], e.args[1]))
#         cur.close()
#         conn.commit()
#         conn.close()
#     except MySQLdb.Error as e:
#         print ("Mysql Error insertList")
#     return ret

# def checkDB(dbname):
#     try:
#         conn=MySQLdb.connect(host = wlcdb['dhost'], user = wlcdb['user'], passwd = wlcdb['passwd'],  port = wlcdb['dport'])
#         mycursor = conn.cursor()
#         mycursor.execute("SHOW DATABASES")
#         databases = mycursor.fetchall()
#         for db in databases:
#             if db[0]==dbname:
#                 print("****Find have crawler_img DataBase*****")
#                 return True
#         return False
#     except MySQLdb.Error as e:
#         print ("Mysql Error checkDB")
#         return False
# '''
# def writePicMany(talbe_name, picList, dbase='chuilei'):
#     rukuList = []
#     x = time.localtime(time.time())
#     nowTime = time.strftime('%Y-%m-%d %H:%M:%S',x)
#     try:
#         conn=MySQLdb.connect(host = lcdb['dhost'], user = lcdb['user'], passwd = lcdb['passwd'], db = dbase, port = lcdb['dport'])
#         sql = "insert into "+tbl+"(set_sign, pic_seq, objurl, from_url, pic_title, pic_desc, picture_id, width, height, content_sign1, content_sign2, create_time, update_time) values(%d, %d, %s, %s, %s, %s, %d, %d, %d, %d, %d, %s, %s)"
#         for picDic in picList:
#             picTuple = (picDic['set_sign'], picDic['pic_seq'], picDic['objurl'], picDic['from_url'], picDic['pic_title'], \
#                     picDic['pic_desc'],picDic['picture_id'],picDic['width'], picDic['height'],picDic['content_sign1'], \
#                     picDic['content_sign2'], nowTime, nowTime)
#             rukuList.append(picTuple)
#         cur=conn.cursor()
#         cur.execute("SET NAMES utf8mb4")
#         try:
#             cur.executemany(sql, rukuList)
#         except MySQLdb.Error,e:
#             print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#         cur.close()
#         conn.commit()
#         conn.close()
#     except MySQLdb.Error,e:
#         print "Mysql Error insertList"
# '''
# def initDatabase():
#     if checkDB(dbname='crawler_img3'):
#         print("Database is OK")
#     else:
#         print("Ready Go,Init Database")
#         try:
#             conn=MySQLdb.connect(charset='utf8', init_command='SET NAMES UTF8',host = wlcdb['dhost'], user = wlcdb['user'], passwd = wlcdb['passwd'], port = wlcdb['dport'])
#             cur=conn.cursor()
#             try:
#                 stmts = parse_sql('crawler_img_database.sql')
#                 for stmt in stmts:
#                     cur.execute(stmt)
#             except MySQLdb.Error as e:
#                 print ("Mysql Error %d: %s" % (e.args[0], e.args[1]))
#             cur.close()
#             conn.commit()
#             conn.close()
#             print("Init Database Done")
#         except MySQLdb.Error as e:
#             print ("Mysql Error insertList")

# if __name__ == "__main__":
#     initDatabase()