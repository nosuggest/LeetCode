#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 8:58 AM
# @Author  : Slade
# @File    : LeetCode563binary-tree-tilt.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = 0

    def findTilt(self, root):
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

            '''每个结点左右求差'''
            self.ans += abs(left - right)

            '''每个结点求和'''
            return left + right + root.val

        dfs(root)
        return self.ans
