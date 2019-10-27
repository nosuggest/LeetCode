#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/5 11:00 AM
# @Author  : Slade
# @File    : test1.py
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1:
            return s

        maxLen = 0
        ans = ''

        def find(s, i, j):
            while j < len(s) and i >= 0 and s[i] == s[j] :
                i -= 1
                j += 1

            return s[i + 1: j], len(s[i + 1:j])

        for i in range(len(s) - 1):
            ansEven, maxEven = find(s, i, i)
            print(ansEven)
            print(maxEven)
            ansOdd, maxOdd = find(s, i, i + 1)
            if maxEven > maxOdd:
                maxTmp = maxEven
                ansTmp = ansEven
            else:
                maxTmp = maxOdd
                ansTmp = ansOdd

            if maxTmp > maxLen:
                ans = ansTmp
                maxLen = maxTmp
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("a"))
