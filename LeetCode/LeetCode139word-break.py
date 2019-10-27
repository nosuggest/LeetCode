#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 3:30 PM
# @Author  : Slade
# @File    : LeetCode139word-break.py

# 疯狂超时
# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#
#         def find(s, wordDict):
#             if len(s) == 0:
#                 return True
#
#             for i in range(len(s) + 1):
#                 if s[:i] in wordDict:
#                     if find(s[i:], wordDict):
#                         return True
#                 continue
#             return False
#
#         return find(s, wordDict)

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s) + 1):
            for j in range(i, len(s) + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True

        print(dp)
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print (solution.wordBreak(s, wordDict))
