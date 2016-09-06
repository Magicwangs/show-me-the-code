# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 16:34:18 2016

@author: MagicWang
"""
import re

def word_count(filename):
    words=list()
    with open(filename) as fr:
        #返回所有字符串
        for line in fr:
            line=line.strip()
            #找到所有单词字符 \w表示：匹配包括下划线在内的单词字符，[0-9a-zA-Z_]
            word=re.findall(r'\w+',line)
            words.extend(word)
    #返回根据小写排序的单词序列
    return sorted(words,key=str.lower)
    
if __name__=="__main__":
    English=word_count('words.txt')
    print "the word number is %d"%len(list(set(English)))