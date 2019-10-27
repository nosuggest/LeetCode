#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 9:55 PM
# @Author  : Slade
# @File    : LeetCode111minimum-depth-of-binary-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        return left+1 if root.right is None else right +1 if root.left is None else min(left, right) + 1
