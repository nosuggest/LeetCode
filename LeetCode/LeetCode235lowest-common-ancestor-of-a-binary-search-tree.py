#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/13 4:56 PM
# @Author  : Slade
# @File    : LeetCode235lowest-common-ancestor-of-a-binary-search-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return left if right == None else right if left == None else root
