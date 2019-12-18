#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 6:23 PM
# @Author  : Slade
# @File    : LeetCode974subarray-sums-divisible-by-k.py
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        tmp = [0] + A
        for i in range(len(A)):
            tmp[i + 1] = tmp[i] + A[i]
        hashmap = dict()
        for i in tmp:
            mod = i % K
            hashmap[mod] = hashmap.get(mod, 0) + 1
        ans = 0
        for k, v in hashmap.items():
            if v > 1:
                ans += v * (v - 1) / 2
        return ans
