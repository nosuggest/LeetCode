#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 7:43 PM
# @Author  : Slade
# @File    : LeetCode961n-repeated-element-in-size-2n-array.py
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        hashmap = dict()
        length = len(A)
        for i in A:
            hashmap[i] = hashmap.get(i, 0) + 1
            if hashmap[i] == (length >> 1):
                break
        return i
