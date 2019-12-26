#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 9:33 PM
# @Author  : Slade
# @File    : LeetCode670maximum-swap.py
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        origin = list(map(int, list(str(num))))
        l = sorted(map(int, list(str(num))), reverse=True)
        length = len(origin)
        idx = 0
        rep = -1
        while idx < length:
            if l[idx] == origin[idx]:
                idx += 1
            else:
                rep = l[idx]
                break
        if rep != -1:
            idx1 = length - origin[::-1].index(rep) - 1
            origin[idx], origin[idx1] = origin[idx1], origin[idx]
        return int("".join(map(str, origin)))

