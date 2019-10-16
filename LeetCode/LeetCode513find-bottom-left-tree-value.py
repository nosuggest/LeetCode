#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 11:58 PM
# @Author  : Slade
# @File    : LeetCode513find-bottom-left-tree-value.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None

        queue = [root]
        tmp = None
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if i == 0:
                    tmp = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return tmp
