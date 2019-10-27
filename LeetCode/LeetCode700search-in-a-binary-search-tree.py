#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 12:33 PM
# @Author  : Slade
# @File    : LeetCode700search-in-a-binary-search-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val == val:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return None