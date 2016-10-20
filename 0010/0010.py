# python2.7
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:46:49 2016

@author: MagicWang
"""
import os
import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import string

# 汉字常用字unicode码表
CommenChinese =u'''
\u7684\u4e00\u4e86\u662f\u6211\u4e0d\u5728\u4eba\u4eec\u6709\u6765\u4ed6\u8fd9\u4e0a\u7740\u4e2a\u5730\u5230\u5927\u91cc\u8bf4\u5c31\u53bb\u5b50\u5f97
\u4e5f\u548c\u90a3\u8981\u4e0b\u770b\u5929\u65f6\u8fc7\u51fa\u5c0f\u4e48\u8d77\u4f60\u90fd\u628a\u597d\u8fd8\u591a\u6ca1\u4e3a\u53c8\u53ef\u5bb6\u5b66
\u53ea\u4ee5\u4e3b\u4f1a\u6837\u5e74\u60f3\u751f\u540c\u8001\u4e2d\u5341\u4ece\u81ea\u9762\u524d\u5934\u9053\u5b83\u540e\u7136\u8d70\u5f88\u50cf\u89c1
\u4e24\u7528\u5979\u56fd\u52a8\u8fdb\u6210\u56de\u4ec0\u8fb9\u4f5c\u5bf9\u5f00\u800c\u5df1\u4e9b\u73b0\u5c71\u6c11\u5019\u7ecf\u53d1\u5de5\u5411\u4e8b
\u547d\u7ed9\u957f\u6c34\u51e0\u4e49\u4e09\u58f0\u4e8e\u9ad8\u624b\u77e5\u7406\u773c\u5fd7\u70b9\u5fc3\u6218\u4e8c\u95ee\u4f46\u8eab\u65b9\u5b9e\u7ec6
\u5403\u505a\u53eb\u5f53\u4f4f\u542c\u9769\u6253\u5462\u771f\u5168\u624d\u56db\u5df2\u6240\u654c\u4e4b\u6700\u5149\u4ea7\u60c5\u8def\u5206\u603b\u6761
\u767d\u8bdd\u4e1c\u5e2d\u6b21\u4eb2\u5982\u88ab\u82b1\u53e3\u653e\u513f\u5e38\u6c14\u4e94\u7b2c\u4f7f\u5199\u519b\u5427\u6587\u8fd0\u518d\u679c\u80cc
\u600e\u5b9a\u8bb8\u5feb\u660e\u884c\u56e0\u522b\u98de\u5916\u6811\u7269\u6d3b\u90e8\u95e8\u65e0\u5f80\u8239\u671b\u65b0\u5e26\u961f\u5148\u529b\u6162
\u5b8c\u5374\u7ad9\u4ee3\u5458\u673a\u66f4\u4e5d\u60a8\u6bcf\u98ce\u7ea7\u8ddf\u7b11\u554a\u5b69\u4e07\u5c11\u76f4\u610f\u591c\u6bd4\u9636\u53f6\u538b
\u8fde\u8f66\u91cd\u4fbf\u6597\u9a6c\u54ea\u5316\u592a\u6307\u53d8\u793e\u4f3c\u58eb\u8005\u5e72\u77f3\u6ee1\u65e5\u51b3\u767e\u539f\u62ff\u7fa4\u5ffd
\u7a76\u5404\u516d\u672c\u601d\u89e3\u7acb\u6cb3\u6751\u516b\u96be\u65e9\u8bba\u5417\u6839\u5171\u8ba9\u76f8\u7814\u4eca\u5176\u4e66\u5750\u822c\u62a5
\u63a5\u5e94\u5173\u4fe1\u89c9\u6b65\u53cd\u5904\u8bb0\u5c06\u5343\u627e\u4e89\u9886\u6216\u5e08\u7ed3\u5757\u8dd1\u8c01\u8349\u8d8a\u5b57\u6797\u725b
\u52a0\u811a\u7d27\u7231\u7b49\u4e60\u9635\u6015\u6708\u9752\u534a\u706b\u6cd5\u9898\u5efa\u8d76\u4f4d\u5531\u6d77\u4e03\u5973\u4efb\u4ef6\u611f\u4f55
\u51c6\u5f20\u56e2\u5c4b\u79bb\u8272\u8138\u7247\u79d1\u5012\u775b\u5229\u4e16\u521a\u4e14\u7531\u9001\u5207\u661f\u5bfc\u665a\u8868\u591f\u6574\u975e
\u8ba4\u54cd\u96ea\u6d41\u672a\u573a\u8be5\u5e76\u5e95\u6df1\u523b\u5e73\u4f1f\u5fd9\u63d0\u786e\u8fd1\u4eae\u8f7b\u8bb2\u519c\u53e4\u9ed1\u533a\u8863
\u544a\u754c\u62c9\u540d\u5440\u571f\u6e05\u9633\u7167\u529e\u53f2\u6539\u5386\u8f6c\u753b\u9020\u5634\u6b64\u6cbb\u5317\u5fc5\u670d\u9876\u6025\u5cb8
\u96e8\u7a7f\u5185\u8bc6\u9a8c\u4f20\u4e1a\u83dc\u722c\u7761\u5174\u5f62\u91cf\u54b1\u89c2\u82e6\u4f53\u4f17\u901a\u51b2\u5408\u7834\u79cd\u88c5\u6389
\u53cb\u5ea6\u672f\u996d\u516c\u65c1\u623f\u6781\u5357\u67aa\u8bfb\u6c99\u5c81\u7ebf\u91ce\u575a\u7a7a\u6536\u7b97\u81f3\u653f\u57ce\u505c\u606f\u53e5
\u52b3\u843d\u94b1\u7279\u56f4\u5f1f\u80dc\u6559\u70ed\u5c55\u5305\u6b4c\u7c7b\u6e10\u5f3a\u6570\u4e61\u547c\u6027\u97f3\u7b54\u54e5\u6562\u53d6\u5165
\u9645\u65e7\u795e\u5ea7\u7ae0\u5e2e\u5566\u53d7\u7cfb\u4ee4\u8df3
'''


class CodePic:
    #__str__ 用于print，可读性高   输出print standard可见
    def __str__(self):
        return 'CodePicture Generator'
        
    __repr__ = __str__
    
    #__init__构造函数 codeNum：验证码数量 codeLength:验证码长度
    def __init__(self, codeNum=10, codeLength=4, codeDir='codePicDir',
                        bgSize=(100,50), bgColor=(255,255,255), fontSize=20, 
                        fontColor=(0,0,255), fontPath='./ttfLib/msyh.ttc', drawLine=True,
                        lineColor=(255,0,0), lineNum=(1,3)):
        self.codeNum = codeNum
        self.codeLength = codeLength
        self.codeDir = codeDir
        self.bgSize = bgSize
        self.bgColor = bgColor
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.fontPath = fontPath
        self.drawLine = drawLine
        self.lineColor = lineColor
        self.linNum = lineNum
        self.image = Image.new('RGB',self.bgSize,self.bgColor)
    
    def checkDir(self):
        try:
            if not os.path.exists(self.codeDir):
                os.mkdir(self.codeDir)
                print "Directory Created"
        except:
            print "Failed to create directory!"
            exit(0)
        print "File OK!"
    
    def codeGenerator(self):
#        basicCode = 'abcdefghijklmnopgrstuvwxyzABCDEFGHIJKLMNOPGRSTUVWXYZ1234567890'
        basicCode = list(string.letters)
        for index in range(0,10):
            basicCode.append(str(index))
        retCode=[]
        for num in range(self.codeNum):
            randStr=''.join(random.sample(basicCode,self.codeLength))
            retCode.append(randStr)
        return retCode
    
    def chineseCodeGen(self):
        retChineseCode=list()
        for num in range(self.codeNum):
            temp=str()
            for l in range(self.codeLength):
                # 所有汉字范围 u4E00-u9FA5 
                head = random.randint(0xE4,0xE9)
                body = random.randint(0xB8,0xBE)
                tail = random.randint(0x80,0xA5)
                val = (head << 16)|(body << 8)|tail
                hexStr = "{0:x}".format(val)
                temp = temp+hexStr.decode('hex').decode('UTF-8')#转化为unicode编码
            retChineseCode.append(temp)
        return retChineseCode
        
    def CommenChineseGen(self):
        #常用汉字列表 unicode
        Ucode_ChineseArray = CommenChinese.replace('\n','')
        retChineseCode=list()
        for num in range(self.codeNum):
            temp = str()
            for l in range(self.codeLength):
                index = random.randint(0,len(Ucode_ChineseArray)-1)
                temp = temp+Ucode_ChineseArray[index]
            retChineseCode.append(temp)
        return retChineseCode
    
    
    def pic_Line(self, draw):
        if self.drawLine:
            begin = (random.randint(0,self.bgSize[0]),random.randint(0,self.bgSize[1]))
            end = (random.randint(0,self.bgSize[0]),random.randint(0,self.bgSize[1]))
            draw.line([begin,end],fill=self.lineColor)
       
    def picGenerator(self):
        self.checkDir()
        self.codeArray = self.codeGenerator()#字母和数字构成验证码
        self.codeArray = self.chineseCodeGen()#所有中文构成验证码
        self.codeArray = self.CommenChineseGen()#常见汉字构成验证码
        for code in self.codeArray:
            self.image = Image.new('RGB',self.bgSize,self.bgColor)
            font = ImageFont.truetype(self.fontPath,self.fontSize)
            draw = ImageDraw.Draw(self.image)
            font_width,font_height = font.getsize(code)
            draw.text(((self.bgSize[0]-font_width)/self.codeLength,(self.bgSize[1]-font_height)/self.codeLength), 
                        code, font=font, fill=self.fontColor)
            randline = random.randint(self.linNum[0],self.linNum[1])
            for l in range(randline):
                self.pic_Line(draw)
            # 图形扭曲参数
            params = [1 - float(random.randint(1, 2)) / 100,
                      0,
                      0,
                      0,
                      1 - float(random.randint(1, 10)) / 100,
                      float(random.randint(1, 2)) / 500,
                      0.001,
                      float(random.randint(1, 2)) / 500
                      ]
            self.image = self.image.transform((self.bgSize[0],self.bgSize[1]), Image.PERSPECTIVE,
                                              params)
            self.image = self.image.filter(ImageFilter.EDGE_ENHANCE_MORE)
            self.image.save(self.codeDir+'/'+code+'.png')
    
if __name__=="__main__":
    myCode = CodePic()
    myCode.picGenerator()