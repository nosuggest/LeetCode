#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 1:02 PM
# @Author  : Slade
# @File    : LeetCode230kth-smallest-element-in-a-bst.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def dfs(root, k):
            if root:
                dfs(root.left, k)
                self.ans.append(root.val)
                dfs(root.right, k)

        dfs(root, k)
        return self.ans[k - 1]


