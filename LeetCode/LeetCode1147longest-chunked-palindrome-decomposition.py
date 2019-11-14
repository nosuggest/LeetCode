#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 9:30 PM
# @Author  : Slade
# @File    : LeetCode1147longest-chunked-palindrome-decomposition.py

class Solution(object):
    def __init__(self):
        self.ans = 0

    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """

        def search(left, right, s):
            if len(s) == 0:
                return self.ans
            if s[:left] == s[-right:]:
                self.ans += 2 if len(s) != left else 1
                return search(1, 1, s[left:-right])
            else:
                return search(left + 1, right + 1, s)

        return search(1, 1, text)


if __name__ == '__main__':
    print(Solution().longestDecomposition("elvtoelvto"))
