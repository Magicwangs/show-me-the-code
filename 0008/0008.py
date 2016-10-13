#python2.7
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 10:52:44 2016

@author: MagicWang
"""

import re
import requests as req

DEBUG = 1

reBODY = re.compile(r'<body.*?>([\s\S]*?)<\/body>',re.I)
reIMG = re.compile(r'<img[\s\S]*?src=[\'|"]([\s\S]*?)[\'|"][\s\S]*?>')

reCOMM = r'<!--.*?-->'

reTRIM = r'<{0}.*?>([\s\S]*?)<\/{0}>'
reTAG  = r'<[\s\S]*?>|[ \t\r\f\v]'  # 去除tag和空格、\t横向制表符、\r回车、\f换页、\v纵向制表符

class HTML_Extractor:
    def __str__(self):
        return 'HTML_Extractor'
    
    __repr__=__str__
    
    def __init__(self,url='',blockSize=5,timeout=5,image=False, proxy=None):
        self.url = url
        self.blockSize = blockSize
        self.timeout = timeout
        self.saveImage = image #是否保存图片
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
        if DEBUG:
            print "PageCode is " + r.encoding
        #强制改变编码
#        r.encoding = "utf-8"
        # status_code：响应状态码404、200等
        # text：网页文本
        return r.status_code,r.text    
       
    # 去除标签注释等   
    def processTags(self):
        # 替换去除
        self.body = re.sub(reCOMM, "", self.body)#去除注释 作用不大注释可以在reTAG时去掉
        self.body = re.sub(reTRIM.format("script"), "", re.sub(reTRIM.format("style"),"",self.body))
        self.body = re.sub(reTRIM.format("noscript"),"",self.body)    
        self.body = re.sub(reTAG, "", self.body)
    
    def processBlocks(self):
        self.ctexts = self.body.split("\n")#最后有一个是空的因为最后一行也有换行符
        self.textLens = [len(text) for text in self.ctexts]
        if DEBUG:
            print "textLens is {0}".format(self.textLens)
        lines = len(self.ctexts)
        self.cblocks = [0]*(lines-self.blockSize-1)
        for i in range(self.blockSize):
            self.cblocks = list(map(lambda x,y: x+y,self.textLens[i:lines-self.blockSize-1+i],self.cblocks))
        maxTextLen = max(self.cblocks)
        if DEBUG:
            print "maxTextlen is {0}".format(maxTextLen)

        self.start = self.end = self.cblocks.index(maxTextLen)
        while self.start > 0 and self.cblocks[self.start] > min(self.textLens):
            self.start -= 1
        while self.end < lines-self.blockSize and self.cblocks[self.end] > min(self.textLens):
            self.end +=1
        return "".join(self.ctexts[self.start:self.end])
        
    # 保留图片不变图片地址外部加上{{}}
    def processImages(self):
        self.body = reIMG.sub(r'{{\1}}',self.body)
    
    def getContext(self):
        status,self.rawPage = self.getRawPage()
        self.body = re.findall(reBODY, self.rawPage)[0]
        if self.saveImage:
            self.processImages()
        self.processTags()
        return self.body,self.processBlocks()


if __name__=="__main__":
    #可以调节blocksize来达到自己效果，访问外网启用代理
    myExtractor = HTML_Extractor(url="http://www.bbc.com/zhongwen/simp/world/2016/10/161010_analysis_us_election_pole", blockSize=7, image=True, proxy="localhost:1080")
    status,pageText = myExtractor.getRawPage()
    Body,Context = myExtractor.getContext()
    #国内的网址,纯文字，效果比较好
    chinaExtractor = HTML_Extractor(url="http://tech.163.com/13/1230/10/9HB88VE600094NRG.html", blockSize=5, image=True)
    Bo,Con = chinaExtractor.getContext()
    