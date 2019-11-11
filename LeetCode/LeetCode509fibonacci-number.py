#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 7:56 PM
# @Author  : Slade
# @File    : LeetCode509fibonacci-number.py
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0] * (N + 1)
        if N in [0, 1]:
            return N

        dp[0] = 0
        dp[1] = 1
        for i in range(2, N + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[-1]