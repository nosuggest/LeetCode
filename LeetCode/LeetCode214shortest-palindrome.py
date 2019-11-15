#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 11:12 AM
# @Author  : Slade
# @File    : LeetCode214shortest-palindrome.py

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        while s[:n][::-1] != s[:n]:
            n -= 1
        return s[n:][::-1] + s

    def shortestPalindrome1(self, s: str) -> str:
        length = len(s)
        start = 0
        # 从左侧开始的可能的最长回文子串
        for end in range(length - 1, -1, -1):
            if s[end] == s[start]:
                start += 1
        if start == length:
            return s
        # 不等的地方开始再递归处理
        suffix = s[start:]
        return suffix[::-1] + self.shortestPalindrome1(s[:start]) + suffix


if __name__ == '__main__':
    print(Solution().shortestPalindrome1("abc"))
