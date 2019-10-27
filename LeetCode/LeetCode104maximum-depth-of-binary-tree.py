#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/7 10:38 PM
# @Author  : Slade
# @File    : LeetCode104maximum-depth-of-binary-tree.py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left,right = self.maxDepth(root.left),self.maxDepth(root.right)
        return max(left,right)+1