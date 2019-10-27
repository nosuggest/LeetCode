#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 1:24 PM
# @Author  : Slade
# @File    : LeetCode814binary-tree-pruning.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.val == 0 and not root.left and not root.right:
            return None
        return root
