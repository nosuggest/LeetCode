#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode1234replace-the-substring-for-balanced-string.py
@Author: sladesha
@Date  : 2019/11/17 12:58
@Desc  : 
'''


class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        times = len(s) / 4
        from collections import Counter
        sdict = Counter(s)
        tmp = {}
        for k, v in sdict.items():
            if v > times:
                tmp[k] = v - times
        if not tmp:
            return 0
        left = 0
        right = 0
        lookup = {}
        ret = float("inf")
        while right < len(s):
            lookup[s[right]] = lookup.get(s[right], 0) + 1
            while all([lookup.get(k) >= v for k, v in tmp.items()]):
                ret = min(ret, right - left + 1)
                lookup[s[left]] -= 1
                left += 1
            right += 1
        return ret


if __name__ == '__main__':
    print(Solution().balancedString("QWER"))
