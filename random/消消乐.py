#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : 消消乐.py.py
@Author: sladesha
@Date  : 2019/9/1 22:37
@Desc  : 
'''

'''
有n个数字，每次可以选择任意两个不同的数字，并同时删除它们，请问最后是否可以删完

```
两个坑：
1.汇总每个数字出现的次数的时候，不要用.count()，会超时；遍历hashmap
2.汇总后的数组中的每个数字是可拆的，并不是把一个数组切分成n个和相等的子数组，只需要max_value<=sum/2即可
```
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
