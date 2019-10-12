#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 7:59 PM
# @Author  : Slade
# @File    : LeetCode236lowest-common-ancestor-of-a-binary-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        return left if right is None else right if left is None else root
