#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 10:44 PM
# @Author  : Slade
# @File    : LeetCode559maximum-depth-of-n-ary-tree.py

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        candidates = [self.maxDepth(item) for item in root.children] if root.children else [0]
        return max(candidates)+1