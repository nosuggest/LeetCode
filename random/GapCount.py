#!/usr/bin/env python
# -*- coding: utf-8 -*-
# interesting question:
# How can we get the max gap between the interfacing elements in an array? Show the fastest way as you can

import sys
class SortWay:
    def __init__(self):
        self.data = None
        self.minbum = None
        self.maxnum = None
    #桶排序
    def _sort(self,data):
        self.data = data
        self.maxnum = max(self.data)
        self.minbum = min(self.data)
        length = self.maxnum-self.minbum
        d = {}
        for i in range(self.minbum,self.maxnum+1):
            d[i] = 0
        for i in range(len(data)):
            d[data[i]] = 1 + d[data[i]]
        return d
    
    #统计间隔数目
    def _NanCount(self,data):
        dic = self._sort(data)
        num = 0
        NCount = 0
        for i in dic.keys():
            if dic[i]==0:
                NCount = NCount + 1
            else:
                if NCount > num:
                    num = NCount
                NCount = 0
        return num+1


if __name__ == '__main__':
    data = [1,2,3,7,10]
    res = SortWay()._NanCount(data)
    print(res)
