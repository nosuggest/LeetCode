#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 11:26 AM
# @Author  : Slade
# @File    : LeetCode779K-thSymbolinGrammar.py

import functools
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        dt = {"0":"01","1":"10"}

        @functools.lru_cache(maxsize=128, typed=False)
        def f(n) :
            if n==0:
                return "0"
            res = []
            for item in f(n-1):
                res.append(dt[item])
            return ''.join(res)
        return f(N-1)[K-1]