#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 12:53 PM
# @Author  : Slade
# @File    : LeetCode783minimum-distance-between-bst-nodes.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = []
        ans = []
        cur = root
        while True:
            while cur:
                queue.append(cur)
                cur = cur.left
            if not queue:
                return min([abs(ans[i + 1] - ans[i]) for i in range(len(ans) - 1)])
            cur = queue.pop()
            ans.append(cur.val)
            cur = cur.right
        return min([abs(ans[i + 1] - ans[i]) for i in range(len(ans) - 1)])