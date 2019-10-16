#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 9:40 AM
# @Author  : Slade
# @File    : LeetCode144binary-tree-preorder-traversal.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [root]
        output = []
        while queue:
            node = queue.pop()
            output.append(node.val)

            if node.right:
                queue.append(node.right)

            if node.left:
                queue.append(node.left)
        return output
