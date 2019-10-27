#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 12:01 PM
# @Author  : Slade
# @File    : LeetCode222count-complete-tree-nodes.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left+right+1