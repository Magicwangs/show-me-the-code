# -*- coding: utf-8 -*-
# python2.7
"""
Created on Thu Oct 27 10:37:33 2016

@author: MagicWang
"""
import re
import os
import requests

def checkDir(output_dir):
    try:
        if not os.path.exists(output_dir):  
            os.mkdir(output_dir)
    except:  
        print ("Failed to create directory:")  
        exit()
    print ("config OK!")

def getRawPage():
    try:
        r = requests.get('http://tieba.baidu.com/p/2166231880', timeout=5)
    except Exception as e:
        raise e
    return r.text
    
def downloadPic(imgUrl,filename):
    r = requests.get(imgUrl, stream=True) # here we need to set stream = True parameter  
    with open(filename, 'wb') as f:  
        for chunk in r.iter_content(chunk_size=1024):  
            if chunk: # filter out keep-alive new chunks  
                f.write(chunk)  
                f.flush()  

if __name__=="__main__":
    index = 0
    output_dir ="./picDir" #创建对应的文件夹
    checkDir(output_dir)
    content = getRawPage()
    URLs = re.findall(r'<img pic_type="0" class="BDE_Image" src="(.*?)"', content, re.I)
    for url in URLs:
        picName = output_dir + '/{0}.jpg'.format(index)
        downloadPic(url, picName)
        index += 1