#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 1:42 PM
# @Author  : Slade
# @File    : 最大公共字符串长度.py

'''有两个字符串，你只可以进行删除操作，问你最少进行多少次操作可以使两个字符串相等'''

def getNumofCommonSubstr(str1, str2):
    lstr1 = len(str1)
    lstr2 = len(str2)

    # 需要预留首字母的计算位，record[1][1]=0+similarity(1,1)
    record = [[0] * (lstr2 + 1) for i in range(lstr1 + 1)]

    idx = 0
    maxNum = 0
    for i in range(lstr1):
        for j in range(lstr2):
            if str1[i] == str2[j]:
                record[i + 1][j + 1] = record[i][j] + 1
                if maxNum< record[i + 1][j + 1]:
                    maxNum=record[i + 1][j + 1]
                    idx = i
    return maxNum,str1[(idx-maxNum+1):(idx+1)]