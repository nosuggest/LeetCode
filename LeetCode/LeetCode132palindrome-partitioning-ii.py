#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 9:10 AM
# @Author  : Slade
# @File    : LeetCode132palindrome-partitioning-ii.py

'''
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
'''

import functools


class Solution(object):
    @functools.lru_cache(None)
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return 0

        ans = float("inf")
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1]:
                ans = min(self.minCut(s[i:]) + 1, ans)
        return ans

    def minCut1(self, s):
        minl = list(range(len(s)))
        n = len(s)
        # i-j之间是否需要切分
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            # +1为了修正dp[i][i]为True
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if j == 0:
                        minl[i] = 0
                    else:
                        # [j,i]已经保证是回文了
                        minl[i] = min(minl[i], minl[j - 1] + 1)
        print(dp)
        return minl[-1]


if __name__ == '__main__':
    print(Solution().minCut1("leet"))
