#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode516longest-palindromic-subsequence.py
@Author: sladesha
@Date  : 2019/11/16 9:00
@Desc  : 
'''


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dp = [[0 for i in range(length)] for i in range(length)]

        for i in range(length - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][length - 1]


# 最长回文子串
# class Solution(object):
#     def __init__(self):
#         self.res = 0
#
#     def longestPalindromeSubseq(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#
#         def search(s, left, right):
#             res = 0
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 res = max(res, right - left + 1)
#                 left -= 1
#                 right += 1
#             return res
#
#         for idx in range(len(s)):
#             self.res = max(self.res, max(search(s, idx, idx), search(s, idx, idx + 1)))
#
#         return self.res
#

if __name__ == '__main__':
    print(Solution().longestPalindromeSubseq("bbbbacbbbbb"))
