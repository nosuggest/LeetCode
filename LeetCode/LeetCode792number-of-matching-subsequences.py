#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode792number-of-matching-subsequences.py
@Author: sladesha
@Date  : 2019/11/19 0:03
@Desc  : 
'''


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        def is_sub(S, sub):
            idx0 = 0
            idx1 = 0
            length0 = len(S)
            length1 = len(sub)
            while idx0 < length0 and idx1 < length1:
                if S[idx0] == sub[idx1]:
                    idx1 += 1
                idx0 += 1
            return idx1 == length1

        cnt = 0
        from collections import Counter
        hashmap = Counter(words)
        for word, value in hashmap.items():
            if is_sub(S, word):
                cnt += value
        return cnt
