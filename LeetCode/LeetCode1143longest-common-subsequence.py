#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode1143longest-common-subsequence.py
@Author: sladesha
@Date  : 2019/11/18 22:15
@Desc  : 
'''

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        t = len(text1)+1
        s = len(text2)+1
        dp = [[0 for i in range(t)] for j in range(s)]

        for i in range(1,s):
            for j in range(1,t):
                if text1[j-1]==text2[i-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
