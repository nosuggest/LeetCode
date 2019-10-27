#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 1:29 PM
# @Author  : Slade
# @File    : 插入排序.py

def sort(l):
    for i in range(1, len(l)):
        tmp = l[i]
        for j in range(i, -1, -1):

            # 循环挪动，因为i～0都是有序的
            if l[j - 1] > tmp:
                l[j] = l[j - 1]
            else:
                break
        # 这个值就是比tmp大的最小值
        l[j] = tmp
    return l


if __name__ == '__main__':
    print (sort([67, 70, 56]))
