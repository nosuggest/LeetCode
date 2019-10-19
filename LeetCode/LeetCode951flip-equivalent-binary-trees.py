#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 9:18 PM
# @Author  : Slade
# @File    : LeetCode951flip-equivalent-binary-trees.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is None and root2 is None:
            return True
        if root1 is None:
            return False
        if root2 is None:
            return False

        return root1.val == root2.val and (
            self.flipEquiv(root1.left, root2.right) or self.flipEquiv(root1.left, root2.left)) and (
               self.flipEquiv(root1.right, root2.right) or self.flipEquiv(root1.right, root2.left))
