#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode115distinct-subsequences.py
@Author: sladesha
@Date  : 2019/11/17 15:21
@Desc  : 
'''


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sLength = len(s) + 1
        tLength = len(t) + 1
        dp = [[0 for _ in range(sLength)] for _ in range(tLength)]
        # 作为首列、首行我们认为为空串，作为初始化
        # s中能够满足空串的只有我们假设的，所以dp[0][j]必然为1
        for j in range(sLength):
            dp[0][j] = 1

        for i in range(1, tLength):
            for j in range(1, sLength):
                if t[i - 1] != s[j - 1]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().numDistinct("babgbag", "bag"))
