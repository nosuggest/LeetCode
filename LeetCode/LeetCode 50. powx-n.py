#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 3:31 PM
# @Author  : Slade
# @File    : LeetCode 50. powx-n.py

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 简单的递归
        def help(x,n):
            if n == 0:
                return 1
            if not n&1:
                return help(x*x,n>>1)
            if n&1:
                return help(x*x,n>>1)*x
        if n>0:
            return help(x,n)
        elif n==0:
            return 1
        else:
            n = abs(n)
            return 1/(help(x,n))