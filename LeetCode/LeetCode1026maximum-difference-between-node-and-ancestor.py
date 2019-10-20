#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 4:10 PM
# @Author  : Slade
# @File    : LeetCode1026maximum-difference-between-node-and-ancestor.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []

    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def dfs(root, tmp):
            if not root.left and not root.right:
                self.ans.append(tmp + [root.val])
                return

            if root.left:
                dfs(root.left, tmp + [root.val])

            if root.right:
                dfs(root.right, tmp + [root.val])

        dfs(root, [])
        return max([max(item) - min(item) for item in self.ans])