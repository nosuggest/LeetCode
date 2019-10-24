#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 8:45 PM
# @Author  : Slade
# @File    : LeetCode394decode-string.py

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = ""
        multi = ""
        for c in s:
            if '\u0030' <= str(c) <= '\u0039':
                multi += str(c)

            if ('\u0041' <= str(c) <= '\u005a') or ('\u0061' <= str(c) <= '\u007a'):
                res += str(c)
            if c == "[":
                stack.append([res, multi])
                res = ""
                multi = "   "
            if c == "]":
                r, m = stack.pop()

                res = r + res * int(m)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.decodeString("3[a]2[bc]"))
