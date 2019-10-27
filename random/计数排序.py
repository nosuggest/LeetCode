#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 10:26 AM
# @Author  : Slade
# @File    : 计数排序.py

def sort(nlist):
    result = [None] * len(nlist)
    for i in range(len(a)):
        p, q = 0, 0
        for j in range(len(a)):
            if a[j] < a[i]:
                p += 1
            elif a[i] == a[j]:
                q += 1

        for k in range(p, p + q):
            result[k] = a[i]
    return result
