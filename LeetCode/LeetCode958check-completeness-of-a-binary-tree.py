#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 9:25 PM
# @Author  : Slade
# @File    : LeetCode958check-completeness-of-a-binary-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = [root]
        none_before = False
        while queue:
            node = queue.pop(0)
            if not node and not node:
                none_before = True

            elif none_before and node:
                return False

            if p:
                queue.extend([node.left, node.right])
        return True
