#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 3:57 PM
# @Author  : Slade
# @File    : 堆排序.py


def heapify(arr, n, i):
    '''
    n是用来限制数组长度的，让最大堆只在一定范围内进行构造
    :param arr: 数组
    :param n:  数组长度
    :param i:   修正数组第i个结点为最大堆结点
    :return:
    '''
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # 每次拿倒数第k个元素最大堆的top值进行保存
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换

        '''将交换后堆堆重新变为最大堆'''
        heapify(arr, i, 0)
    return arr


if __name__ == '__main__':
    print(heapSort([3, 2, 1, 0, 5, 8, 7, 2, -5, 9, 6, 11]))
