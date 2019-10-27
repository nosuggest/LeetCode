#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 3:19 PM
# @Author  : Slade
# @File    : LeetCode461hamming-distance.py
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y)[2:].count("1")