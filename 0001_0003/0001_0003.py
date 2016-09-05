# -*- coding: utf-8 -*-
"""
Created on Sat Sep 03 18:51:27 2016

@author: MagicWang
"""

import random
import sqlite3
import redis

def codeGenerator(codeNum,codeLength):
    basicCode='abcdefghijklmnopgrstuvwxyzABCDEFGHIJKLMNOPGRSTUVWXYZ1234567890'
    retCode=[]
    for num in range(codeNum):
        randStr=''
        for i in range(codeLength):
            randIndex=random.randint(0,len(basicCode)-1)
            randStr=randStr+basicCode[randIndex]
        retCode.append(randStr)
    return retCode
    
def initSql():
    conn=sqlite3.connect('code.db')
    cursor=conn.cursor()
    cursor.execute("drop table if exists Code")
    cursor.execute('''create table Code(
                        id integer primary key not null,
                        code varchar(40)
                        );''')
    cursor.close()
    conn.commit()
    
def saveSql(Codelist):
    conn=sqlite3.connect('code.db')
    cursor=conn.cursor()
    for codeline in Codelist:
        #第一种方法传递有漏洞,绝对不要做
#        cursor.execute('select * from Code where code='%s';'%codeline)
        cursor.execute('select * from Code where code=:code;',{"code":codeline})
        #返回结果保存在cursor中        
        sameCode = cursor.fetchone()
        if sameCode is None:
            cursor.execute("insert into Code (code) values (?);",(codeline,))
        else:
            print 'sameCode:%s'%codeline
    cursor.close()
    conn.commit()

def saveRedis(Codelist):
    pool=redis.ConnectionPool(
            host='localhost',
            port=6379,
            db=0,
            password='magic'
            )
    r=redis.StrictRedis(connection_pool=pool)
    r.delete('money-off coupon')
    for codeline in Codelist:
#        r.lpush('money-off coupon',codeline)
        #从右边插入 rpushx 必须名字已经存在时才能进行
        r.rpush('money-off coupon',codeline) 
    r.save()
    return r.lrange('money-off coupon',0,-1)
    
if __name__=='__main__':
    Code=codeGenerator(200,7)
#    initSql()
#    saveSql(Code)
    a=saveRedis(Code)
    