#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 9:43 PM
# @Author  : Slade
# @File    : LeetCode150evaluate-reverse-polish-notation.py

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        nums = []

        def func(token, v1, v2):
            if token == "+":
                return v1 + v2
            elif token == "/":
                return int(v1 / float(v2))
            elif token == "-":
                return v1 - v2
            else:
                return v1 * v2

        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                nums.append(eval(token))
            else:
                v2 = nums.pop()
                v1 = nums.pop()
                nums.append(func(token, v1, v2))
        return nums[0]