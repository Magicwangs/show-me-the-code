#python2.7
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 10:52:44 2016

@author: MagicWang
"""
import urllib2
import re
import requests as req

DBUG = 1

reBODY=re.compile(r'<body.*?>([\s\S]*?)<\/body>',re.I)

reCOMM = r'<!--.*?-->'

reTRIM = r'<{0}.*?>([\s\S]*?)<\/{0}>'
reTAG  = r'<[\s\S]*?>|[ \t\r\f\v]'  # 去除tag和空格、换列、

class HTML_Extractor:
    def __str__(self):
        return 'HTML_Extractor'
    
    __repr__=__str__
    
    def __init__(self,url='',blockSize=3,timeout=5,image=False, proxy=None):
        self.url = url
        self.blockSize = blockSize
        self.timeout = timeout
        self.saveImage = image
        self.rawPage = ""
        self.ctexts = []
        self.cblocks = []
        self.proxy = {"http":proxy, "https":proxy}
    # 获取原始页面    
    def getRawPage(self):
        try:
            r = req.get(self.url, proxies=self.proxy, timeout=self.timeout)
        except Exception as e:
            raise e
        # 根据调试的结果该笔按后面的编码方式
        if DBUG:
            print "PageCode is " + r.encoding
        #强制改变编码
#        r.encoding = "utf-8"
        # status_code：响应状态码404、200等
        # text：网页文本
        return r.status_code,r.text    
        
    def processTags(self):
        # 替换去除
        self.body = re.sub(reCOMM, "", self.body)#去除注释
        self.body = re.sub(reTRIM.format("script"), "", re.sub(reTRIM.format("style"),"",self.body))
        self.body = re.sub(reTAG, "", self.body)



if __name__=="__main__":
    myExtractor = HTML_Extractor(url="http://www.bbc.com/zhongwen/simp/world/2016/10/161010_analysis_us_election_pole", proxy="localhost:1080")
    status,pageText = myExtractor.getRawPage()
    
    
    
    
    