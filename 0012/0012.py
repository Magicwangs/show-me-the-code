# -*- coding: utf-8 -*-
# python 2.7
"""
Created on Thu Oct 27 10:23:23 2016

@author: MagicWang
"""

def getFilterWord(Filter_Dir):
    with open(Filter_Dir,'rb') as fr:
        filterWord = list()
        for line in fr:
            filterWord.append(line.strip())
    return filterWord
    
if __name__ == "__main__":
    flag = True
    filterWord = getFilterWord('filtered_words.txt')
    # 直接输入中文,但测试中有出现没有获取输入的问题
    inputWord = raw_input("Please input your word:")
    # 通过input输入需要加引号
#    inputWord = input("Please input your word:")
    for word in filterWord:    
        if inputWord.find(word)>-1:
            inputWord = inputWord.replace(word,'**')
            
    print inputWord
            