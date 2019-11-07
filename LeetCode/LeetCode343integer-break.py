#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 9:21 AM
# @Author  : Slade
# @File    : LeetCode343integer-break.py

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]*(n+1)
        for i in range(3,n+1):
            j = (i>>1)+1
            for k in range(1,j):
                dp[i] = max(dp[i],(i-k)*k,dp[k]*dp[i-k],(i-k)*dp[k],k*dp[i-k])
        return dp[-1]