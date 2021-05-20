from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from pathlib import Path

# 创建对象的基类:
Base = declarative_base()

class EnglishName(Base):
    # table name:
    __tablename__ = 'english_name'
    # table struct:
    id = Column(Integer, primary_key=True)
    ename = Column(String(32) )
    cname = Column(String(32))
    pronunciation = Column(String(32))
    cname_ext = Column(String(32))
    gender = Column(String(32))
    origin = Column(String(32))
    moral = Column(String(32))
    meaning = Column(String(32))
    impression = Column(String(32))
    similar = Column(String(32))
    created_at = Column(String(32))
    def __repr__(self):
        return self.cname

class TblContent(Base):
    # table name:
    __tablename__ = 'tbl_content'
    # table struct:
    urlSign=Column(String(32))
    title=Column(String(32))
    text=Column(String(64))
    images=Column(String(32))
    tags=Column(String(32))
    url=Column(String(64))
    isAlbum=Column(Integer)
    picUrl=Column(String(64))
    mypos=Column(String(32))
    sourceUrl=Column(String(64))
    status=Column(Integer)
    category=Column(String(32))
    domain=Column(String(32))
    publishTime=Column(String(32))
    crawlTime=Column(String(32))
    id= Column(Integer, primary_key=True)

    def __repr__(self):
        return self.urlSign

class TblName(Base):
    # table name:
    __tablename__ = 'tbl_name'
    # table struct:
    id= Column(Integer, primary_key=True)
    category=Column(String(32))
    title=Column(String(32))
    sourceCat=Column(String(32))
    crawlTime=Column(String(32))
    
    def __repr__(self):
        return self.sourceCat

def addEnglishName(session,id,ename, cname, pronunciation, cname_ext, 
        gender, origin, moral, meaning, impression, similar, created_at):
    if getEnglishName(session,id=id) is None:
        # 创建User对象
        u = EnglishName(id=id, ename=ename, cname=cname, pronunciation=pronunciation, cname_ext=cname_ext, 
            gender=gender, origin=origin, moral=moral, meaning=meaning, impression=impression, similar=similar, created_at=created_at)
        # 添加到session
        session.add(u)
        # 提交并保存到数据库:
        session.commit()
    else:
        print('user%d已经存在！' % id)

def getEnglishName(session,id=None,ename=None, cname=None, pronunciation=None, cname_ext=None,
        gender=None, origin=None, moral=None, meaning=None, impression=None, similar=None, created_at=None):
    # 查找User对象
    if id is not None:
        u = session.query(EnglishName).filter_by(id=id).first()
    elif ename is not None:
        u = session.query(EnglishName).filter_by(ename=ename).first()
    else:
        u = session.query(EnglishName)
    return u

def addContent(session,id,ename, cname, pronunciation, cname_ext, 
        gender, origin, moral, meaning, impression, similar, created_at):
    session.close()

def getContent(session,id=None,ename=None, cname=None, pronunciation=None, cname_ext=None,
        gender=None, origin=None, moral=None, meaning=None, impression=None, similar=None, created_at=None):
    # 查找User对象
    if id is not None:
        u = session.query(TblContent).filter_by(id=id).first()
    else:
        u = session.query(TblContent)
    return u
def getContentCategory(session):
    u = session.query(TblContent)
    return u

def buildInsertSQL(conn,talbe_name, k_v):
    names=[]
    values=[]
    for key in k_v.keys():
        names.append(key)
        value = k_v[key]
        if isinstance(value, str):
            values.append("'%s'"%value)
            # values.append(str(value))
        elif isinstance(value, int):
            values.append("%d"%value)
        else:
            # values.append("%d"%value)
            values.append("'%s'"%value)
            # values.append(str(value))
    return "insert into %s (%s) values (%s);" % (talbe_name, ",".join(names), ",".join(values))

def initDb():
    # 1、建立数据库连接:
    db_path = 'CrawlerImg.db'
    engine = create_engine('sqlite:///' + db_path, echo=True)
    
    # Base.metadata.drop_all(engine)
    # 2、创建表
    # Base.metadata.create_all(engine)

    # 3、创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 4、创建session对象:
    session = DBSession()
    return session

def initDb2(databaseName='CrawlerImg.db'):
    # 1、建立数据库连接:
    path = os.path.dirname(os.path.abspath(__file__))
    db_path = path+'\\'+databaseName 
    engine = create_engine('sqlite:///' + db_path, echo=False)
    conn=engine.connect()
    return conn

if __name__ == "__main__":
    initDb()