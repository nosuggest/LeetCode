#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 10:56 PM
# @Author  : Slade
# @File    : LeetCode965univalued-binary-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        cur = root.val
        while queue:
            node = queue.pop(0)
            if cur!=node.val:
                return False
            cur = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return True