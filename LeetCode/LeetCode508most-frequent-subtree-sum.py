#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 1:41 PM
# @Author  : Slade
# @File    : LeetCode508most-frequent-subtree-sum.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            ans.append(left + right + root.val)
            return left + right + root.val

        dfs(root)
        d = dict()
        for i in set(ans):
            d[i] = ans.count(i)
        maxCount = max(d.values())
        return [i[0] for i in d.items() if i[1] == maxCount]
