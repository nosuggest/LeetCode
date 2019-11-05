#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : 二分查找.py
@Author: sladesha
@Date  : 2019/9/2 22:37
@Desc  : 
'''


def binarySreach(data, element):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == element:
            return mid
        elif data[mid] > element:
            end = mid - 1
        else:
            start = mid + 1
    return -1


if __name__ == '__main__':
    print(binarySreach([1, 3, 5, 9, 10, 11, 13, 56], 911))
