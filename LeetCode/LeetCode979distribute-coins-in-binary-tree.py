#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 11:57 PM
# @Author  : Slade
# @File    : LeetCode979distribute-coins-in-binary-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = 0

    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            # abs(left),abs(right)是只当前结点的需要补充的金币量
            self.ans += abs(left) + abs(right)

            # 针对root结点来说，需要把多少left和right上的金币移到root上，但是root需要保留一个，多余的为多余量
            return root.val + left + right - 1

        dfs(root)
        return self.ans
