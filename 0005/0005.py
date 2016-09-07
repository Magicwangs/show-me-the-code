# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 20:43:03 2016

@author: MagicWang
"""
from os import listdir
import os
from cv2 import *

def changeSize(file_name):
    iPhone5_WIDTH = float(1136)
    iPhone5_HEIGHT = float(640)
    file_list=listdir(file_name)
    #切换到图片所在目录  尽量不要切换
#    os.chdir(file_name)
    output_dir ="./output" #创建对应的文件夹
    try:
        if not os.path.exists(output_dir):  
            os.mkdir(output_dir)
    except:  
        print ("Failed to create directory:")  
        exit()
    print ("config OK!")
    
    for pic in file_list:
        if len(pic.split('.'))>1 and pic.split('.')[1]=="jpg":
#            print pic
            img=imread(file_name+'/'+pic,1)
            #可能由于图片的压缩格式问题，出现读取故障，不是图片大小的问题，已测试 6M也可读取
            if img is None:
                print 'Pic Bug: %s'%pic
            else:
                rate=max(img.shape[0]/iPhone5_WIDTH if img.shape[0]>iPhone5_WIDTH else 1,
                         img.shape[1]/iPhone5_HEIGHT if img.shape[1]>iPhone5_HEIGHT else 1)
                rate=rate[0][0]
                res=resize(img,None,fx=1/rate,fy=1/rate,interpolation = INTER_CUBIC)
                imwrite(output_dir+'/'+pic,res)
#                print res.shape
        else:
            break
        
if __name__=="__main__":
    changeSize('HuabanBeauty')