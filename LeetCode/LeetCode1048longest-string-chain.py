#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 10:02 AM
# @Author  : Slade
# @File    : LeetCode1048longest-string-chain.py
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words, key=lambda x: len(x))
        res = dict()
        for word in words:
            for i in range(len(word)):
                res[word] = max(res.get(word, 1), res.get(word[:i] + word[i + 1:], 0) + 1)
        return max(res.values())


