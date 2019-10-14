#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 3:11 PM
# @Author  : Slade
# @File    : LeetCode337house-robber-iii.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dp(root))

    def dp(self, root):
        if not root:
            return [0, 0]

        left = self.dp(root.left)
        right = self.dp(root.right)

        # [a,b],a为不考虑root.val下的max值，b为考虑当前root.val下的最大值
        return [max(left) + max(right), root.val + left[0] + right[0]]
