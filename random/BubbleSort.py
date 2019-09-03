#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : BubbleSort.py
@Author: sladesha
@Date  : 2019/9/2 22:21
@Desc  : 
'''


def BubbleSort(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(0, i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


if __name__ == '__main__':
    print(BubbleSort([3, 7, 7, 111, 1, 2, 4]))
