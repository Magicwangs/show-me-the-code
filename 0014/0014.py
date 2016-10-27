# -*- coding: utf-8 -*-
# python2.7
"""
Created on Thu Oct 27 19:06:42 2016

@author: MagicWang
"""
import xlwt
import json

def getFileContent(fileName):
    with open(fileName,'rb') as fr:
        content = json.load(fr,encoding='UTF-8')
    return content

if __name__=="__main__":
    workBook = xlwt.Workbook()
    workSheet = workBook.add_sheet('Student')
    contentDict = getFileContent('student.txt')
    indexKey = sorted(contentDict.keys())
    for i in range(len(indexKey)):
        raw = i
        col = 0
        workSheet.write(raw, col, indexKey[i])
        dataList = contentDict[indexKey[i]]
        for j in range(len(dataList)):
            col = j+1
            workSheet.write(raw, col, dataList[j])
    workBook.save('student.xls')