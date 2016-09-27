# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:09:51 2016

@author: MagicWang
"""
from os import listdir
import re

def statistics(dir_path):
    line_count=0
    block_count=0
    comment_count=0
    mul_comment_flag=1
    file_list=listdir(dir_path)
    #只取python的文件
    file_list=[item for item in file_list if item.endswith('.py')]
    for file_name in file_list:
        filename=dir_path+'\\'+file_name
        with open(filename,'rb') as fr:
            #readlines只能遍历小文件，大文件建议用下面的方法，逐行读取
            for line in fr:
                line=line.strip()
                if line=='':
                    if mul_comment_flag:
                        block_count=block_count+1
                    else:
                        comment_count=comment_count+1
                else:
                    if re.findall(r'(^```)|(^""")',line)!=[]:
                        mul_comment_flag=mul_comment_flag+1
                        mul_comment_flag=mul_comment_flag%2
                        comment_count=comment_count+1
                    else:
                        if mul_comment_flag:
                            if re.findall(r'^#',line)!=[]:
                                comment_count=comment_count+1
                            else:
                                line_count=line_count+1
                        else:
                            comment_count=comment_count+1
    return line_count,block_count,comment_count
    
if __name__=="__main__":
    line_count,block_count,comment_count=statistics('codedir')