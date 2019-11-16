#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode459repeated-substring-pattern.py
@Author: sladesha
@Date  : 2019/11/16 14:05
@Desc  : 
'''


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(set(s)) == 1:
            return True
        doubles = s+s
        return s in doubles[1:-1]
