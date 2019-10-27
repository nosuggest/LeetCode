#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 8:40 PM
# @Author  : Slade
# @File    : LeetCode110balanced-binary-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            if left == -1:
                return -1
            right = dfs(root.right)
            if right ==-1:
                return -1
            return max(left,right)+1 if abs(left-right)<2 else -1
        return False if dfs(root)==-1 else True