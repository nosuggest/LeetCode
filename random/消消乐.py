#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : 消消乐.py.py
@Author: sladesha
@Date  : 2019/9/1 22:37
@Desc  : 
'''

from collections import defaultdict


class mydict(defaultdict):
    def max_value(self):
        maxValue = None
        for key in self:
            if not maxValue or self[key] > maxValue:
                maxValue = self[key]
        return maxValue


def get_result(data):
    d = mydict(int)
    for i in data:
        d[i] += 1
    # 最多元素的出现的次数小于数组长度的一半即可
    if d.max_value() > len(data) / 2:
        return False
    else:
        return True


if __name__ == '__main__':
    print (get_result([1, 22, 3, 4]))
