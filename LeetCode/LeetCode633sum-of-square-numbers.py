#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/20 3:39 PM
# @Author  : Slade
# @File    : LeetCode633sum-of-square-numbers.py
import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(int(math.sqrt(c))+1):
            tmp = math.sqrt(c-i**2)
            if tmp==int(tmp):
                return True
        return False