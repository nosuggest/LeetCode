#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 9:37 AM
# @Author  : Slade
# @File    : LeetCode129sum-root-to-leaf-numbers.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def dfs(root, s):
            s = s + str(root.val)
            if root.left is None and root.right is None:
                self.ans.append(s)
                return
            if root.left is not None:
                dfs(root.left, s)
            if root.right is not None:
                dfs(root.right, s)

        dfs(root, "")
        return sum(map(int, self.ans))