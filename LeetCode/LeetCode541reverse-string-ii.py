#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 4:47 PM
# @Author  : Slade
# @File    : LeetCode541reverse-string-ii.py

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverseSingle(s, k):
            if len(s) >= k:
                return s[:k][::-1] + s[k:]
            else:
                return s[:k][::-1]

        return reverseSingle(s[:2 * k], k) + self.reverseStr(s[2 * k:], k) if s[2 * k:] else reverseSingle(s[:2 * k],
                                                                                                           k) + ""




if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr("abcdefg", 8))
