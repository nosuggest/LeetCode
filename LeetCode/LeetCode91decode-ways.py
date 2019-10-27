#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode91decode-ways.py.py
@Author: sladesha
@Date  : 2019/8/20 22:10
@Desc  :
'''

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not len(s):
            return 0
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * len(s)

        dp[0] = 1

        for i in range(1, len(s)):
            if s[i] != "0":
                dp[i] = dp[i - 1]
            if s[i - 1] != "0" and int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2] if i>1 else 1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print (s.numDecodings("27"))
