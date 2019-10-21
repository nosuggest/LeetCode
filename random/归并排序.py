#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 3:24 PM
# @Author  : Slade
# @File    : 归并排序.py

def mergeSort(data):
    if len(data) <= 1:
        return data

    mid = len(data) >> 1
    left, right = mergeSort(data[:mid]), mergeSort(data[mid:])
    return merge(left, right)


def merge(left, right):
    res = []
    while left and right:
        min_val = left.pop(0) if left[0] < right[0] else right.pop(0)
        res.append(min_val)

    res += left if left else right
    return res


if __name__ == '__main__':
    print(mergeSort([3, 2, 1, 0, 5, 8, 7, 2, -5, 9, 6, 11]))
