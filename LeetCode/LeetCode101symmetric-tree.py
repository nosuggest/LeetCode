#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/13 4:01 PM
# @Author  : Slade
# @File    : LeetCode101symmetric-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = [root.left, root.right]
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if left is None and right is None:
                continue
            if left is None:
                return False
            if right is None:
                return False
            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True
