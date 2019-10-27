#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/29 10:41 PM
# @Author  : Slade
# @File    : LeetCode647palindromic-substrings.py
class Solution1(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dp = [1] * length

        def check(s):
            halfLength = len(s) // 2 + 1
            if s[:halfLength] == s[::-1][:halfLength]:
                return 1
            else:
                return 0

        for i in range(length):
            for j in range(i):
                if check(s[j:i + 1]):
                    dp[i] += 1
        return sum(dp)


class Solution2(object):
    cnt = 0

    def countSubstrings(self, s):
        s_index = 0
        for _ in s:
            self.search(s_index, s_index, s)
            self.search(s_index, s_index + 1, s)
            s_index += 1
        return self.cnt

    def search(self, start, end, s):
        while (start >= 0 and end < len(s)) and s[start] == s[end]:
            start -= 1
            end += 1
            self.cnt += 1
