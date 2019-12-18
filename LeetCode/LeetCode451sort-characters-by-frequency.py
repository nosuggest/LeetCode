#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 5:39 PM
# @Author  : Slade
# @File    : LeetCode451sort-characters-by-frequency.py
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        hashmap = Counter(s)
        res = sorted(hashmap.items(),key=lambda x:x[1],reverse=True)
        ans = ""
        for k,v in res:
            ans+=k*v
        return ans