#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 12:02 AM
# @Author  : Slade
# @File    : LeetCode515find-largest-value-in-each-tree-row.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None

        queue = [root]
        ans = []
        while queue:
            tmp = []
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(max(tmp))
        return ans
