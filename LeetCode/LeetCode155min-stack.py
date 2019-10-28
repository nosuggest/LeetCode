#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 2:45 PM
# @Author  : Slade
# @File    : LeetCode155min-stack.py
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.tmp = []
        self.helper = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.tmp.append(x)
        if len(self.helper) == 0 or x < self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self):
        """
        :rtype: None
        """
        self.tmp = self.tmp[:-1]
        self.helper = self.helper[:-1]

    def top(self):
        """
        :rtype: int
        """
        if self.tmp:
            return self.tmp[-1]
        else:
            return -1

    def getMin(self):
        """
        :rtype: int
        """
        if self.helper:
            return self.helper[-1]
        else:
            return -1

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
