#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 10:05 PM
# @Author  : Slade
# @File    : LeetCode112path-sum.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        def dfs(root, sum):
            if not root and sum == 0:
                return True

            if not root:
                return False

            left = dfs(root.left, sum - root.val)
            right = dfs(root.right, sum - root.val)

            return left if root.right is None else right if root.left is None else left or right

        return dfs(root, sum)
