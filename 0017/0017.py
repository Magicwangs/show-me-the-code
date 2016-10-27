# -*- coding: utf-8 -*-
# python2.7

"""
Created on Thu Oct 27 20:31:11 2016

@author: MagicWang
"""
import json
import xlrd
from lxml import etree

def getConentOfExcel(xlsName):
    xls = xlrd.open_workbook(xlsName)
    sheet = xls.sheet_by_name('Student')
    retDict = dict()
    for i in range(sheet.nrows):
        line = list()
        for j in range(1,sheet.ncols):
            value = sheet.cell_value(i,j)
            try:
                value = int(value)
            except UnicodeEncodeError:
                pass #此时出错时因为值为中文，仅将float转化为int
            line.append(value)
        retDict[sheet.cell_value(i,0)] = line
    return retDict

def ToXML(xmlName, data):
    root = etree.Element('root')
    student = etree.SubElement(root, 'students')
    student.append(etree.Comment(u"""学生信息表\n"id" : [名字, 数学, 语文, 英文]\n"""))
    student.text = data
    tree = etree.ElementTree(root)
    tree.write(xmlName, pretty_print=True, xml_declaration=True, encoding='utf-8')

if __name__=="__main__":
    contentDict = getConentOfExcel('student.xls')
    dataStr = unicode(json.dumps(contentDict).decode('utf-8'))
    ToXML('student.xml', dataStr)
