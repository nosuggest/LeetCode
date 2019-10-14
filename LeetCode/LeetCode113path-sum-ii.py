#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 10:43 PM
# @Author  : Slade
# @File    : LeetCode113path-sum-ii.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        def dfs(root, sum, tmp):
            if not root:
                return
            if not root.left and not root.right and sum == root.val:
                self.ans.append(tmp + [root.val])
                return

            left = dfs(root.left, sum - root.val, tmp + [root.val])
            right = dfs(root.right, sum - root.val, tmp + [root.val])

            return

        return list(set(dfs(root, sum, [])))
