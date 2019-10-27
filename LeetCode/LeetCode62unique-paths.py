#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode62unique-paths.py
@Author: sladesha
@Date  : 2019/10/24 0:15
@Desc  : 
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp =[[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            dp[0][i]=1
        for j in range(m):
            dp[j][0]=1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[-1][-1]