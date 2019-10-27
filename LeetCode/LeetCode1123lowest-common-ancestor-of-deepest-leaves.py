#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 8:48 PM
# @Author  : Slade
# @File    : LeetCode1123lowest-common-ancestor-of-deepest-leaves.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def dfs(root, depth):
            if not root:
                return root, depth

            left, d1 = dfs(root.left, depth + 1)
            right, d2 = dfs(root.right, depth + 1)

            return left if d1 > d2 else right if d1 < d2 else root, max(d1, d2)

        return dfs(root, 0)[0]
