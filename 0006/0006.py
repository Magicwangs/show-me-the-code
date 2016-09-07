# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 19:08:13 2016

@author: MagicWang
"""
from collections import Counter
from os import listdir
import re


def DiaryCount(diaryPath):
    importantWord=list()
    filelist=listdir(diaryPath)
    for diary in filelist:
        diarywords=list()
        if len(diary.split('.'))>1 and diary.split('.')[1]=="txt":
            with open(diaryPath+'/'+diary) as fr:
                for line in fr:
                    line.strip()
                    lineword=re.findall(r'\w+',line)
                    diarywords.extend(lineword)
            c=Counter(diarywords)
            diary_Word=c.most_common(1)
            importantWord.extend(diary_Word)
    return importantWord
    
if __name__=="__main__":
    words=DiaryCount('Diary')