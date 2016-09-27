# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:09:51 2016

@author: MagicWang
"""
from os import listdir
import re

def statistics(dir_name):
    codeline=list()
    line_count=0
    block_count=0
    comment_count=0
    file_list=listdir(dir_name)
    for file_name in file_list:
        filename=dir_name+'\\'+file_name
        with open(filename,'rb') as fr:
            #readlines只能遍历小文件，大文件建议用下面的方法
            for line in fr:
                line_count=line_count+1
    return line_count,block_count,comment_count
    
if __name__=="__main__":
    line_count,block_count,comment_count=statistics('codedir')