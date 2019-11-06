#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 8:33 PM
# @Author  : Slade
# @File    : LeetCode60permutation-sequence.py
class Solution(object):
    def __init__(self):
        self.count = 0
        self.ans = 0

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        candidates = list(map(str, range(1, 1 + n)))
        self.dfs('', 0, k, candidates)
        return self.ans

    def fact(self, n):
        res = 1
        while n:
            res *= n
            n -= 1
        return res

    def dfs(self, tmp, time, k, candidates):
        if self.ans:
            return
        if not candidates:
            self.count += 1
            if self.count == k:
                self.ans = tmp
            return
        # 当迭代轮数超过一次完整循环的值的时候，直接跳过
        l = self.fact(len(candidates)-1)
        for index in range(len(candidates)):
            if l < k:
                k -= l
                continue
            self.dfs(tmp + candidates[index], time + 1, k, candidates[:index] + candidates[index + 1:])
