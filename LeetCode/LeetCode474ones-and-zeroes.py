#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 4:58 PM
# @Author  : Slade
# @File    : LeetCode474ones-and-zeroes.py

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(m + 1)] for i in range(n + 1)]
        for s in strs:
            count0 = s.count("0")
            count1 = len(s) - count0
            for i in range(n, -1, -1):
                for j in range(m, -1, -1):
                    if i >= count1 and j >= count0:
                        dp[i][j] = max(dp[i][j], dp[i - count1][j - count0] + 1)
        return dp[-1][-1]
