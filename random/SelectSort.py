#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : SelectSort.py
@Author: sladesha
@Date  : 2019/9/2 22:30
@Desc  : 
'''


def SelectSort(data):
    for i in range(0, len(data) - 1):
        minindex = i
        for j in range(i, len(data)):
            if data[minindex] > data[j]:
                minindex = j
        if minindex != i:
            data[minindex], data[i] = data[i], data[minindex]
    return data


if __name__ == '__main__':
    print(SelectSort([3, 7, 7, 111, 1, 2, 4]))
