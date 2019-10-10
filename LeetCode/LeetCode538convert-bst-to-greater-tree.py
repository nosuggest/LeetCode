#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 12:08 AM
# @Author  : Slade
# @File    : LeetCode538convert-bst-to-greater-tree.py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.add = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        _ = self.convertBST(root.right)
        root.val += self.add
        self.add = root.val
        _ = self.convertBST(root.left)
        return root
