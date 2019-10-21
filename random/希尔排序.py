#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 2:41 PM
# @Author  : Slade
# @File    : 希尔排序.py

def shellSort(nlist):
    gap = int(len(nlist) >> 1)

    while gap > 0:
        # 从gap开始，遍历到数组结束的地方
        for j in range(gap, len(nlist)):
            temp = nlist[j]

            # 当观察值在gap右侧且左比右要大才需要进行交换计算
            while j >= gap and temp < nlist[j - gap]:
                nlist[j] = nlist[j - gap]
                j -= gap
            nlist[j] = temp
        gap >>= 1
    return nlist


if __name__ == '__main__':
    print(shellSort([12, 34, 54, 2, 3, 1, 2, 3, 4, 6, 10,99,23,4,54,64,757,68,5,865,68,68,9]))
