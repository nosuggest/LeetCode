#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : 消消乐.py.py
@Author: sladesha
@Date  : 2019/9/1 22:37
@Desc  : 
'''

from collections import defaultdict

def get_result(data):
    d = defaultdict(int)
    for i in data:
        d[i] += 1
    # 最多元素的出现的次数小于数组长度的一半即可
    if max(d.values()) > len(data) / 2:
        return False
    else:
        return True


if __name__ == '__main__':
    print (get_result([1, 22, 3, 4]))
