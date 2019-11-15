#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 8:42 PM
# @Author  : Slade
# @File    : LeetCode680valid-palindrome-ii.py

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def search(start, end, s, tmp):
            if start >= end or tmp > 1:
                return tmp
            if s[start] == s[end]:
                return search(start + 1, end - 1, s, tmp)
            else:
                return min(search(start + 1, end, s, tmp + 1), search(start, end - 1, s, tmp + 1))

        return True if search(0, len(s) - 1, s, 0) <= 1 else False
