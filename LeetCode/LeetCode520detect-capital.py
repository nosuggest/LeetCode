#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 2:24 PM
# @Author  : Slade
# @File    : LeetCode520detect-capital.py.py
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cnt = 0
        for c in word:
            if ord(c) - ord("a") < 0:
                cnt += 1
        if cnt == 0:
            return True
        elif cnt == len(word):
            return True
        elif cnt == 1 and ord(word[0]) - ord("a") < 0:
            return True

        return False
