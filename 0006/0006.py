# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 19:08:13 2016

@author: MagicWang
"""
from collections import Counter
from os import listdir
import re

def DiaryCount(diaryPath):
    importantWord=dict()
    #需要过滤词，应为存在 a the等词的干扰
    filter_word=['the', 'in', 'of', 'and', 'to', 'has', 'that', 's', 'is', 'are', 'a', 'with', 'as', 'an','it']
    filelist=listdir(diaryPath)
    for diary in filelist:
        if len(diary.split('.'))>1 and diary.split('.')[1]=="txt":
            with open(diaryPath+'/'+diary) as fr:
                content=fr.read()
                content=content.strip()
                wordlist=re.findall(r'\w+',content)
#                print wordlist
            c=Counter(wordlist)
            #去除过滤词
            for filword in filter_word:
#                c[filword]=0
                del c[filword]
            #选择最高频词为最重要的词
            diary_Word=c.most_common(1)
            importantWord[diary]=diary_Word[0][0]
    return importantWord
    
if __name__=="__main__":
    words=DiaryCount('Diary')