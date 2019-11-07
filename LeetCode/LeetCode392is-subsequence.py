#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 9:05 PM
# @Author  : Slade
# @File    : LeetCode392is-subsequence.py

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        length = len(s)
        idx = 0
        index = 0
        while index<len(t) and idx<length:
            if s[idx]==t[index]:
                idx+=1
            index+=1
        return idx==length